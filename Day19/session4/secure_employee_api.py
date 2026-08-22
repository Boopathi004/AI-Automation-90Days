from datetime import datetime, timedelta, timezone

import jwt

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel


app = FastAPI(
    title="Secure Employee Management API",
    version="1.0.0"
)


# -----------------------------
# JWT CONFIGURATION
# -----------------------------

SECRET_KEY = "my-super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# -----------------------------
# DEMO USER DATABASE
# -----------------------------

users_db = {
    "admin": {
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "username": "user",
        "password": "user123",
        "role": "user"
    }
}


# -----------------------------
# EMPLOYEE DATA
# -----------------------------

employees = [
    {
        "id": 101,
        "name": "Arun",
        "department": "IT",
        "salary": 50000
    },
    {
        "id": 102,
        "name": "Kumar",
        "department": "HR",
        "salary": 45000
    }
]


# -----------------------------
# EMPLOYEE MODEL
# -----------------------------

class Employee(BaseModel):
    name: str
    department: str
    salary: int


# -----------------------------
# AUTHENTICATION
# -----------------------------

def authenticate_user(username: str, password: str):

    user = users_db.get(username)

    if not user:
        return None

    if user["password"] != password:
        return None

    return user


# -----------------------------
# CREATE JWT TOKEN
# -----------------------------

def create_access_token(data: dict):

    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({
        "exp": expire
    })

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# -----------------------------
# GET CURRENT USER
# -----------------------------

def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")
        role = payload.get("role")

        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        return {
            "username": username,
            "role": role
        }

    except jwt.InvalidTokenError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )


# -----------------------------
# ADMIN AUTHORIZATION
# -----------------------------

def require_admin(
    current_user: dict = Depends(get_current_user)
):

    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    return current_user


# -----------------------------
# HOME
# -----------------------------

@app.get("/")
def home():

    return {
        "message": "Secure Employee Management API is running"
    }


# -----------------------------
# LOGIN
# -----------------------------

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    user = authenticate_user(
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        {
            "sub": user["username"],
            "role": user["role"]
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# -----------------------------
# PROFILE
# -----------------------------

@app.get("/profile")
def profile(
    current_user: dict = Depends(get_current_user)
):

    return {
        "message": "Profile accessed",
        "username": current_user["username"],
        "role": current_user["role"]
    }


# -----------------------------
# GET ALL EMPLOYEES
# -----------------------------

@app.get("/employees")
def get_employees(
    current_user: dict = Depends(get_current_user)
):

    return {
        "logged_in_user": current_user["username"],
        "employees": employees
    }


# -----------------------------
# CREATE EMPLOYEE
# ADMIN ONLY
# -----------------------------

@app.post("/employees")
def create_employee(
    employee: Employee,
    current_user: dict = Depends(require_admin)
):

    new_id = max(
        [emp["id"] for emp in employees],
        default=100
    ) + 1

    new_employee = {
        "id": new_id,
        "name": employee.name,
        "department": employee.department,
        "salary": employee.salary
    }

    employees.append(new_employee)

    return {
        "message": "Employee created successfully",
        "created_by": current_user["username"],
        "employee": new_employee
    }


# -----------------------------
# DELETE EMPLOYEE
# ADMIN ONLY
# -----------------------------

@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    current_user: dict = Depends(require_admin)
):

    for employee in employees:

        if employee["id"] == employee_id:

            employees.remove(employee)

            return {
                "message": "Employee deleted successfully",
                "deleted_by": current_user["username"],
                "employee_id": employee_id
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )


# -----------------------------
# ADMIN DASHBOARD
# -----------------------------

@app.get("/admin/dashboard")
def admin_dashboard(
    current_user: dict = Depends(require_admin)
):

    return {
        "message": "Admin Dashboard",
        "username": current_user["username"],
        "total_employees": len(employees),
        "access": "Full Access"
    }