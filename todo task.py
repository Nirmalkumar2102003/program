tasks = []

def add_task():
    task = input("Enter task: ")
    if task not in tasks:
        tasks.append(task)
        with open("C:/Users/nirmal/Desktop/file.txt", 'a') as file:
            file.write(task + "\n")
        print("Task added")
    else:
        print("Existing task")

def complete_task():
    task = input("Enter task to mark as completed: ")
    if task in tasks:
        tasks.remove(task)
        with open("C:/Users/nirmal/Desktop/file.txt", "w") as file:
            for t in tasks:
                file.write(t + "\n")
        print("Task", task, "completed.")
    else:
        print("Task not found.")

def pending_tasks():
    print("Pending tasks:")
    with open("C:/Users/nirmal/Desktop/file.txt", "r") as file:
        for task in file:
            print(task.strip())

def quit_program():
    print("Exiting program.")
    quit()

while True:
    print("\n1. Add Task\n2. Complete Task\n3. View Pending Tasks\n4. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        complete_task()
    elif choice == '3':
        pending_tasks()
    elif choice == '4':
        quit_program()
    else:
        print("Invalid choice. Please try again.")
