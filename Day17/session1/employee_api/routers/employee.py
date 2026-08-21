from fastapi import APIRouter
from schemas.employee import (EmployeeCreate, EmployeeResponse, EmployeeUpdate)
from fastapi import APIRouter, HTTPException
from services.employee_service import (
    get_all_employees,
    create_employee,
    get_employee_by_id,
    update_employee,
    delete_employee
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.get("/")
def get_employees():
    return {
        "employees": get_all_employees()
    }
@router.post("/", response_model=EmployeeResponse)
def add_employee(employee: EmployeeCreate):

    return create_employee(
        employee.name,
        employee.department,
        employee.salary
    )

@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int):

    employee = get_employee_by_id(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee

@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee_route(
    employee_id: int,
    employee: EmployeeUpdate
):

    updated_employee = update_employee(
        employee_id,
        employee.name,
        employee.department,
        employee.salary
    )

    if updated_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated_employee
@router.delete("/{employee_id}")
def delete_employee_route(employee_id: int):

    deleted = delete_employee(employee_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }