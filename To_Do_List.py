class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def mark_as_completed(self):
        
        self.completed = True

    def mark_as_incomplete(self):
        self.completed = False

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.name}: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def create_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)

    def update_task(self, task_name, completed):
        task = self.find_task(task_name)
        if task:
            if completed:
                task.mark_as_completed()
            else:
                task.mark_as_incomplete()
        else:
            print("Task not found!")

    def find_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None

    def display_tasks(self):
        print("To-Do List:")
        for task in self.tasks:
            print(task)

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Create Task")
        print("2. Update Task")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            todo_list.create_task(task_name)
        elif choice == "2":
            task_name = input("Enter task name: ")
            completed = input("Is it completed? (yes/no): ").lower() == "yes"
            todo_list.update_task(task_name, completed)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
