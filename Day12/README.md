# 🚀 Day 12 – REST API Automation with Python

## 🎯 Day 12 Goal

Learn how to work with **REST APIs using Python** and build a practical Employee API Management System.

Today I progressed from local data/database automation into **API-based automation**, an important step toward AI Automation Engineering.

---

## 📚 What I Learned

### Session 1 – API Fundamentals

- What an API is
- REST API basics
- HTTP requests
- GET request
- JSON data
- Reading API responses
- Writing JSON data
- Working with Python `requests`

### Session 2 – API Client

Built an interactive API client using Python.

Practiced:

- GET all employees
- GET employee by ID
- POST/create employee
- Sending JSON payloads
- Reading status codes
- Processing JSON responses
- Building menu-driven API programs

### Session 3 – API Error Handling

Learned how to make API automation more reliable.

Practiced:

- `try/except`
- `requests.get()`
- Request timeouts
- `response.raise_for_status()`
- HTTP error handling
- Handling invalid employee IDs
- Handling connection/request failures
- Creating reusable API functions

### Session 4 – Employee API Management System

Built a complete **Employee API Management System**.

Features:

1. View All Employees
2. Search Employee
3. Create Employee
4. Update Employee
5. Delete Employee
6. Employee Summary
7. Exit

The Employee Summary includes:

- Total employees
- First employee
- Last employee

---

## 💻 Technologies Used

- Python
- REST API
- HTTP
- JSON
- `requests` library
- Exception handling
- API status codes
- VS Code
- Git & GitHub

---

## 🧩 Main Project

### Employee API Management System

A menu-driven Python application that communicates with a REST API.

### Features

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

## 🔑 Important Concepts

### GET

Used to retrieve data from an API.

```python
response = requests.get(url)
```

### POST

Used to create new data.

```python
response = requests.post(url, json=data)
```

### PUT

Used to update existing data.

```python
response = requests.put(url, json=data)
```

### DELETE

Used to delete data.

```python
response = requests.delete(url)
```

### Status Code

```python
print(response.status_code)
```

Common codes:

- `200` – Success
- `201` – Created
- `400` – Bad Request
- `404` – Not Found
- `500` – Server Error

### Error Handling

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException as error:
    print("API Error:", error)
```

---

## 🛠️ Projects Built So Far

By the end of Day 12, the journey includes:

- File Automation Projects
- Excel Automation Projects
- CSV Automation Projects
- JSON Automation Projects
- SQLite Database Projects
- Employee CRUD System
- Employee Dashboard
- Employee Reports
- Company Management System
- REST API Client
- API Error Handler
- Employee API Management System

---

## 🧠 Skills Developed

### Python

- Functions
- OOP
- Exception Handling
- Lambda
- map/filter/reduce
- Modules
- File handling
- JSON
- Logging

### Databases

- SQLite
- SQL
- CRUD
- Aggregate functions
- GROUP BY
- ORDER BY
- Database relationships
- Data integrity

### APIs

- REST APIs
- HTTP methods
- JSON responses
- Status codes
- GET
- POST
- PUT
- DELETE
- API error handling
- Request timeout handling

---

## 📈 Challenge Progress

```text
████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

Completed: 12 / 90 Days

Progress: 13.3%
```

---

## 🎯 Current Focus

- Advanced Python
- REST API Automation
- Database Automation
- Data Integration
- Error Handling
- AI Automation Foundations

---

## 🚀 Next Learning Direction

The next stages of the journey will move toward:

- Advanced API integrations
- Web Scraping
- Email Automation
- OpenAI API
- Prompt Engineering
- LLM Applications
- LangChain
- RAG
- AI Agents
- n8n
- Make.com
- Production AI Automation Projects

---

## 💡 Day 12 Takeaway

> **APIs are the bridge between applications. Learning to consume and automate APIs is a core skill for building real-world automation systems.**

---

## 🤝 Connect

💻 GitHub: https://github.com/Boopathi004

💼 LinkedIn: https://www.linkedin.com/in/boopathiraja

🌐 Portfolio: https://boopathi-builder-chi.vercel.app/

---

# 🎯 Goal

**90 Days → Real Projects → Strong Portfolio → AI Automation Engineer**

> One day. One concept. One project. Every day closer. 🚀
