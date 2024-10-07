

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def execute(self):
        print(f"Executing task: {self.name} with priority {self.priority}")

# Example task creation
if __name__ == '__main__':
    task1 = Task('Task 1', 2)
    task2 = Task('Task 2', 1)
    task1.execute()
    task2.execute()
