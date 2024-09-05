class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
            return
        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, 1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{idx}. {task['task']} [{status}]")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks.pop(task_index)
            print(f"Task '{task['task']}' deleted.")
        else:
            print("Invalid task number.")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            print(f"Task '{self.tasks[task_index]['task']}' marked as completed.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Mark Task Completed\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            todo_list.view_tasks()
            task_num = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(task_num)

        elif choice == '4':
            todo_list.view_tasks()
            task_num = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_completed(task_num)

        elif choice == '5':
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
