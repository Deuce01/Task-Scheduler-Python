
import time
from tasks import Task

# Decorator to log task execution time
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Context manager to handle logging
class TaskLogContextManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        print(f"Opening log file: {self.file_name}")
        self.file = open(self.file_name, 'a')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing log file: {self.file_name}")
        if self.file:
            self.file.close()

# Generator to yield tasks one at a time
def task_generator(tasks):
    for task in tasks:
        yield task

@log_execution_time
def schedule_tasks(tasks):
    with TaskLogContextManager('logs/task_log.txt') as log_file:
        task_gen = task_generator(tasks)
        for task in task_gen:
            task.execute()
            log_file.write(f"Task {task.name} with priority {task.priority} executed\n")
