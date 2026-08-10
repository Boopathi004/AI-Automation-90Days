# Day 11 -- Advanced SQLite & Relational Database Programming

## Objective

Today I moved from basic SQLite operations into advanced database
programming with Python.

### Topics

-   Advanced SQL Queries
-   Database Constraints
-   Data Integrity
-   Primary Keys and Foreign Keys
-   Relationships and JOINs
-   Aggregate Functions
-   GROUP BY
-   SQL Reports
-   Exception Handling
-   Company Management System

------------------------------------------------------------------------

# Session 1 -- Advanced SQL Queries

## WHERE

Filters records based on a condition.

``` sql
SELECT * FROM employees WHERE salary > 50000;
```

## LIKE

Used for pattern-based searching.

``` sql
SELECT * FROM employees WHERE name LIKE ?;
```

Python example:

``` python
name = input("Enter name to search: ")

cursor.execute(
    "SELECT * FROM employees WHERE name LIKE ?",
    ('%' + name + '%',)
)

employees = cursor.fetchall()
```

Pattern examples:

``` text
%boo%   → contains "boo"
boo%    → starts with "boo"
%boo    → ends with "boo"
```

## IN

``` sql
SELECT * FROM employees
WHERE department IN ('IT', 'HR');
```

## BETWEEN

``` sql
SELECT * FROM employees
WHERE salary BETWEEN 40000 AND 80000;
```

## ORDER BY

``` sql
SELECT * FROM employees
ORDER BY salary DESC;
```

-   ASC → lowest to highest
-   DESC → highest to lowest

## LIMIT

``` sql
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 1;
```

Useful for finding the highest-paid employee.

## Parameterized Queries

Prefer:

``` python
cursor.execute(
    "SELECT * FROM employees WHERE name LIKE ?",
    ('%' + name + '%',)
)
```

instead of directly concatenating user input. Parameterized queries
safely separate SQL from data and help reduce SQL injection risks.

### Session 1 Mini Project

Built an Advanced Employee Search application with:

-   Search employee by name
-   Search employees by salary
-   Count total employees
-   Handle invalid employee IDs
-   Filter and sort employee records

------------------------------------------------------------------------

# Session 2 -- Database Constraints & Data Integrity

Database constraints protect the quality and validity of data.

## PRIMARY KEY

Uniquely identifies each record.

``` sql
id INTEGER PRIMARY KEY AUTOINCREMENT
```

## NOT NULL

Prevents empty values.

``` sql
name TEXT NOT NULL
```

## UNIQUE

Prevents duplicate values.

``` sql
email TEXT UNIQUE
```

## CHECK

Enforces a condition.

``` sql
salary REAL CHECK(salary > 0)
```

## DEFAULT

Provides a value automatically.

``` sql
status TEXT DEFAULT 'Active'
```

## FOREIGN KEY

Creates a relationship between tables.

``` sql
department_id INTEGER,
FOREIGN KEY(department_id)
REFERENCES departments(id)
```

### Data Integrity

Data integrity means keeping information accurate, consistent, valid,
and reliable.

Typical flow:

``` text
User Input
    ↓
Validation
    ↓
Constraints
    ↓
Database
```

### IntegrityError

``` python
try:
    cursor.execute(
        "INSERT INTO employees(name, email) VALUES (?, ?)",
        (name, email)
    )
    connection.commit()

except sqlite3.IntegrityError as error:
    print(f"Database error: {error}")
```

------------------------------------------------------------------------

# Session 3 -- Relationships, JOINs & SQL Reports

## One-to-Many Relationship

One department can have many employees.

``` text
Department
    |
    +-- Employee 1
    +-- Employee 2
    +-- Employee 3
```

## INNER JOIN

Returns matching records from both tables.

``` sql
SELECT
    e.name,
    d.name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id;
```

## LEFT JOIN

Returns all records from the left table and matching records from the
right table.

``` sql
SELECT
    d.name,
    e.name
FROM departments d
LEFT JOIN employees e
ON d.id = e.department_id;
```

## Aggregate Functions

### COUNT

``` sql
SELECT COUNT(*) FROM employees;
```

### SUM

``` sql
SELECT SUM(salary) FROM employees;
```

### AVG

``` sql
SELECT AVG(salary) FROM employees;
```

### MIN

``` sql
SELECT MIN(salary) FROM employees;
```

