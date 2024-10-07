
from tasks import Task
from scheduler import schedule_tasks

# Create tasks with different priorities
task1 = Task('Task 1', 2)
task2 = Task('Task 2', 1)
task3 = Task('Task 3', 3)

# Store tasks in a list
tasks = [task1, task2, task3]

# Sort tasks using lambda by priority (ascending order)
sorted_tasks = sorted(tasks, key=lambda task: task.priority)

# Schedule tasks for execution
schedule_tasks(sorted_tasks)
