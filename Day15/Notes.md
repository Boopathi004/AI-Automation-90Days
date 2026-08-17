# Day 15 — Notes

## Topic
SQLite + SQL CRUD + FastAPI Database Integration

## Session 1 — SQLite Basics

SQLite is a lightweight file-based relational database.

```python
import sqlite3

connection = sqlite3.connect("employees.db")
cursor = connection.cursor()
```

Create a table:

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")
```

Insert data:

```python
cursor.execute("""
INSERT INTO employees (id, name, department, salary)
VALUES (?, ?, ?, ?)
""", (101, "Boopathi", "AI Engineering", 50000))
```

Save and close:

```python
connection.commit()
connection.close()
```

## Session 2 — SQL CRUD

```text
C → Create
R → Read
U → Update
D → Delete
```

SELECT:

```sql
SELECT * FROM employees;
```

INSERT:

```sql
INSERT INTO employees
(id, name, department, salary)
VALUES (?, ?, ?, ?);
```

UPDATE:

```sql
UPDATE employees
SET salary = ?
WHERE id = ?;
```

DELETE:

```sql
DELETE FROM employees
WHERE id = ?;
```

Use parameterized queries to safely pass values.

## Session 3 — FastAPI + SQLite

FastAPI exposes database operations through REST endpoints.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/employees")
def get_employees():
    ...
```

The endpoint connects to SQLite, executes SQL and returns JSON.

## Session 4 — Employee Management API

Pydantic model:

```python
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    department: str
    salary: int
```

Endpoints:

```text
GET     /employees
GET     /employees/{employee_id}
POST    /employees
PUT     /employees/{employee_id}
DELETE  /employees/{employee_id}
```

Example POST body:

```json
{
    "name": "Boopathi",
    "department": "IT",
    "salary": 50000
}
```

## Common Errors

### UNIQUE constraint failed
Cause: duplicate primary-key ID.

Solution: use a unique ID or check before inserting.

### 405 Method Not Allowed
Cause: HTTP method does not match the endpoint.

Solution: use Swagger `/docs` and select the correct method.

### 404 Not Found
Cause: route or requested employee does not exist.

### 500 Internal Server Error
Cause: an exception occurred in the application.

Solution: inspect the Uvicorn terminal traceback.

## Swagger
FastAPI provides interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Swagger can test GET, POST, PUT and DELETE endpoints.

## Key Takeaways
1. SQLite stores application data locally.
2. SQL manages relational data.
3. CRUD means Create, Read, Update and Delete.
4. FastAPI exposes backend functionality through REST APIs.
5. Pydantic validates incoming request data.
6. Swagger makes API testing easier.
7. HTTP status codes help diagnose API problems.
8. Database + API integration is an important backend foundation.

## Day 15 Challenge

Built an Employee Management API using:

```text
Python + SQLite + SQL + FastAPI + Pydantic
```

## Status

✅ Session 1 complete  
✅ Session 2 complete  
✅ Session 3 complete  
✅ Session 4 complete  

**Day 15 / 90 — COMPLETE 🚀**
