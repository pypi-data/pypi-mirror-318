import sqlite3
from persistent_q_interface import PersistentQInterface

class PersistentQSQLite(PersistentQInterface):
    def __init__(self, db_name: str = "persistent_queue.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, job TEXT)"""
        )

    def put(self, job: str) -> None:
        self.cursor.execute("INSERT INTO jobs (job) VALUES (?)", (job,))
        self.conn.commit()

    def get(self) -> str:
        self.cursor.execute("SELECT job FROM jobs ORDER BY id LIMIT 1")
        job = self.cursor.fetchone()
        if job:
            return job[0]
        return None

    def delete(self, job: str) -> None:
        self.cursor.execute("DELETE FROM jobs WHERE job = ?", (job,))
        self.conn.commit()

    def size(self) -> int:
        self.cursor.execute("SELECT COUNT(*) FROM jobs")
        return self.cursor.fetchone()[0]