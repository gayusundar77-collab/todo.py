import json
import os

FILE = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add task
def add_task():
    tasks = load_tasks()
    name = input("\n Enter your task: ")
    
    task = {
        "name": name,
        "status": "Not Done"
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully")

# View tasks
def view_tasks():
    tasks = load_tasks()
    
    print("\n Your Tasks:")
    if len(tasks) == 0:
        print("No tasks available")
        return
    
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]['name']} - {tasks[i]['status']}")

# Mark as done
def mark_done():
    tasks = load_tasks()
    view_tasks()

    try:
        num = int(input("\n Enter task number to mark as done: "))
        if num >= 1 and num <= len(tasks):
            tasks[num-1]["status"] = "Done"
            save_tasks(tasks)
            print("Task marked as DONE")
        else:
            print("Invalid task number")
    except:
        print("Please enter a valid number")

# Delete task
def delete_task():
    tasks = load_tasks()
    view_tasks()

    try:
        num = int(input("\n Enter task number to delete: "))
        if num >= 1 and num <= len(tasks):
            tasks.pop(num-1)
            save_tasks(tasks)
            print("Task deleted successfully")
        else:
            print("Invalid task number")
    except:
        print("Please enter a valid number")

# Main menu
while True:
    print("\n TO-DO APP ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input(" Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting Your tasks are saved")
        break
    else:
        print("Invalid choice! Try again")