from .task import Task
from .setup_db import get_connection

class User:
    def __init__(self, id, name, email):
        # Initialize the User instance with id, name, and email
        self.id = id
        self.name = name
        self.email = email

    def save(self):
        # Establish a database connection
        conn = get_connection()
        cursor = conn.cursor()
        
        # Insert the user into the 'users' table
        cursor.execute('''
            INSERT INTO users (name, email) VALUES (?, ?)
        ''', (self.name, self.email))
        
        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        # Establish a database connection
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute a query to fetch all users from the 'users' table
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        
        # Close the connection and return the fetched rows
        conn.close()
        return rows

    @classmethod
    def find_by_id(cls, user_id):
        # Establish a database connection
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute a query to fetch a user by their id
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        
        # Close the connection and return the fetched row
        conn.close()
        return row

    @classmethod
    def delete(cls, user_id):
        # Establish a database connection
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute a query to delete a user by their id
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        
        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

    def get_tasks(self):
        # Get all tasks associated with this user's id
        return Task.get_all_by_user(self.id)
