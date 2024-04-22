# First the app is going to greet the user:

user_name = input ("Hello! What's is your name?: ")
print (f"Welcome to To Do List App, {user_name}!")
       
# Inside the function we are suggesting to user to enter a new task using the input() function.

def add_task(todo_list):
    title = input("Enter task title, please: ")
    todo_list.append({"title": title, "status": "Incomplete"})
    print (f"Task '{title}' added successfully!")

# THe function represents the list of tasks in the todo list. 
# Then the function checking if the task exists in the todo list, if not the user will be informed.
# If the list is not empty the user will be informed that the function will display the list of tasks.  
# It then iterates over each task in the todo_list using a for loop with enumerate(todo_list, 1). It starts the counter from 1. 
# So, "i" will be the index of the task in the list plus 1.

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks found.")
        return
    print("Tasks:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task['title']} - {task['status']}")


# First this function calls the @view_list" function to display the current todo list along with their titles and statuses.
# Then it prompts the user to input the task number they want to mark as complete using the input() function.
# THen converting the input task_num into an integer using int(task_num). 
# If the entered task number is valid, it updates the status of the corresponding task in the todo_list to "Complete" by accessing the task using todo_list[task_num - 1]["status"] and assigning it the value "Complete".
# If the user enters a non-integer value, a ValueError exception is raised, and the program prints "Invalid input. Please enter a number."

def mark_complete(todo_list):
    view_tasks(todo_list)
    task_num = input("Enter the task number to mark as complete: ")
    try:
        task_num = int(task_num)
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["status"] = "Complete"
            print(f"Task '{todo_list[task_num - 1]['title']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.") 

# To delete the task, again, first the function calls "view_list" the function that displays the todo list
# then the function suggests the user to enter the task numberthe user wants to delete using the input() function
# Inside the try-exce[t x]
# Inside a try-except block, the function trшуы to convert the input task_num into an integer using int(task_num). 
# If the input cannot be converted to an integer (e.g., if the user enters a non-numeric value), a ValueError exception is raised and caught by the except block.
# This function allows the user to delete a task from the to-do list by providing the task number, (handling both valid and invalid inputs gracefully.)

def delete_task(todo_list):
    view_tasks(todo_list)
    task_num = input("Enter the task number to delete: ")
    try:
        task_num = int(task_num)
        if 1 <= task_num <= len(todo_list):
            del todo_list[task_num - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def display_menu():
    print("""
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Exit 
    """)

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            mark_complete(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()