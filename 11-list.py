# Empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added: " + task)

# Function to display tasks in the list
def show_tasks():
    print("Tasks in the to-do list:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

# Function to remove a task from the list
def remove_task(task_index):
    try:
        task_index = int(task_index)
        removed_task = tasks.pop(task_index - 1)
        print("Task removed: " + removed_task)
    except IndexError:
        print("Invalid task index. Task not found.")
    except ValueError:
        print("Invalid input. Please enter a valid task index.")

# Main function to interact with the user
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            task_index = input("Enter the task number to remove: ")
            remove_task(task_index)
        elif choice == "4":
            print("Exiting the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()


print("hello world")