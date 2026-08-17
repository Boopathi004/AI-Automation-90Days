from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()


def get_connection():
    return sqlite3.connect("../session1/employees.db")


@app.get("/")
def home():
    return {
        "message": "Day 15 - FastAPI + SQLite"
    }
@app.get("/employees")
def get_employees():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    connection.close()

    return {
        "employees": employees
    }
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE id = ?",
        (employee_id,)
    )

    employee = cursor.fetchone()

    connection.close()

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "id": employee[0],
        "name": employee[1],
        "department": employee[2],
        "salary": employee[3]
    }