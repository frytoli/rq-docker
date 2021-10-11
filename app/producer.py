#!/usr/bin/env python3

from redis import Redis
from rq import Queue
import consumer
import random
import time
import os

def main():
    # Connect to queue
    redis_conn = Redis(
        host=os.getenv('REDIS_HOST'),
        port=os.getenv('REDIS_PORT')
    )
    redis_queue = Queue(connection=redis_conn)
    # Create an empty list to record queued tasks
    tasks = []
    # Send tasks to queue
    for i in range(10):
        tasks.append(
            redis_queue.enqueue(consumer.pythagorean_theorem, args=(random.randint(5,15),random.randint(5,15)))
        )

    # Retrieve results
    completed_tasks = 0
    # While number of completed tasks is less than the number of queued tasks...
    while completed_tasks < len(tasks):
        # Check the status of each task and output the result if one has been returned
        for task in tasks:
            if task.get_status(refresh=True) in ['finished', 'stopped', 'canceled', 'failed']: # Status options: https://python-rq.org/docs/jobs/#retrieving-jobs
                completed_tasks += 1
                print(f'Right triangle with sides {task.args} has hypotenuse {task.result}')
            if completed_tasks < len(tasks):
                print('Tasks still finishing. Will check again in 5 seconds...')
                time.sleep(5)



if __name__ == '__main__':
    main()