### MAX

``` sql
SELECT MAX(salary) FROM employees;
```

## GROUP BY

``` sql
SELECT department_id, COUNT(*)
FROM employees
GROUP BY department_id;
```

## Department-Wise Analytics

``` sql
SELECT
    d.name,
    COUNT(e.id),
    AVG(e.salary),
    SUM(e.salary)
FROM departments d
LEFT JOIN employees e
ON d.id = e.department_id
GROUP BY d.id, d.name;
```

Example report:

``` text
Finance   | Employees: 2 | Average Salary: 62500.00 | Total Salary: 125000.00
HR        | Employees: 1 | Average Salary: 43000.00 | Total Salary: 43000.00
IT        | Employees: 2 | Average Salary: 50000.00 | Total Salary: 100000.00
Marketing | Employees: 0 | Average Salary: 0.00     | Total Salary: 0.00
```

### Employee Dashboard

Built a dashboard with:

1.  View All Employees
2.  Highest Salary Employee
3.  Lowest Salary Employee
4.  Average Salary
5.  Total Salary
6.  Total Employees
7.  Employees by Department
8.  Sort by Salary
9.  Exit

------------------------------------------------------------------------

# Session 4 -- Company Management System

Built a complete database-driven Company Management System using Python
and SQLite.

## Main Features

1.  Add Employee
2.  View Employees
3.  Search Employee
4.  Update Employee
5.  Delete Employee
6.  Department Report
7.  Highest Salary
8.  Average Salary
9.  Total Employees
10. Exit

## Add Employee

Accepts employee information such as:

``` text
Employee Name
Department
Salary
```

and stores it in SQLite.

## View Employees

Displays employee records from the database.

## Search Employee

``` sql
SELECT * FROM employees
WHERE name LIKE ?;
```

## Update Employee

Updates employee information such as name, department, or salary.

## Delete Employee

A safe delete operation should:

1.  Ask for the employee ID
2.  Check whether the employee exists
3.  Ask for confirmation
4.  Delete the record
5.  Commit the transaction
6.  Display the result

## Department Report

Generates:

-   Department
-   Employee Count
-   Average Salary
-   Total Salary

## Highest Salary

``` sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 1;
```

## Average Salary

``` sql
SELECT AVG(salary)
FROM employees;
```

## Total Employees

``` sql
SELECT COUNT(*)
FROM employees;
```

------------------------------------------------------------------------

# Exception Handling

Database applications must handle unexpected situations safely.

Common problems:

-   Invalid employee ID
-   Invalid salary
-   Empty input
-   Duplicate email
-   Invalid department
-   Missing records
-   Constraint violations
-   Incorrect data types

Example:

``` python
try:
    salary = float(input("Enter salary: "))

except ValueError:
    print("Invalid salary. Please enter a number.")

except sqlite3.IntegrityError as error:
    print(f"Database error: {error}")

finally:
    connection.close()
```

## Commit

Save INSERT, UPDATE, and DELETE changes:

``` python
connection.commit()
```

## Rollback

Undo uncommitted changes after a failed transaction:

``` python
try:
    cursor.execute(...)
    connection.commit()

except Exception:
    connection.rollback()
```

## Closing the Connection

``` python
connection.close()
```

Using `finally` helps ensure the connection is closed.

------------------------------------------------------------------------

# SQL Injection

Avoid constructing SQL by concatenating user input.

### Avoid

``` python
query = "SELECT * FROM employees WHERE name = '" + name + "'"
```

### Prefer

``` python
cursor.execute(
    "SELECT * FROM employees WHERE name = ?",
    (name,)
)
```

Parameterized queries are safer.

------------------------------------------------------------------------

# Important SQLite Python Pattern

``` python
import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

try:
    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    for employee in employees:
        print(employee)

except sqlite3.Error as error:
    print(f"Database error: {error}")

finally:
    connection.close()
```

------------------------------------------------------------------------

# Key Learnings

## SQL

-   SELECT
-   WHERE
-   LIKE
-   IN
-   BETWEEN
-   ORDER BY
-   LIMIT
-   GROUP BY
-   JOIN

## Aggregate Functions

-   COUNT()
-   SUM()
-   AVG()
-   MIN()
-   MAX()

## Database Design

-   Primary Key
-   Foreign Key
-   One-to-Many Relationship
-   Constraints
-   Data Integrity

