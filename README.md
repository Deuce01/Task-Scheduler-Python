# **Task Scheduler with Advanced Python Features** 🛠️

### **Project Overview**

This project is a **Task Scheduler** built using advanced Python features such as **decorators**, **context managers**, **generators**, and **lambda functions**. The scheduler allows users to create tasks with priorities, schedule them for execution, and log their execution in a log file.

---

### **Features**

- **Task Management**: Create tasks with specific names and priorities.
- **Task Execution**: Schedule tasks and execute them one at a time.
- **Logging**: Automatically logs the execution of each task with a custom **context manager**.
- **Timing Decorator**: Tracks and logs the time taken for task execution using a **decorator**.
- **Lazy Execution**: Uses a **generator** to yield tasks dynamically, minimizing memory usage.
- **Lambda Functions**: Efficiently sorts tasks by priority before execution.

---

### **Technologies Used**

- **Python** 🐍
  - **Decorators**: Modify task execution behavior dynamically.
  - **Context Managers**: Manage log file operations (open/close).
  - **Generators**: Lazily yield tasks for execution, one at a time.
  - **Lambda Functions**: Sort and filter tasks based on priority.

---

### **Project Structure**

```plaintext
task_scheduler/
│
├── task_scheduler.py        # Main script with all logic
├── scheduler.py             # File for scheduling logic and task execution
├── tasks.py                 # File to define and manage task creation
├── logs/                    # Directory for log files
└── task_log.txt             # Log file for recording task execution
```

---

### **How It Works**

1. **Create Tasks**: Tasks are created with a name and a priority.
2. **Schedule Tasks**: Tasks are scheduled for execution based on their priority.
3. **Log Execution**: Task execution is logged into a log file using a context manager.
4. **Execution Time**: The task scheduling process is timed using a decorator.
5. **Dynamic Execution**: Tasks are processed one by one using a generator, ensuring efficient memory usage.

---

### **Getting Started**

#### **1. Clone the repository**:


#### **2. Navigate to the project directory**:
```bash
cd task_scheduler
```

#### **3. Run the Task Scheduler**:
```bash
python task_scheduler.py
```

---

### **Example Usage**

In `task_scheduler.py`, tasks are created, sorted, and scheduled for execution:

```python
from tasks import Task
from scheduler import schedule_tasks

# Create tasks with different priorities
task1 = Task('Task 1', 2)
task2 = Task('Task 2', 1)
task3 = Task('Task 3', 3)

# Sort tasks using lambda by priority (ascending order)
sorted_tasks = sorted([task1, task2, task3], key=lambda task: task.priority)

# Schedule and execute tasks
schedule_tasks(sorted_tasks)
```

**Output**:
```plaintext
Opening log file: logs/task_log.txt
Executing task: Task 2 with priority 1
Executing task: Task 1 with priority 2
Executing task: Task 3 with priority 3
Closing log file: logs/task_log.txt
schedule_tasks executed in 0.0040 seconds
```

---

### **Project Features Breakdown**

- **Decorators**:
  - `log_execution_time`: Times and logs the task scheduling and execution process.
  
- **Context Managers**:
  - `TaskLogContextManager`: Manages the opening and closing of the log file.

- **Generators**:
  - `task_generator`: Lazily yields tasks one by one for execution.

- **Lambda Functions**:
  - `lambda task: task.priority`: Sorts tasks by their priority in ascending order.

---

### **Future Improvements**

- Add a UI to visualize tasks and their priorities.
- Implement recurring tasks functionality.
- Support for task dependencies (e.g., task B cannot run until task A completes).
  
---


**Happy Coding!** 🎉
