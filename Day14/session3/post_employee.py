from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Employee(BaseModel):
    name: str
    department: str
    salary: int


@app.get("/")
def home():
    return {
        "message": "Day 14 - Session 3"
    }


@app.post("/employees")
def create_employee(employee: Employee):
    return {
        "message": "Employee created successfully",
        "employee": employee
    }