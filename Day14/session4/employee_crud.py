from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#create a model for employee

class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: int


employees = [
    {
        "id": 101,
        "name": "Boopathi",
        "department": "IT",
        "salary": 50000
    },
    {
        "id": 102,
        "name": "Arun",
        "department": "HR",
        "salary": 45000
    },
    {
        "id": 103,
        "name": "Kumar",
        "department": "IT",
        "salary": 55000
    }
]

# get all employees
@app.get("/employees")
def get_employees():
    return employees

# get employee by id

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

#update employee by id

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):

    for index, employee in enumerate(employees):

        if employee["id"] == employee_id:

            employees[index] = updated_employee.model_dump()

            return {
                "message": "Employee updated successfully",
                "employee": employees[index]
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

#delete employee by id

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    for index, employee in enumerate(employees):

        if employee["id"] == employee_id:

            deleted_employee = employees.pop(index)

            return {
                "message": "Employee deleted successfully",
                "employee": deleted_employee
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )
#department based employee search
@app.get("/employees/department/{department_name}")
def department (department_name: str):
    department_employees = [employee for employee in employees if employee["department"].lower() == 
                            department_name.lower()]

    if not department_employees:
        raise HTTPException(
            status_code=404,
            detail="No employees found in the specified department"
        )

    return {
        "department": department_name,
        "employees": department_employees
    }