# 📝 Day 13 – Complete Learning Notes

## Advanced Python for AI Automation

Today I learned advanced Python concepts that make automation code
reusable, efficient, measurable, and maintainable.

------------------------------------------------------------------------

# 1. Python Decorators

A decorator is a function that receives another function and extends or
modifies its behavior.

``` python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
```

Usage:

``` python
@my_decorator
def hello():
    print("Hello")
```

`@my_decorator` is equivalent to:

``` python
hello = my_decorator(hello)
```

------------------------------------------------------------------------

# 2. Wrapper Functions

A wrapper is an inner function used by a decorator.

``` python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

- `*args` → positional arguments
- `**kwargs` → keyword arguments

This allows a decorator to work with different function signatures.

------------------------------------------------------------------------

# 3. Execution Logger

A practical decorator created today measured function execution time.

``` python
import time

def execution_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        try:
            result = func(*args, **kwargs)
            return result
        except Exception as error:
            print(f"Error: {error}")
        finally:
            end_time = time.time()
            execution_time = end_time - start_time

            print(f"Completed: {func.__name__}")
            print(f"Execution Time: {execution_time:.4f} seconds")

    return wrapper
```

Execution time:

``` python
execution_time = end_time - start_time
```

------------------------------------------------------------------------

# 4. Generators

A generator produces values one at a time.

``` python
def employee_generator(employees):
    for employee in employees:
        yield employee
```

A generator is consumed as needed instead of creating the entire output
at once.

------------------------------------------------------------------------

# 5. `yield` vs `return`

### `return`

Stops the function and returns a result.

``` python
def numbers():
    return [1, 2, 3, 4, 5]
```

### `yield`

Produces values one at a time.

``` python
def numbers():
    for i in range(1, 6):
        yield i
```

Generators are especially useful for large datasets and streaming
workflows.

------------------------------------------------------------------------

# 6. Employee Analytics

Example employee data:

``` python
employees = [
    {"id": 101, "name": "Boopathi", "department": "IT", "salary": 50000},
    {"id": 102, "name": "Arun", "department": "HR", "salary": 45000},
    {"id": 103, "name": "Kumar", "department": "IT", "salary": 55000},
    {"id": 104, "name": "Ravi", "department": "Finance", "salary": 48000},
    {"id": 105, "name": "Priya", "department": "IT", "salary": 60000}
]
```

### Total Employees

``` python
total_employees = len(employees)
```

### Total Salary

``` python
total_salary = sum(emp["salary"] for emp in employees)
```

### Average Salary

``` python
if total_employees > 0:
    average_salary = total_salary / total_employees
else:
    average_salary = 0
```

### Highest Salary

``` python
highest_employee = max(
    employees,
    key=lambda employee: employee["salary"]
)
```

------------------------------------------------------------------------

# 7. Department Analytics

Departments can be collected using:

``` python
departments = {
    employee["department"]
    for employee in employees
}
```

Then each department can be counted:

``` python
for department in departments:
    count = sum(
        1 for employee in employees
        if employee["department"] == department
    )
    print(department, count)
```

------------------------------------------------------------------------

# 8. Errors Encountered and Fixed

## Error 1 – Local Variable Scope

``` text
cannot access local variable 'employees'
where it is not associated with a value
```

### Lesson

Be careful with local/global scope and avoid accidentally reusing a
variable name inside a function.

A clean approach is to pass data explicitly:

``` python
def process_employees(employees):
    ...
```

## Error 2 – Division by Zero

``` text
Error: division by zero
```

### Cause

The average calculation attempted to divide by zero.

### Fix

``` python
if total_employees > 0:
    average_salary = total_salary / total_employees
else:
    average_salary = 0
```

------------------------------------------------------------------------

# 9. Final Day 13 Architecture

``` text
Employee Data
      ↓
Employee Generator
      ↓
Process Employees
      ↓
Execution Logger Decorator
      ↓
Employee Analytics
      ↓
├── Total Employees
├── Total Salary
├── Average Salary
├── Highest Salary
└── Department Analysis
```

------------------------------------------------------------------------

# 10. Real-World AI Automation Applications

### Decorators

- API logging
- Retry mechanisms
- Execution monitoring
- Error tracking
- Authentication

### Generators

- Large API responses
- Streaming data
- Large files
- Database records
- Automation pipelines

### Future integrations

- OpenAI APIs
- LLM applications
- RAG
- AI Agents
- n8n
- Make.com
- REST APIs
- Database automation

------------------------------------------------------------------------

# 🎤 Interview Questions

### 1. What is a decorator?

A function that extends or modifies another function’s behavior without
changing its original implementation.

### 2. What is a generator?

A function that uses `yield` to produce values lazily.

### 3. `return` vs `yield`?

`return` ends the function; `yield` pauses a generator and produces a
value.

### 4. Why are generators memory efficient?

They generate values on demand rather than storing the complete sequence
in memory.

### 5. Why use `*args` and `**kwargs` in decorators?

To support functions with different positional and keyword arguments.

### 6. How do you measure execution time?

``` python
start = time.time()
# operation
end = time.time()
execution_time = end - start
```

### 7. How do you prevent division by zero?

``` python
if count > 0:
    average = total / count
```

------------------------------------------------------------------------

# 🏆 Day 13 Summary

``` text
Python Decorators       ✅
Wrapper Functions       ✅
*args / **kwargs        ✅
Execution Logging       ✅
Generators              ✅
yield                   ✅
Lazy Evaluation         ✅
Error Handling          ✅
Employee Processing     ✅
Salary Analytics        ✅
Department Analytics    ✅
Automation Workflow     ✅
```

## Final Takeaway

> **Decorators add reusable behavior.**
>
> **Generators process data efficiently.**
>
> **Together, they are powerful building blocks for automation
> systems.**

## Day 13 Status

**✅ COMPLETED — 13 / 90 Days — 14.4%**
