class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
    def update_task(self, index, new_task):
        try:
            self.tasks[index - 1] = new_task
        except IndexError:
            print("Invalid task index.")
    def delete_task(self, index):
        try:
            del self.tasks[index - 1]
        except IndexError:
            print("Invalid task index.")
def main():
    to_do_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter a task: ")
            to_do_list.add_task(task)
        elif choice == "2":
            to_do_list.view_tasks()
        elif choice == "3":
            index = int(input("Enter task index: "))
            new_task = input("Enter new task: ")
            to_do_list.update_task(index, new_task)
        elif choice == "4":
            index = int(input("Enter task index: "))
            to_do_list.delete_task(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
