def add_task(tasks):
    """Prompt for a task description, add it to `tasks`, and confirm."""
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


def view_tasks(tasks):
    """Display all tasks numbered from 1, or a message if empty."""
    if not tasks:
        print("Your to-do list is empty.")
        return

    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task(tasks):
    """Show the tasks, ask which number to remove, then remove it."""
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.")
        return

    view_tasks(tasks)
    choice = input("Enter task number to delete: ")

    try:
        index = int(choice)
    except ValueError:
        print("Error: Please enter a valid task number.")
        return

    if index < 1 or index > len(tasks):
        print("Error: Invalid task number.")
        return

    removed = tasks.pop(index - 1)
    print(f'Task "{removed}" has been removed.')


def print_menu():
    """Display the to-do list menu."""
    print("============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def main():
    tasks = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please choose a number between 1 and 4.")

        print()


if __name__ == "__main__":
    main()
