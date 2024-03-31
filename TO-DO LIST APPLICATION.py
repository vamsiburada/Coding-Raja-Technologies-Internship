import os
import datetime

# Function to add a task
def add_task(tasks):
    name = input("Enter task name: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    tasks.append({"name": name, "priority": priority, "due_date": due_date, "completed": False})

# Function to remove a task
def remove_task(tasks):
    index = int(input("Enter the index of the task to remove: "))
    if 0 <= index < len(tasks):
        del tasks[index]
    else:
        print("Invalid index")

# Function to mark a task as completed
def mark_completed(tasks):
    index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
    else:
        print("Invalid index")

# Function to display all tasks
def display_tasks(tasks):
    for index, task in enumerate(tasks):
        print(f"{index}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")

# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['name']},{task['priority']},{task['due_date']},{task['completed']}\n")

# Function to load tasks from a file
def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                name, priority, due_date, completed = line.strip().split(",")
                tasks.append({"name": name, "priority": priority, "due_date": due_date, "completed": completed == "True"})
    return tasks

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
