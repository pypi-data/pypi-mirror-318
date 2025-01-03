import time
from persistent_q import PersistentQSQLite

def manager(queue: PersistentQSQLite):
    while True:
        # Simulate resubmitting failed jobs
        print("Resubmitting failed jobs...")
        time.sleep(10)

if __name__ == "__main__":
    queue = PersistentQSQLite()
    manager(queue)