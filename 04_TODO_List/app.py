# TODO List App
# ==============

import time
import os

# Function to get a valid input from the user
def valid_input(prompt, valid_choice):
    while True:
        try:
            user_input = input(prompt)
            if user_input not in valid_choice:
                raise Exception("Invalid Choice!! Try agian.")
            return user_input
        except Exception as e:
            print(f"Error: {e}")

tasks = {
    "1" : "Add Task",
    "2" : "Delete Task",
    "3" : "Update Task",
    "4" : "View Tasks",
    "5" : "Exit"
}

todo_tasks = []

def get_filename():
    # get the filename from the user
    filename = input("Enter the filename of your TODO list (example: work.txt): ").strip()
    
    if not filename.endswith(".txt"):
        filename += ".txt"
    
    if not os.path.exists(filename):
        with open(filename, "w"):  # Create an empty file if it doesn't exist
            pass
    
    return filename
            

# Function to add new tasks in the TODO list
def add_task(filename):
    task = input("Add your task: ")
    
    task_list = [task for task in task.split(", ") if task.strip()]
    
    with open(filename, "a") as file:
        for task in task_list:
            todo_tasks.append(task)
            file.write(task + "\n")
    print("Taks added successfully.")

def del_task(filename):
    print("Task in your TODO list")
    for index, task in enumerate(todo_tasks, start=1):
        print(f"{index}. {task}")
    
    if not todo_tasks:
        print("No tasks to delete.")
        return
    
    ask_task_number = valid_input("Tell task number to delete: ",
                                   [str(i) for i in range(1, len(todo_tasks) + 1)])
    
    task_numbers = [num.strip() for num in ask_task_number.split(", ") if num.strip()]
    
    for task_num in sorted(task_numbers, reverse=True):
        del todo_tasks[task_num - 1]
    
    # overwrite the file with new list
    with open(filename, "w") as file:
        for task in todo_tasks:
            file.write(task + "\n")
    print(f"Task {ask_task_number} Deleted.")
    
# Functiom to update the task
def update_task(filename):
    print("Task in your TODO list")
    for index, task in enumerate(todo_tasks, start=1):
        print(f"{index}. {task}")
    
    if not todo_tasks:
        print("No tasks to update.")
        return
    
    ask_task_number = valid_input("Tell task number to update: ",
                                [str(i) for i in range(1, len(todo_tasks) + 1)])
    
    new_task = input("Enter new task: ")
    todo_tasks[int(ask_task_number) - 1] = new_task
    
    # update the task in the file as well
    with open(filename, "w") as file:
        for task in todo_tasks:
            file.write(task + "\n")
    print(f"Task {ask_task_number} updated to {new_task}")

# Function to load the tasks from a file
def load_task(filename):
    todo_tasks.clear()
    try:
        with open(filename, "r") as file:
            for line in file:
                todo_tasks.append(line.strip())
    except FileNotFoundError:
        print("No file found.")
        open(filename, "w").close()

# Function to view the tasks
def view_task(filename):
    if not todo_tasks:
        print("No tasks available in your list!!")
        return
    
    print("\nTasks in your TODO List\n")
    try:
        with open(filename, "r") as file:
            for index, task in enumerate(file, start=1):
                print(f"{index}. {task}")
    except FileNotFoundError:
        print("No file found.")
        open(filename, "w").close()

# Function to quit the app
def exit_app():
        print("Quitting....")
        time.sleep(0.2)
        quit()

# TODO Menu Function
def TODO():
    filename = get_filename()
    load_task(filename)
    while True:
        # Options for the app
        print("\nTODO List App:")
        print("""
              1. Add New Task(s)
              2. Delete Task(s)
              3. Update Task(s)
              4. View Task(s)
              5. Exit
              \n""")
        
        
        choice = valid_input("What would you like to do today? ",
                             ["1", "2", "3", "4", "5"])
        print(f"You selected: {tasks[choice]}")
        
        match choice:
            case "1":
                add_task(filename)
            
            case "2":
                del_task(filename)
            
            case "3":
                update_task(filename)
            
            case "4":
                view_task(filename)
                
            case "5":
                exit_app()


if __name__ == "__main__":
    TODO()