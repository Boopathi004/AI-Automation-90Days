# 📝 Day 14 Notes — FastAPI & REST APIs

## 🎯 Topic

FastAPI & REST API Development

## 1. What is FastAPI?

FastAPI is a modern Python framework used to build APIs and backend applications.

Key benefits:
- Fast API development
- Automatic API documentation
- Request validation
- Type hints
- Easy Python integration

## 2. Installing FastAPI

```bash
python -m pip install fastapi uvicorn
```

Run an application:

```bash
python -m uvicorn filename:app --reload
```

Example:

```bash
python -m uvicorn fastapi_basic:app --reload
```

## 3. Basic FastAPI Application

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI application"}
```

Open:

```text
http://127.0.0.1:8000
```

## 4. Swagger UI

FastAPI automatically provides interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Swagger allows us to view, test, and inspect API endpoints.

## 5. GET Request

```python
@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
        "product_id": product_id,
        "product_name": "Laptop",
        "price": 55000
    }
```

Request:

```text
GET /products/103
```

## 6. Path Parameters

A path parameter is part of the URL.

```text
/products/103
```

Here `103` is the `product_id`.

## 7. Query Parameters

Example:

```text
/search?name=Boopathi
```

## 8. POST Request

POST is commonly used to create new data.

```python
@app.post("/employees")
def create_employee(employee: Employee):
    return {
        "message": "Employee created successfully",
        "employee": employee
    }
```

## 9. Pydantic BaseModel

```python
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    department: str
    salary: int
```

Example JSON:

```json
{
    "name": "Boopathi",
    "department": "IT",
    "salary": 50000
}
```

## 10. PUT Request

PUT is used to update existing data.

```python
@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    updated_employee: Employee
):
    ...
```

## 11. DELETE Request

```python
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    ...
```

## 12. HTTPException

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="Employee not found"
)
```

Common status codes:

```text
200 → Success
201 → Created
400 → Bad Request
404 → Not Found
500 → Server Error
```

## 13. CRUD

CRUD means:

```text
C → Create
R → Read
U → Update
D → Delete
```

API mapping:

```text
POST   → Create
GET    → Read
PUT    → Update
DELETE → Delete
```

## 14. Employee API

```text
GET /employees
GET /employees/{employee_id}
POST /employees
PUT /employees/{employee_id}
DELETE /employees/{employee_id}
```

## 15. Department Search

Created:

```text
GET /employees/department/{department_name}
```

Example:

```text
/employees/department/it
```

Case-insensitive comparison:

```python
employee["department"].lower() == department_name.lower()
```

## 16. Filtering Employees

```python
department_employees = [
    employee
    for employee in employees
    if employee["department"].lower()
    == department_name.lower()
]
```

## 17. Handling Empty Results

```python
if not department_employees:
    raise HTTPException(
        status_code=404,
        detail="No employees found in the specified department"
    )
```

## 18. Uvicorn

Uvicorn is the ASGI server used to run FastAPI applications.

```bash
python -m uvicorn employee_crud:app --reload
```

## 19. Important Learning

```text
Frontend
    ↓
REST API
    ↓
Backend
    ↓
Database
```

Future AI architecture:

```text
Frontend
    ↓
FastAPI
    ↓
LLM / AI Agent
    ↓
RAG / Vector Database
    ↓
Response
```

## 20. Day 14 Debugging Experience

During today's learning I faced practical development issues:

- FastAPI import configuration
- Uvicorn command issues
- Module import errors
- API route testing
- HTTP 404 responses
- Understanding empty search results
- Testing endpoints through Swagger

This reinforced that backend development requires both coding and debugging.

## 21. Interview Questions

**Q1. What is FastAPI?**  
A modern Python framework for building APIs and backend applications.

**Q2. What is Pydantic?**  
A library used for data validation and structured request models.

**Q3. What is REST API?**  
An architectural approach for communication between applications using HTTP methods.

**Q4. What is CRUD?**  
Create, Read, Update, Delete.

**Q5. Difference between GET and POST?**  
GET is generally used to retrieve data; POST is generally used to create or submit data.

**Q6. What is a path parameter?**  
A value embedded directly in the URL path, such as `/employees/101`.

**Q7. What is a query parameter?**  
A parameter passed after `?`, such as `/search?name=Boopathi`.

**Q8. Why use HTTPException?**  
To return appropriate HTTP error responses.

**Q9. What is Uvicorn?**  
An ASGI server used to run FastAPI applications.

**Q10. Why is FastAPI useful for AI applications?**  
It can expose AI functionality through REST APIs so frontend applications, automation systems, and other services can communicate with AI backends.

## 🏆 Day 14 Completed

### Skills Added

- FastAPI
- REST APIs
- GET
- POST
- PUT
- DELETE
- Pydantic
- Uvicorn
- Swagger UI
- HTTPException
- CRUD
- API testing
- Parameter handling

## 🔥 Key Takeaway

> Build the API first. Then connect the intelligence.

## 🚀 Next Learning Direction

```text
FastAPI
   ↓
Database
   ↓
AI / LLM
   ↓
RAG
   ↓
AI Agents
   ↓
Production AI Application
```
