from lib.models.user import User
from lib.models.category import Category
from lib.models.task import Task
from tabulate import tabulate
from colorama import init, Fore, Style
import re

def is_valid_email(email):
    # Email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def main():
    init(autoreset=True)  # Initialize colorama for colored output and auto-reset after each print

    while True:
        # Display the main menu
        print("Task Management System")
        print("1. Create User")
        print("2. Delete User")
        print("3. Display All Users")
        print("4. Find User by ID")
        print("5. Create Category")
        print("6. Delete Category")
        print("7. Display All Categories")
        print("8. Find Category by ID")
        print("9. Create Task")
        print("10. Delete Task")
        print("11. Display All Tasks")
        print("12. Find Task by ID")
        print("13. Update Task")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Create a new user
            name = input("Enter user name: ")
            email = input("Enter user email: ")

            if not is_valid_email(email):
                print(Fore.RED + "Invalid email address. Please try again.")
                continue

            user = User(id=None, name=name, email=email)
            user.save()
            print(Fore.GREEN + "User created successfully.")
        
        elif choice == '2':
            # Delete an existing user
            user_id = input("Enter user ID to delete: ")
            User.delete(user_id)
            print(Fore.GREEN + "User deleted successfully.")
        
        elif choice == '3':
            # Display all users
            users = User.get_all()
            print(tabulate(users, headers=["ID", "Name", "Email"]))
        
        elif choice == '4':
            # Find a user by ID
            user_id = input("Enter user ID to find: ")
            user = User.find_by_id(user_id)
            if user:
                print(tabulate([user], headers=["ID", "Name", "Email"]))
            else:
                print(Fore.RED + "User not found.")
        
        elif choice == '5':
            # Create a new category
            name = input("Enter category name: ")
            description = input("Enter category description: ")
            category = Category(id=None, name=name, description=description)
            category.save()
            print(Fore.GREEN + "Category created successfully.")
        
        elif choice == '6':
            # Delete an existing category
            category_id = input("Enter category ID to delete: ")
            Category.delete(category_id)
            print(Fore.GREEN + "Category deleted successfully.")
        
        elif choice == '7':
            # Display all categories
            categories = Category.get_all()
            print(tabulate(categories, headers=["ID", "Name", "Description"]))
        
        elif choice == '8':
            # Find a category by ID
            category_id = input("Enter category ID to find: ")
            category = Category.find_by_id(category_id)
            if category:
                print(tabulate([category], headers=["ID", "Name", "Description"]))
            else:
                print(Fore.RED + "Category not found.")
        
        elif choice == '9':
            # Create a new task
            user_id = input("Enter user ID: ")
            category_id = input("Enter category ID: ")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            status = input("Enter status: ")
            task = Task(id=None, user_id=user_id, category_id=category_id, title=title, description=description, due_date=due_date, status=status)
            task.save()
            print(Fore.GREEN + "Task created successfully.")
        
        elif choice == '10':
            # Delete an existing task
            task_id = input("Enter task ID to delete: ")
            Task.delete(task_id)
            print(Fore.GREEN + "Task deleted successfully.")
        
        elif choice == '11':
            # Display all tasks
            tasks = Task.get_all()
            print(tabulate(tasks, headers=["ID", "User ID", "Category ID", "Title", "Description", "Due Date", "Status"]))
        
        elif choice == '12':
            # Find a task by ID
            task_id = input("Enter task ID to find: ")
            task = Task.find_by_id(task_id)
            if task:
                print(tabulate([task], headers=["ID", "User ID", "Category ID", "Title", "Description", "Due Date", "Status"]))
            else:
                print(Fore.RED + "Task not found.")

        elif choice == '13':
            # Update an existing task
            task_id = input("Enter task ID to update: ")
            task = Task.find_by_id(task_id)
            if task:
                task.user_id = input(f"Enter new user ID [{task.user_id}]: ") or task.user_id
                task.category_id = input(f"Enter new category ID [{task.category_id}]: ") or task.category_id
                task.title = input(f"Enter new title [{task.title}]: ") or task.title
                task.description = input(f"Enter new description [{task.description}]: ") or task.description
                task.due_date = input(f"Enter new due date [{task.due_date}]: ") or task.due_date
                task.status = input(f"Enter new status [{task.status}]: ") or task.status
                task.save()
                print(Fore.GREEN + "Task updated successfully.")
            else:
                print(Fore.RED + "Task not found.")
        
        elif choice == '14':
            # Exit the program
            break
        
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
