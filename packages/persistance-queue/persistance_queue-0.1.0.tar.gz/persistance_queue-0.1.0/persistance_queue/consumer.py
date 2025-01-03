import time
import random
from persistent_q import PersistentQSQLite

def consumer(queue: PersistentQSQLite):
    while True:
        job = queue.get()
        if job:
            print(f"Consumed: {job}")
            queue.delete(job)
        time.sleep(random.randint(7, 15))

if __name__ == "__main__":
    queue = PersistentQSQLite()
    consumer(queue)