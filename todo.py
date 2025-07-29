class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'"{task}" added to the list.')

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f'"{removed}" removed from the list.')
        else:
            print("Invalid task number.")

todo = ToDoList()

while True:
    print("\n1. Add Task\n2. Show Tasks\n3. Delete Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter your task: ")
        todo.add_task(task)
    elif choice == "2":
        todo.show_tasks()
    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        todo.delete_task(num)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
