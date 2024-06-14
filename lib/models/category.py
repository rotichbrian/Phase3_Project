# category.py
from .setup_db import get_connection
from .task import Task  # Import the Task class

class Category:
    def __init__(self, id, name, description):
        # Initialize the Category instance with id, name, and description
        self.id = id
        self.name = name
        self.description = description

    def save(self):
        # Establish a database connection
        conn = get_connection()
        cursor = conn.cursor()
        
        # Insert the category into the 'categories' table
        cursor.execute('''
            INSERT INTO categories (name, description) VALUES (?, ?)
        ''', (self.name, self.description))
        
        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        # Establish a database connection
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute a query to fetch all categories from the 'categories' table
        cursor.execute('SELECT * FROM categories')
        rows = cursor.fetchall()
        
        # Close the connection and return the fetched rows
        conn.close()
        return rows

    @classmethod
    def find_by_id(cls, category_id):
        # Establish a database connection
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute a query to fetch a category by its id
        cursor.execute('SELECT * FROM categories WHERE id = ?', (category_id,))
        row = cursor.fetchone()
        
        # Close the connection and return the fetched row
        conn.close()
        return row

    @classmethod
    def delete(cls, category_id):
        # Establish a database connection
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute a query to delete a category by its id
        cursor.execute('DELETE FROM categories WHERE id = ?', (category_id,))
        
        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

    def get_tasks(self):
        # Get all tasks associated with this category's id
        return Task.get_all_by_category(self.id)
