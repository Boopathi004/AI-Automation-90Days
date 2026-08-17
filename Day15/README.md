# Day 15 — SQLite Database + FastAPI CRUD

## 🎯 Objective
Day 15 focused on connecting Python applications and FastAPI services with SQLite and building a database-backed Employee CRUD API.

## 📚 Sessions Completed
- ✅ Session 1 — SQLite Database & Table Creation
- ✅ Session 2 — SQL CRUD Operations
- ✅ Session 3 — FastAPI + SQLite Integration
- ✅ Session 4 — Employee Management REST API

## 🧠 Skills Learned
- Python `sqlite3`
- SQLite database and table creation
- SQL `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- Parameterized SQL queries
- Database connections, cursors, `commit()` and `close()`
- FastAPI REST API development
- Pydantic `BaseModel` and request validation
- HTTP methods: GET, POST, PUT, DELETE
- Path parameters
- Swagger/OpenAPI testing
- API error handling
- FastAPI + SQLite integration

## 🛠️ Session Details

### Session 1 — SQLite Basics
Created an SQLite database and an `employees` table.

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
);
```

Inserted employee records and retrieved them with SQL.

### Session 2 — SQL CRUD
Practiced the four core database operations:

```text
CREATE / INSERT
READ / SELECT
UPDATE
DELETE
```

Also debugged the duplicate primary-key error:

```text
sqlite3.IntegrityError: UNIQUE constraint failed: employees.id
```

The issue was resolved by using unique employee IDs and avoiding duplicate inserts.

### Session 3 — FastAPI + SQLite
Connected FastAPI to the SQLite database and created an endpoint to retrieve employee records.

```text
GET /employees
```

### Session 4 — Employee Management API
Built an Employee Management API using FastAPI, Pydantic and SQLite.

```text
GET     /employees
GET     /employees/{employee_id}
POST    /employees
PUT     /employees/{employee_id}
DELETE  /employees/{employee_id}
```

Tested the API with:

```text
http://127.0.0.1:8000/docs
```

## 🔍 Debugging Lessons

### 405 Method Not Allowed
The route exists, but the HTTP method is wrong. For example, opening a POST/PUT endpoint in a browser sends GET.

### 404 Not Found
The requested route or employee record does not exist.

### 500 Internal Server Error
An unhandled application exception occurred. The Uvicorn terminal traceback should be checked first.

## 🏗️ Architecture

```text
Client / Swagger
       ↓
    FastAPI
       ↓
 Pydantic Validation
       ↓
 SQLite Database
       ↓
 Employee Records
```

## 🚀 Why This Matters for AI Automation
Database-backed APIs are a foundation for AI applications. The same architecture can later support AI agents, RAG systems, vector databases and business workflows.

## 📈 90-Day Challenge Progress
**Day 15 / 90 completed — 16.7%**

**AI Automation Engineer — 90 Day Challenge**  
Learning by building. 🚀
