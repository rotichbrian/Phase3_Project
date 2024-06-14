import sqlite3

def get_connection():
    # Establish and return a connection to the 'task_management.db' SQLite database
    return sqlite3.connect('task_management.db')

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
    ''')

    # Create categories table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT
    )
    ''')

    # Create tasks table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        category_id INTEGER,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        status TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Create the tables when the script is run directly
    create_tables()
