# 🚀 Day 11 – Advanced SQLite & Relational Database Programming

## 🎯 Day 11 Objective

Today I moved beyond basic SQLite CRUD operations and learned how to build more reliable and professional database-driven applications using Python and SQLite.

The main focus was:

- Advanced SQL Queries
- Database Constraints
- Data Integrity
- Relationships
- JOIN Operations
- SQL Aggregations
- Database Reports
- Exception Handling
- Building a Complete Management System

---

# 📚 Sessions Completed

## ✅ Session 1 – Advanced SQL Queries

### Topics Learned

- `WHERE`
- `LIKE`
- `IN`
- `BETWEEN`
- `ORDER BY`
- `LIMIT`
- `OFFSET`
- Searching database records
- Filtering database records
- Sorting query results

### Mini Project

🔍 Advanced Employee Search

Features:

- Search employees by name
- Search employees based on salary
- Count total employees
- Filter records using SQL conditions

---

## ✅ Session 2 – Database Constraints & Data Integrity

### Topics Learned

- Primary Key
- Foreign Key
- `NOT NULL`
- `UNIQUE`
- `CHECK`
- `DEFAULT`
- Data validation
- SQLite `IntegrityError`
- Maintaining database integrity

### Why Constraints Matter

Database constraints prevent invalid or duplicate data from entering the database.

Example:

```sql
salary REAL CHECK(salary > 0)