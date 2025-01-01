import curses
import importlib.util
import inspect
import json
import os
import queue
import sys
import tempfile
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, Optional
from .db import JobMonitorDB


@dataclass
class Job:
    name: str
    total: int
    current: int = 0
    status: str = "running"
    start_time: datetime = field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    error: Optional[str] = None
    pid: Optional[int] = None

    @property
    def progress(self) -> float:
        """Calculate job progress."""
        return (self.current / self.total) * 100 if self.total > 0 else 0

    @property
    def elapsed_time(self) -> float:
        """Calculate elapsed time in seconds."""
        end = self.end_time if self.end_time else datetime.now()
        return (end - self.start_time).total_seconds()

    @property
    def job_time(self) -> float:
        """Calculate elapsed time in seconds."""
        return (self.end_time - self.start_time).total_seconds()

    def complete(self) -> None:
        """Mark job as complete and set end time."""
        if not self.end_time:
            self.end_time = datetime.now()

    def to_dict(self):
        return {
            "name": self.name,
            "total": self.total,
            "current": self.current,
            "status": self.status,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "error": self.error,
            "pid": self.pid,
        }

    @classmethod
    def from_dict(cls, data):
        data["start_time"] = datetime.fromisoformat(data["start_time"])
        if data.get("end_time"):
            data["end_time"] = datetime.fromisoformat(data["end_time"])
        return cls(**data)


class JobMonitor:
    STATE_FILE = os.path.join(tempfile.gettempdir(), "pyjob_state.json")

    def __init__(self):
        self.jobs: Dict[str, Job] = {}
        self._lock = threading.Lock()
        self._update_queue = queue.Queue()
        self._stop_event = threading.Event()
        self._display_thread = threading.Thread(target=self._display_progress)
        self._display_thread.daemon = True
        self.pid = os.getpid()
        self._db_lock = threading.Lock()

    def _get_db(self):
        """Get thread-local database connection."""
        if not hasattr(threading.current_thread(), "_db"):
            threading.current_thread()._db = JobMonitorDB()
        return threading.current_thread()._db

    def save_state(self):
        """Save current state to file."""
        state = {
            "pid": self.pid,
            "jobs": {name: job.to_dict() for name, job in self.jobs.items()},
        }
        with open(self.STATE_FILE, "w") as f:
            json.dump(state, f)

    def are_all_jobs_complete(self) -> bool:
        """Check if all jobs are either completed or errored."""
        return all(job.status in ["completed", "error"] for job in self.jobs.values())

    @classmethod
    def load_state(cls):
        """Load state from file."""
        try:
            with open(cls.STATE_FILE, "r") as f:
                state = json.load(f)

            monitor = cls()
            monitor.pid = state["pid"]
            monitor.jobs = {
                name: Job.from_dict(job_data)
                for name, job_data in state["jobs"].items()
            }
            return monitor
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def add(self, name: str, total: int) -> None:
        with self._lock:
            self.jobs[name] = Job(name=name, total=total, pid=self.pid)
            self.save_state()

    def update(self, name: str, current: int, status: str = "running") -> None:
        self._update_queue.put(("update", name, current, status))

        with self._lock:
            if name in self.jobs:
                job = self.jobs[name]
                job.current = current
                job.status = status

                self.save_state()

    def error(self, name: str, error: str) -> None:
        self._update_queue.put(("error", name, error))

        with self._lock:
            if name in self.jobs:
                job = self.jobs[name]
                job.error = error

                self.save_state()

    def done(self, name: str) -> None:
        self._update_queue.put(("complete", name))
        job = self.jobs[name]

        job.status = "completed"
        job.current = job.total
        job.complete()

        with self._db_lock:
            db = self._get_db()
            db.add_job(
                name, job.total, job.start_time, job.end_time, job.job_time, job.error
            )

        self.save_state()

    def start(self) -> None:
        """Start monitoring."""
        if not self._display_thread.is_alive():
            self._stop_event.clear()
            self._display_thread.start()

    def stop(self) -> None:
        """Stop monitoring."""
        self._stop_event.set()
        if self._display_thread.is_alive():
            self._display_thread.join()

        try:
            os.remove(self.STATE_FILE)
        except FileNotFoundError:
            pass

    def _process_update(self, update_type: str, name: str, *args) -> None:
        """Process updates from the queue."""
        with self._lock:
            if name not in self.jobs:
                return

            job = self.jobs[name]
            if update_type == "update":
                current, status = args
                job.current = current
                job.status = status
            elif update_type == "error":
                (error,) = args
                job.status = "error"
                job.error = error
            elif update_type == "complete":
                job.status = "completed"
                job.current = job.total
                job.complete()

            self.save_state()

    def _display_progress(self) -> None:
        """Display progress of all jobs in the terminal."""

        def init_curses(stdscr):
            curses.start_color()
            curses.use_default_colors()
            curses.init_pair(1, curses.COLOR_GREEN, -1)  # Success
            curses.init_pair(2, curses.COLOR_RED, -1)  # Error
            curses.init_pair(3, curses.COLOR_YELLOW, -1)  # Running
            curses.init_pair(4, curses.COLOR_BLUE, -1)  # Info
            return stdscr

        def draw_progress(stdscr):
            while not self._stop_event.is_set():
                try:
                    while True:
                        try:
                            update = self._update_queue.get_nowait()
                            self._process_update(*update)
                        except queue.Empty:
                            break

                    stdscr.clear()

                    # Draw header
                    header = "PyJob Monitor"
                    stdscr.addstr(0, 0, "=" * curses.COLS)
                    stdscr.addstr(
                        1,
                        (curses.COLS - len(header)) // 2,
                        header,
                        curses.color_pair(4) | curses.A_BOLD,
                    )
                    stdscr.addstr(2, 0, "=" * curses.COLS)

                    with self._lock:
                        for i, (_, job) in enumerate(sorted(self.jobs.items())):
                            base_line = i * 4 + 4

                            status_color = {
                                "running": 3,  # yellow
                                "completed": 1,  # green
                                "error": 2,  # red
                            }.get(job.status, 0)

                            # Job name and status
                            name_status = f"{job.name}: [{job.status.upper()}]"
                            stdscr.addstr(
                                base_line,
                                0,
                                name_status,
                                curses.color_pair(status_color),
                            )

                            # Time elapsed for job
                            elapsed = f"Time: {job.elapsed_time:.1f}s - {job.current} / {job.total}"
                            stdscr.addstr(
                                base_line, curses.COLS - len(elapsed) - 1, elapsed
                            )

                            # Progress bar
                            width = curses.COLS - 20
                            filled = int((width * job.progress) / 100)
                            bar = f"[{'=' * filled}{' ' * (width - filled)}]"
                            progress_text = f"{bar} {job.progress:.1f}%"
                            stdscr.addstr(base_line + 1, 2, progress_text)

                            if job.error:
                                error_msg = f"Error: {job.error}"
                                stdscr.addstr(
                                    base_line + 2, 2, error_msg, curses.color_pair(2)
                                )

                    stdscr.refresh()
                    time.sleep(0.1)

                except KeyboardInterrupt:
                    break

        curses.wrapper(lambda stdscr: draw_progress(init_curses(stdscr)))


