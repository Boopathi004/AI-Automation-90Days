import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_NAME = BASE_DIR / "employees.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary INTEGER NOT NULL
        )
    """)
    
def insert_sample_data():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO employees
        (id, name, department, salary)
        VALUES (?, ?, ?, ?)
    """, (101, "Boopathi", "AI Engineering", 50000))

    cursor.execute("""
        INSERT OR IGNORE INTO employees
        (id, name, department, salary)
        VALUES (?, ?, ?, ?)
    """, (102, "Arun", "HR", 45000))

    cursor.execute("""
        INSERT OR IGNORE INTO employees
        (id, name, department, salary)
        VALUES (?, ?, ?, ?)
    """, (103, "Kumar", "IT", 55000))

    connection.commit()
    connection.close()

