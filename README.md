# Phase3 Project

## Date,2024/06/14

### By Brian Rotich

## Task Management System

## Description

The Task Management System is a CLI-based application that allows users to manage tasks effectively. Users can create, update, delete, and view tasks, categories, and users. This project uses SQLite for the database and follows ORM principles to interact with the database.

## How to Run

To run the Task management system locally, follow these steps:

1. Clone or download the repository to your local machine.

2. Create and activate a virtual environment using the following respectively commands pipenv install and pipenv shell.

3. Install dependencies using the pip install command(pip install tabulate
).

4. Start the React app with the following command 'npm start'.

5. The tasks information will be displayed in the web page including title, description, priority, and the due date.

## Technologies used

Python 3.8
SQLite
pipenv (for dependency management)
tabulate (for displaying tables in CLI)
colorama (provides colored ouputs)

## Functionality

The Task Management System has the following functionalities:

1. User Management:

- Create a new user: Allows creation of a new user by providing a name and a valid email address.

- Display all users: Lists all the users in the system with their ID, name, and email address.

-Find a user by name: Retrieves and displays user information based on the provided user name.

-Delete User: Enables the deletion of a user by specifying the user ID.

2. Category Mangement:

-Create Category: Allows the creation of a new category by providing a name and a description.

-Display all categories: Lists all the categories in the system with their ID, name, and description.

-Find a category by ID: Retrieves and displays category information based on the provided category ID.

-Delete Category: Enables the deletion of a category by specifying the category ID.

3. Task Management:

-Create Task: Allows the creation of a new task by specifying the user ID, category ID, title, description, due date, and status and also it ensures the task is associated with an existing user and category.

-Display all tasks: Lists all the tasks in the system with their ID, user ID, category ID, title, description, due date, and status.

-Find a task by ID: Retrieves and displays task information based on the provided task ID.

-Update Task: Enables the update of a task by specifying the task ID and the new information.

-Delete Task: Enables the deletion of a task by specifying the task ID.

### Support and Contact Details

Incase of any query, need for collaboration or issues with this code, feel free to reach me at <brian.rotich1@student.moringaschool.com>

## License

The content of this site is licensed under

MIT License

Copyright © 2023 Brian Rotich.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
