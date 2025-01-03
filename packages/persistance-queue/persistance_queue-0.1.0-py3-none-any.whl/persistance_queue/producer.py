import time
from persistent_q import PersistentQSQLite

def producer(queue: PersistentQSQLite):
    while True:
        job = f"Job {int(time.time())}"
        queue.put(job)
        print(f"Produced: {job}")
        time.sleep(5)

if __name__ == "__main__":
    queue = PersistentQSQLite()
    producer(queue)