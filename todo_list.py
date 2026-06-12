tasks = []

while True:
print("\n--- TO DO LIST ---")
print("1. Add Task")
print("2. View Tasks")
print("3. Remove Task")
print("4. Mark Task as Completed")
print("5. Exit")

choice = input("Enter your choice: ")  

# Add Task  
if choice == "1":  
    task = input("Enter task: ")  
    tasks.append(task)  
    print("Task added successfully!")  

# View Tasks  
elif choice == "2":  
    if len(tasks) == 0:  
        print("No tasks available.")  
    else:  
        print("\nYour Tasks:")  
        for i, task in enumerate(tasks, start=1):  
            print(f"{i}. {task}")  

# Remove Task  
elif choice == "3":  
    if len(tasks) == 0:  
        print("No tasks to remove.")  
    else:  
        for i, task in enumerate(tasks, start=1):  
            print(f"{i}. {task}")  

        remove = int(input("Enter task number to remove: "))  

        if 1 <= remove <= len(tasks):  
            deleted = tasks.pop(remove - 1)  
            print(f"'{deleted}' removed successfully!")  
        else:  
            print("Invalid task number.")  

# Mark Task as Completed  
elif choice == "4":  
    if len(tasks) == 0:  
        print("No task to mark as completed.")  
    else:  
        for i, task in enumerate(tasks, start=1):  
            print(f"{i}. {task}")  

        marked_task = int(input("Enter task number to mark as completed: "))  

        if 1 <= marked_task <= len(tasks):  
            tasks[marked_task - 1] = "✔ " + tasks[marked_task - 1]  
            print("Task marked as completed!")  
        else:  
            print("Invalid task number.")  

# Exit  
elif choice == "5":  
    print("Exiting To-Do List...")  
    break  

else:  
    print("Invalid choice. Try again.")

