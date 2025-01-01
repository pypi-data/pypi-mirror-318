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

            time.sleep(1)

            if monitor.are_all_jobs_complete():
                monitor.stop()
                sys.exit(0)

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
    monitor = JobMonitor.load_state()

    if monitor is None:
        return

    monitor.start()

    try:
        while True:
            time.sleep(0.1)
            if monitor.are_all_jobs_complete():
                break
    finally:
        monitor.stop()


def show_db_jobs(args):
    """Display jobs from database in a formatted table."""
    db = JobMonitorDB()
    jobs = {}

    if args.error:
        error_jobs = db.show_error_message(id=args.error)
        if not error_jobs:
            print(f"No error message found for job ID: {args.error}")
            return
        print("=" * os.get_terminal_size().columns)
        print(f"Error message for Job ID: {args.error}")
        print("=" * os.get_terminal_size().columns)
        print(error_jobs[0][-1] if error_jobs[0][-1] else "No error message")
        return

    if args.name:
        jobs = db.get_jobs_by_name(name=args.name)
    else:
        jobs = db.get_jobs()

    if not jobs:
        print("No jobs found in database.")
        return

    term_width = os.get_terminal_size().columns
    headers = [
        "Id",
        "Job Name",
        "Total Items",
        "Start Time",
        "End Time",
        "Duration (s)",
        "Error",
    ]

    col_width = max(10, term_width // len(headers))

    print("=" * term_width)
    print("Job History")
    print("=" * term_width)

    format_str = (
        f"{{:<{col_width}}}"  # Id
        f"{{:>{col_width}}}"  # Job Name
        f"{{:>{col_width}}}"  # Total Items (right-aligned)
        f"{{:>{col_width}}}"  # Start Time
        f"{{:>{col_width}}}"  # End Time
        f"{{:>{col_width}}}"  # Duration
        f"{{:>{col_width}}}"  # Error
    )

    print(format_str.format(*headers))
    print("-" * term_width)

    for job in jobs:
        id, name, total, start, end, duration, error = job

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
            id,
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

    db_parser = subparsers.add_parser("db", help="Database operations")
    db_subparsers = db_parser.add_subparsers(
        dest="db_command", help="Database commands"
    )

    db_init = db_subparsers.add_parser(
        "init", help="Initialize the pyjob db at ~/.pyjob/pyjob.db."
    )

    db_show = db_subparsers.add_parser(
        "show", help="Show the historical jobs from the database"
    )
    db_show.add_argument("--name", "-n", help="Add the name of the job to show")
    db_show.add_argument(
        "--error",
        "-e",
        help="Show error message of a job followed by job id: pyjob show -e 1",
    )
    db_subparsers.add_parser("clear", help="Clears all job history from database")

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
    elif args.command == "db":
        if args.db_command == "show":
            show_db_jobs(args)
        elif args.db_command == "clear":
            db = JobMonitorDB()
            db.reset_db()
            print("Database history cleared")
        elif args.db_command == "init":
            initialize_db()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
