tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == '2':
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
    elif choice == '3':
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed task: {removed}")
        else:
            print("Invalid number.")
    elif choice == '4':
        print("Exiting To-Do List.")
        break
    else:
        print("Invalid option.")
