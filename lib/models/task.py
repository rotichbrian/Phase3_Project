# import sqlite3
from .setup_db import get_connection

class Task:
    def __init__(self, id, user_id, category_id, title, description, due_date, status):
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('''
                INSERT INTO tasks (user_id, category_id, title, description, due_date, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.user_id, self.category_id, self.title, self.description, self.due_date, self.status))
            self.id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE tasks
                SET user_id = ?, category_id = ?, title = ?, description = ?, due_date = ?, status = ?
                WHERE id = ?
            ''', (self.user_id, self.category_id, self.title, self.description, self.due_date, self.status, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        conn.close()
        return tasks

    @classmethod
    def find_by_id(cls, task_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        task = cursor.fetchone()
        conn.close()
        if task:
            return cls(*task)
        return None

    @classmethod
    def delete(cls, task_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()
