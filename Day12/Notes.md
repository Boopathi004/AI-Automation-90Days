# 📘 Day 12 – REST API Automation with Python

## 🎯 Objective

Today I learned how to communicate with external applications using **REST APIs** and Python.

The main goal was to understand how an API works and build an Employee API Management System.

---

# Session 1 – API Fundamentals

## What is an API?

API stands for **Application Programming Interface**.

An API allows two applications or systems to communicate with each other.

Example:

```text
Python Application
       ↓
     API
       ↓
Server / Database
       ↓
    JSON Data
```

---

## What is a REST API?

REST stands for **Representational State Transfer**.

REST APIs commonly use HTTP methods to perform operations on resources.

Main HTTP methods:

| Method | Purpose |
|---|---|
| GET | Read data |
| POST | Create data |
| PUT | Update data |
| DELETE | Delete data |

---

# Python Requests Library

Install:

```bash
pip install requests
```

Import:

```python
import requests
```

---

# GET Request

A GET request retrieves data.

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)
print(response.json())
```

---

# JSON Response

Most REST APIs return data in JSON format.

```python
data = response.json()

print(data)
```

JSON is commonly represented in Python as:

- Dictionary
- List
- String
- Number
- Boolean
- None

---

# Session 2 – API Client

Today I built an interactive API client.

## Get All Employees

```python
response = requests.get(url)

print(response.status_code)
print(response.json())
```

## Get Employee by ID

```python
emp_id = input("Enter Employee ID: ")

url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"

response = requests.get(url)

print(response.status_code)
print(response.json())
```

---

# POST Request

POST is used to create a new resource.

```python
data = {
    "name": "Boopathi",
    "username": "booo",
    "email": "boopathi@example.com"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
```

A successful creation commonly returns:

```text
201
```

---

# PUT Request

PUT is used to update an existing resource.

```python
data = {
    "name": "Boopathi Updated"
}

response = requests.put(url, json=data)

print(response.status_code)
print(response.json())
```

---

# DELETE Request

DELETE removes a resource.

```python
response = requests.delete(url)

print(response.status_code)
```

---

# HTTP Status Codes

Important status codes:

```text
200 → OK
201 → Created
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
500 → Internal Server Error
```

---

# Session 3 – API Error Handling

API calls can fail.

Possible problems:

- Invalid URL
- No internet connection
- Server unavailable
- Timeout
- Invalid employee ID
- HTTP error

---

## try / except

```python
try:
    response = requests.get(url)

except requests.exceptions.RequestException as error:
    print("API Error:", error)
```

---

# Timeout

Never allow an API request to wait forever.

```python
response = requests.get(url, timeout=5)
```

This gives the request a maximum waiting time.

---

# raise_for_status()

```python
response.raise_for_status()
```

This raises an exception when the server returns an HTTP error status.

Example:

```python
try:
    response = requests.get(url, timeout=5)

    response.raise_for_status()

    data = response.json()

    print(data)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
```

---

# Session 4 – Employee API Management System

Today I combined the concepts into a complete mini project.

## Menu

```text
========== EMPLOYEE API MANAGEMENT SYSTEM ==========

1. View All Employees
2. Search Employee
3. Create Employee
4. Update Employee
5. Delete Employee
6. Employee Summary
7. Exit
```

---

# Feature 1 – View Employees

Uses:

```text
GET /users
```

The application retrieves all employees and displays them.

---

# Feature 2 – Search Employee

The user enters an employee ID.

Example:

```text
Enter Employee ID: 6
```

The application retrieves the employee using the API.

---

# Feature 3 – Create Employee

The user enters:

- Name
- Username
- Email

The program sends the information using POST.

---

# Feature 4 – Update Employee

The program sends updated employee information using PUT.

---

# Feature 5 – Delete Employee

The application sends a DELETE request.

---

# Feature 6 – Employee Summary

The project calculates basic information from the API response.

Example:

```text
========== EMPLOYEE SUMMARY ==========

Total Employees: 10
First Employee: Leanne Graham
Last Employee: Clementina DuBuque
```

---

# 🔥 Important Learning

Day 10 and Day 11 focused heavily on databases.

Day 12 connects those database skills to APIs.

```text
Python
   ↓
REST API
   ↓
JSON
   ↓
External Application
```

This is important for automation engineering because real automation systems often need to:

- Read data from APIs
- Send data to APIs
- Transform JSON
- Handle failures
- Connect multiple systems
- Automate repetitive workflows

---

# 🧠 Interview Questions

## 1. What is an API?

An API is an interface that allows different software applications to communicate.

## 2. What is REST?

REST is an architectural style for building web services using standard HTTP operations.

## 3. Difference between GET and POST?

GET retrieves data.

POST creates or submits data.

## 4. What is JSON?

JSON is a lightweight data-interchange format commonly used by APIs.

## 5. What is status code 404?

It means the requested resource was not found.

## 6. What is status code 201?

It usually indicates that a resource was successfully created.

## 7. Why use timeout?

To prevent the application from waiting indefinitely for a response.

## 8. Why use raise_for_status()?

It automatically raises an exception for HTTP error responses.

## 9. What is API error handling?

It is the process of safely handling request failures, HTTP errors, timeouts, and invalid responses.

---

# 🛠️ Day 12 Mini Project

## Employee API Management System

### Features

- View employees
- Search employee
- Create employee
- Update employee
- Delete employee
- Employee summary
- API error handling

### Technologies

```text
Python
Requests
REST API
JSON
HTTP
Exception Handling
```

---

# 📝 Day 12 Summary

Today I learned:

- REST API fundamentals
- HTTP methods
- GET requests
- POST requests
- PUT requests
- DELETE requests
- JSON responses
- Status codes
- API error handling
- Request timeout
- `raise_for_status()`
- API client development
- Employee API Management System

---

# 🎯 Key Takeaway

> **A good automation engineer should not only write Python code — they should know how to connect different systems through APIs.**

Day 12 completed. 🚀

**Progress: 12 / 90 Days**
