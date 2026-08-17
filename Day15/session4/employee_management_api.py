import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


def get_connection():
    return sqlite3.connect("../session1/employees.db")

class Employee(BaseModel):
    name: str
    department: str
    salary: int
@app.get("/all employees")
def get_all_employees():

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    connection.close()
    return {"employees": employees}
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
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
@app.post("/employees")
def create_employee(employee: Employee):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        (employee.name, employee.department, employee.salary)
    )
    connection.commit()
    connection.close()

    return {
        "message": "Employee created successfully",
        "employee": employee
    }
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    connection.commit()
    connection.close()

    return {
        "message": "Employee deleted successfully"
    }