class ScriptError(Exception):
    pass


class ScriptLoader:
    """Loads the python scripts"""

    @staticmethod
    def load(script_path: str) -> Callable[[Any], None]:
        """
        Load a Python script and return its main function.

        Args:
            script_path (str): Path to the script

        Returns:
            Callable: The main function from the script

        Raises:
            ScriptError: If script can't be loaded or doesn't meet requirements
            ImportError: If script imports can't be resolved
        """
        try:
            script_path = os.path.abspath(script_path)

            if not os.path.exists(script_path):
                raise ScriptError(f"Script not found: {script_path}")

            if not script_path.endswith(".py"):
                raise ScriptError(f"File must be a Python script (.py): {script_path}")

            module_name = ScriptLoader._get_module_name(script_path)

            spec = importlib.util.spec_from_file_location(module_name, script_path)
            if spec is None or spec.loader is None:
                raise ScriptError(f"Could not load script spec: {script_path}")

            module = importlib.util.module_from_spec(spec)

            sys.modules[module_name] = module

            try:
                spec.loader.exec_module(module)
            except Exception as e:
                raise ScriptError(f"Error executing script: {str(e)}")

            if not hasattr(module, "main"):
                raise ScriptError(
                    f"Script must have a 'main' function: {script_path}\n"
                    "Example:\n"
                    "def main(monitor, **kwargs):\n"
                    "    monitor.add('my_job', total_items)\n"
                    "    try:\n"
                    "        # Your code here\n"
                    "    except Exception as e:\n"
                    "        monitor.error('my_job', str(e))"
                    "    monitor.done('my_job')\n"
                )

            main_func = getattr(module, "main")

            ScriptLoader._validate_main_function(main_func, script_path)

            return main_func

        except ImportError as e:
            raise ImportError(f"Error importing script {script_path}: {str(e)}")
        except Exception as e:
            raise ScriptError(f"Error loading script {script_path}: {str(e)}")

    @staticmethod
    def _get_module_name(script_path: str) -> str:
        """
        Generate a unique module name from the script path.

        Args:
            script_path (str): Path to the Python script

        Returns:
            str: Unique module name
        """

        path = Path(script_path)
        module_name = f"pyjob_script_{path.stem}_{hash(str(path.absolute()))}"
        return module_name

    @staticmethod
    def _validate_main_function(func: Callable, script_path: str) -> None:
        """
        Validate the main function signature and requirements.

        Args:
            func (Callable): The main function to validate
            script_path (str): Path to script (for error messages)

        Raises:
            ScriptError: If function doesn't meet requirements
        """
        sig = inspect.signature(func)
        params = sig.parameters

        if len(params) < 1:
            raise ScriptError(
                f"Main function in {script_path} must accept at least one parameter "
                "(the monitor instance)"
            )

        if len(params) > 1:
            second_param = list(params.values())[1]
            if second_param.kind != inspect.Parameter.VAR_KEYWORD:
                raise ScriptError(
                    f"Second parameter of main function in {script_path} must be **kwargs "
                    "to accept configuration options"
                )


def load_config(config_path: str) -> Dict:
    """
    Load and validate configuration file.

    Args:
        config_path (str): Path to JSON config file

    Returns:
        Dict: Configuration dictionary

    Raises:
        ScriptError: If config file is invalid
    """
    try:
        import json

        with open(config_path, "r") as f:
            config = json.load(f)

        if not isinstance(config, dict):
            raise ScriptError("Config file must contain a JSON object")

        return config

    except json.JSONDecodeError as e:
        raise ScriptError(f"Invalid JSON in config file: {str(e)}")
    except Exception as e:
        raise ScriptError(f"Error loading config file: {str(e)}")
