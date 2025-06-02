# simple to do application

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# add a task
def add_task(tasks,task):
    tasks.append(task)
    print(f"Task '{task}' added.")

# remove a task
def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

# main function
def main():
    tasks = []
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter a task: ")
            add_task(tasks, task)
        elif choice == "2":
            task = input("Enter a task to remove: ")
            remove_task(tasks, task)
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
