# Day 16 — Notes

## Topic
Professional FastAPI Project Structure + Service Layer + SQLite

## 1. APIRouter
`APIRouter` separates related FastAPI endpoints into different files.

```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)
```

Connect it with:
```python
app.include_router(employee_router)
```

## 2. Project Structure
```text
employee_api/
├── main.py
├── database/
├── models/
├── routers/
├── schemas/
└── services/
```

## 3. Separation of Concerns
```text
Router
  ↓
Service
  ↓
Database
```

The router handles HTTP requests, the service handles application logic, and the database layer handles database access.

## 4. Database Connection
Reusable SQLite connection:
```python
import sqlite3

def get_connection():
    connection = sqlite3.connect("employees.db")
    connection.row_factory = sqlite3.Row
    return connection
```

## 5. Employee Service
Example:
```python
def get_all_employees():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    connection.close()
    return [dict(employee) for employee in employees]
```

The router calls the service instead of containing SQL directly.

## 6. Department Service
Created a department service using:
```sql
SELECT DISTINCT department FROM employees;
```

## 7. API Architecture
```text
Client
  ↓
FastAPI
  ↓
Router
  ↓
Service
  ↓
Database Connection
  ↓
SQLite
```

## 8. Debugging — no such table
Error:
```text
sqlite3.OperationalError: no such table: employees
```

Cause: the application connected to a SQLite database that did not contain the expected table.

Lesson: SQLite database paths and table setup must be checked carefully.

## 9. API Testing
Swagger:
```text
http://127.0.0.1:8000/docs
```

## 10. Key Takeaways
1. Avoid keeping every endpoint in `main.py`.
2. Use `APIRouter` to organize endpoints.
3. Use service functions to keep routes clean.
4. Reuse database connection logic.
5. Check the database file and schema when SQLite errors occur.
6. Swagger is useful for testing FastAPI endpoints.
7. Separation of concerns makes applications easier to maintain.

## 🏆 Day 16 Challenge
Completed a modular Employee API using:
```text
Python + FastAPI + APIRouter + SQLite + SQL + Service Layer + Swagger
```

- ✅ Session 1
- ✅ Session 2
- ✅ Session 3
- ✅ Session 4

**Day 16 / 90 — COMPLETE 🚀**
