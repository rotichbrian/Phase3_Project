# Import the get_connection function from the setup_db module
from .setup_db import get_connection

class Task:
    def __init__(self, id, user_id, category_id, title, description, due_date, status):
        """
        Initialize a Task object with the given attributes.
        """
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def save(self):
        """
        Save the task to the database. If the task has an ID, it updates the existing record.
        Otherwise, it inserts a new record.
        """
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            # Insert a new task
            cursor.execute('''
                INSERT INTO tasks (user_id, category_id, title, description, due_date, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.user_id, self.category_id, self.title, self.description, self.due_date, self.status))
            # Retrieve the ID of the newly inserted task
            self.id = cursor.lastrowid
        else:
            # Update an existing task
            cursor.execute('''
                UPDATE tasks
                SET user_id = ?, category_id = ?, title = ?, description = ?, due_date = ?, status = ?
                WHERE id = ?
            ''', (self.user_id, self.category_id, self.title, self.description, self.due_date, self.status, self.id))
        conn.commit()  # Commit the transaction
        conn.close()   # Close the connection

    @classmethod
    def get_all(cls):
        """
        Retrieve all tasks from the database.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()  # Fetch all tasks
        conn.close()  # Close the connection
        return tasks

    @classmethod
    def find_by_id(cls, task_id):
        """
        Find a task by its ID. Returns a Task object if found, otherwise returns None.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        task = cursor.fetchone()  # Fetch the task
        conn.close()  # Close the connection
        if task:
            return cls(*task)  # Return a Task object
        return None

    @classmethod
    def delete(cls, task_id):
        """
        Delete a task by its ID. Returns True if the task was deleted, False otherwise.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()  # Commit the transaction
        conn.close()   # Close the connection
        return cursor.rowcount > 0  # Return True if a row was deleted, False otherwise
