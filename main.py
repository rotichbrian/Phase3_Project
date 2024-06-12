from lib.models.user import User
from lib.models.category import Category
from lib.models.task import Task


def main():
   
    while True:
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
        print("13. Exit")

        choice = input("Enter your choice: ")
