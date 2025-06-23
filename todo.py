tasks = []

def show_menu():
    print("\nWhat do you want to do?")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Type your new task: ")
    tasks.append(task)
    print("Task added.")

def complete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Which task number is done? ")) - 1
            print(f"Great! You completed: {tasks[num]}")
            tasks.pop(num)
        except:
            print("Invalid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Which task number to delete? ")) - 1
            print(f"Deleted: {tasks[num]}")
            tasks.pop(num)
        except:
            print("Invalid number.")

# The main program loop
while True:
    show_menu()
    choice = input("Choose 1 to 5: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please choose a number from 1 to 5.")
