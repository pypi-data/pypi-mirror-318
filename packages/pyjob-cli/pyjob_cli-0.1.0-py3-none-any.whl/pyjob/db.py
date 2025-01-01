import sqlite3
import os
from datetime import datetime

DEFAULT_DB_PATH = os.path.expanduser("~/.pyjob/pyjob.db")


def ensure_db_dir():
    db_dir = os.path.dirname(DEFAULT_DB_PATH)
    os.makedirs(db_dir, exist_ok=True)


def initialize_db():
    ensure_db_dir()

    conn = sqlite3.connect(DEFAULT_DB_PATH)
    cursor = conn.cursor()

    # Jobs Table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            total INTEGER,
            start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            end_time TIMESTAMP,
            elapsed_seconds REAL,
            error TEXT
        )
        """
    )

    conn.commit()
    conn.close()

    print(f"Database initialized at: {DEFAULT_DB_PATH}")


def get_connection():
    ensure_db_dir()
    return sqlite3.connect(DEFAULT_DB_PATH)


class JobMonitorDB:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def add_job(
        self,
        name: str,
        total: int,
        start_time: datetime,
        end_time: datetime,
        elapsed_seconds: float,
        error: str,
    ) -> int:
        self.cursor.execute(
            "INSERT INTO jobs (name, total, start_time, end_time, elapsed_seconds, error) VALUES (?, ?, ?, ?, ?, ?)",
            (name, total, start_time, end_time, elapsed_seconds, error),
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_jobs(self):
        """Get all jobs for a run."""
        self.cursor.execute("SELECT * FROM jobs")
        return self.cursor.fetchall()

    def get_jobs_by_name(self, name):
        self.cursor.execute("SELECT * FROM jobs WHERE name = ?", (name,))
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.conn.close()
