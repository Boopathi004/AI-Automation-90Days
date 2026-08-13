# 🚀 Day 14 — FastAPI & REST API Development

> **90-Day AI Automation Engineer Journey**

Day 14 focused on building backend APIs using **FastAPI** and understanding how REST APIs work.

## 🎯 Today's Goal

- Understand FastAPI fundamentals
- Create REST API endpoints
- Work with GET and POST requests
- Use path and query parameters
- Validate request data using Pydantic
- Build PUT and DELETE APIs
- Handle API errors using HTTPException
- Build an Employee CRUD API
- Create department-based employee search
- Test APIs using Swagger UI

## 📚 Sessions Completed

### ✅ Session 1 — FastAPI Fundamentals

Learned FastAPI installation, creating a FastAPI application, GET endpoints, Uvicorn, automatic reload, and browser testing.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my Day 14 FastAPI application"}
```

### ✅ Session 2 — GET APIs & Parameters

Learned GET endpoints, path parameters, query parameters, JSON responses, and product API endpoints.

```python
@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
        "product_id": product_id,
        "product_name": "Laptop",
        "price": 55000
    }
```

### ✅ Session 3 — POST API & Pydantic

Learned POST requests, request bodies, Pydantic `BaseModel`, data validation, and structured API input.

```python
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    department: str
    salary: int
```

### ✅ Session 4 — Employee CRUD API

Built an Employee API supporting GET, POST, PUT, DELETE, department-based search, and error handling with `HTTPException`.

```text
GET /employees
GET /employees/{employee_id}
POST /employees
PUT /employees/{employee_id}
DELETE /employees/{employee_id}
GET /employees/department/{department_name}
```

## 🧪 Challenge Completed

### Department-Based Employee Search

Created:

```text
GET /employees/department/{department_name}
```

The endpoint performs a case-insensitive department search.

Example:

```text
/employees/department/it
```

Invalid departments return `404 Not Found` with an appropriate error message.

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- REST APIs
- HTTPException
- Swagger UI
- VS Code
- Git/GitHub

## 🧠 Key Concepts Learned

### REST API

```text
GET
POST
PUT
DELETE
```

### Path Parameter

```text
/products/{product_id}
```

### Query Parameter

```text
/search?name=Boopathi
```

### HTTPException

```python
raise HTTPException(
    status_code=404,
    detail="Employee not found"
)
```

## 💼 Real-World Relevance

FastAPI is an important skill for AI Product Engineering because AI functionality often needs to be exposed through APIs.

```text
Frontend
   ↓
FastAPI Backend
   ↓
AI / LLM Layer
   ↓
RAG / Vector Database
   ↓
Response
```

This foundation will later support LLM APIs, RAG applications, AI agents, automation workflows, and AI-powered backend services.

## 📈 Day 14 Achievement

**14 / 90 Days Completed**

```text
████████████████░░░░░░░░░░░░░░░░░░░░ 15.6%
```

### Status

✅ FastAPI fundamentals  
✅ REST API development  
✅ GET APIs  
✅ POST APIs  
✅ Pydantic validation  
✅ PUT APIs  
✅ DELETE APIs  
✅ Error handling  
✅ CRUD API  
✅ Department search  

## 🔥 Day 14 Takeaway

> **"AI applications need strong backend foundations. Today I started building that foundation with FastAPI."**

### 🚀 Next

**Day 15 — Backend + Database Integration**
