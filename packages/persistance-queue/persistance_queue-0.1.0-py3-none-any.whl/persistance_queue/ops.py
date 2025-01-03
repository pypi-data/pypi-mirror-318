import time
from persistent_q import PersistentQSQLite

def ops(queue: PersistentQSQLite):
    while True:
        print(f"Queue size: {queue.size()}")
        time.sleep(5)

if __name__ == "__main__":
    queue = PersistentQSQLite()
    ops(queue)