## Python + SQLite

-   sqlite3
-   connect()
-   cursor()
-   execute()
-   fetchone()
-   fetchall()
-   commit()
-   rollback()
-   close()

## Error Handling

-   ValueError
-   sqlite3.IntegrityError
-   sqlite3.Error
-   try
-   except
-   finally

------------------------------------------------------------------------

# Projects Completed

## Project 1 -- Advanced Employee Search

-   Search by Name
-   Salary Filtering
-   Employee Count
-   Invalid ID Handling

## Project 2 -- Employee Dashboard

-   Highest Salary
-   Lowest Salary
-   Average Salary
-   Total Salary
-   Employee Count
-   Department Analysis
-   Salary Sorting

## Project 3 -- Company Management System

-   Add Employee
-   View Employees
-   Search Employee
-   Update Employee
-   Delete Employee
-   Department Reports
-   Salary Analytics

------------------------------------------------------------------------

# Interview Questions

## What is SQLite?

SQLite is a lightweight, serverless, file-based relational database
engine.

## What is a Primary Key?

A Primary Key uniquely identifies each row in a table.

## What is a Foreign Key?

A Foreign Key creates a relationship between records in different
tables.

## INNER JOIN vs LEFT JOIN?

INNER JOIN returns matching records from both tables. LEFT JOIN returns
every record from the left table plus matching records from the right
table.

## What is GROUP BY?

GROUP BY groups rows based on one or more columns so aggregate functions
can be applied.

## Why use constraints?

Constraints maintain data accuracy, consistency, and integrity.

## Why use parameterized queries?

They safely handle user input and help reduce SQL injection risks.

## Why use commit()?

It saves INSERT, UPDATE, and DELETE changes to the database.

## Why use rollback()?

It reverses uncommitted changes when a database operation fails.

------------------------------------------------------------------------

# Practical Skills Completed

By the end of Day 11 I can:

-   Create SQLite databases
-   Create tables
-   Insert records
-   Read records
-   Update records
-   Delete records
-   Search records
-   Filter records
-   Sort records
-   Use aggregate functions
-   Group database records
-   Join related tables
-   Apply constraints
-   Handle database errors
-   Generate business reports
-   Build database-driven Python applications

------------------------------------------------------------------------

# Biggest Learning of Day 11

A real-world application is not only about writing code.

A reliable application needs:

``` text
Clean Code
   +
Input Validation
   +
Database Constraints
   +
Relationships
   +
Business Logic
   +
Reports
   +
Error Handling
   +
Security
```

This is an important step from basic Python programming toward backend
and automation engineering.

------------------------------------------------------------------------

# Career Connection

Today's database skills are useful for:

-   Python Automation Engineer
-   AI Automation Engineer
-   Python Developer
-   Backend Developer
-   API Developer
-   Data Automation roles

These skills will later connect with:

``` text
Python
   ↓
SQLite / SQL
   ↓
REST APIs
   ↓
FastAPI
   ↓
OpenAI APIs
   ↓
LLM Applications
   ↓
RAG
   ↓
AI Agents
   ↓
n8n / Make.com
```

------------------------------------------------------------------------

# Day 11 Progress

``` text
Session 1 → ✅ Completed
Session 2 → ✅ Completed
Session 3 → ✅ Completed
Session 4 → ✅ Completed
```

``` text
Day 11 / 90
Completed: 11 Days
Remaining: 79 Days
Progress: 12.2%
```

``` text
███████████░░░░░░░░░░░░░░░░░
```

------------------------------------------------------------------------

# Next Stage -- Day 12

The next stage will move toward REST APIs and backend development.

Planned topics:

-   HTTP
-   GET
-   POST
-   PUT
-   PATCH
-   DELETE
-   JSON
-   API Requests
-   API Responses
-   HTTP Status Codes
-   FastAPI
-   API Integration

Target architecture:

``` text
Python
   ↓
SQLite / SQL
   ↓
REST APIs
   ↓
FastAPI
   ↓
AI / LLM Applications
   ↓
RAG
   ↓
AI Agents
   ↓
Automation
```

------------------------------------------------------------------------

# 🏁 DAY 11 COMPLETE

Learn → Build → Test → Document → Share → Improve

## 🎯 Goal: Job-Ready AI Automation Engineer
