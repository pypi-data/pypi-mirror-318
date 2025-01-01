import os
import sys
import argparse
import json
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from .db import initialize_db, JobMonitorDB
from .utils import JobMonitor, ScriptLoader


def run_scripts(args):
    """Run scripts in background or foreground."""
    config = {}
    if args.config:
        with open(args.config) as f:
            config = json.load(f)

    scripts = []
    for path in args.scripts:
        try:
            main_func = ScriptLoader.load(path)
            scripts.append((path, main_func))
        except ImportError as e:
            print(f"Error loading {path}: {e}")
            return

    monitor = JobMonitor()

    if args.background:
        pid = os.fork()
        if pid > 0:
            print(f"Started background process with PID {pid}")
            sys.exit(0)

        print(f"Background process started with PID: {os.getpid()}")

        with open(os.devnull, "w") as devnull:
            sys.stdout = devnull
            sys.stderr = devnull

        max_workers = args.workers if args.workers is not None else len(scripts)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for path, main_func in scripts:
                script_config = config.get(Path(path).stem, {})
                future = executor.submit(main_func, monitor, **script_config)
                futures.append(future)

            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    if args.verbose:
                        print(f"Error in script: {e}")
            monitor.stop()

            try:
                os.remove(monitor.STATE_FILE)
            except FileNotFoundError:
                pass
            sys.exit(0)
    else:
        monitor.start()
        max_workers = args.workers if args.workers is not None else len(scripts)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for path, main_func in scripts:
                script_config = config.get(Path(path).stem, {})
                future = executor.submit(main_func, monitor, **script_config)
                futures.append(future)

            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    if args.verbose:
                        print(f"Error in script: {e}")
        monitor.stop()


def show_progress(args):
    """Show progress of running jobs."""
    state_file = JobMonitor.STATE_FILE
    if os.path.exists(state_file):
        with open(state_file, "r") as f:
            print(f.read())

    monitor = JobMonitor.load_state()

    if monitor is None:
        return

    monitor.start()
    try:
        while True:
            time.sleep(0.1)
            if monitor.are_all_jobs_complete():
                break
    except KeyboardInterrupt:
        monitor.stop()
    finally:
        monitor.stop()


def show_db_jobs(args):
    """Display jobs from database in a formatted table."""
    db = JobMonitorDB()
    jobs = {}
    if args.name:
        jobs = db.get_jobs_by_name(name=args.name)
    else:
        jobs = db.get_jobs()

    if not jobs:
        print("No jobs found in database.")
        return

    term_width = os.get_terminal_size().columns
    headers = [
        "Job Name",
        "Total Items",
        "Start Time",
        "End Time",
        "Duration (s)",
        "Error",
    ]

    col_width = max(10, term_width // len(headers))  # Minimum width of 10

    print("=" * term_width)
    print("Job History")
    print("=" * term_width)

    format_str = (
        f"{{:<{col_width}}}"  # Job Name
        f"{{:>{col_width}}}"  # Total Items (right-aligned)
        f"{{:>{col_width}}}"  # Start Time
        f"{{:>{col_width}}}"  # End Time
        f"{{:>{col_width}}}"  # Duration
        f"{{:<{col_width}}}"  # Error (left-aligned)
    )

    print(format_str.format(*headers))
    print("-" * term_width)

    for job in jobs:
        _, name, total, start, end, duration, error = job

        name = str(name) if name else "N/A"
        total = str(total) if total else "0"

        try:
            start_time = (
                datetime.fromisoformat(start).strftime("%Y-%m-%d %H:%M:%S")
                if start
                else "N/A"
            )
        except (ValueError, TypeError):
            start_time = "N/A"

        try:
            end_time = (
                datetime.fromisoformat(end).strftime("%Y-%m-%d %H:%M:%S")
                if end
                else "Running"
            )
        except (ValueError, TypeError):
            end_time = "N/A"

        duration_str = f"{duration:.2f}" if duration else "-"
        error = str(error) if error else "-"

        def truncate(s, w):
            return s[: w - 3] + "..." if len(s) > w else s

        row = [
            truncate(name, col_width),
            truncate(total, col_width),
            truncate(start_time, col_width),
            truncate(end_time, col_width),
            truncate(duration_str, col_width),
            truncate(error, col_width),
        ]

        try:
            print(format_str.format(*row))
        except Exception as e:
            print(f"Error formatting row: {row}")
            print(f"Error: {e}")
            continue

    print("=" * term_width)


def main():
    parser = argparse.ArgumentParser(description="pyjob - Python Job Monitor CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    subparsers.add_parser("show", help="Show progress of running jobs")
    subparsers.add_parser("init", help="Initialize pyjob db.")
    show_db_parser = subparsers.add_parser(
        "show_db", help="Show the historical jobs from the database."
    )
    show_db_parser.add_argument("--name", "-n", help="Add the name of the job to show.")

    run_parser = subparsers.add_parser("run", help="Run scripts")
    run_parser.add_argument(
        "scripts", nargs="+", help="Python scripts to run and monitor"
    )
    run_parser.add_argument("--config", "-c", help="Configuration JSON file")
    run_parser.add_argument(
        "--workers",
        "-w",
        type=int,
        default=None,
        help="Maximum number of concurrent workers",
    )
    run_parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show detailed output"
    )
    run_parser.add_argument(
        "--background", "-b", action="store_true", help="Run in background mode"
    )

    args = parser.parse_args()

    if args.command == "run":
        run_scripts(args)
    elif args.command == "show":
        show_progress(args)
    elif args.command == "init":
        initialize_db()
    elif args.command == "show_db":
        show_db_jobs(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
