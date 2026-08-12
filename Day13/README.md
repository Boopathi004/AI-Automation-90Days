# 🚀 Day 13 – Advanced Python for Automation

## 🎯 Day Objective

Today I focused on advanced Python concepts useful for building
reusable, efficient, and maintainable automation systems.

### Topics Covered

- 🧩 Python Decorators
- 🔄 Generators and `yield`
- ⏱️ Execution-time measurement
- 🛡️ Error handling
- 📊 Employee data processing
- 📈 Employee and department analytics
- ⚙️ Automation workflow design

------------------------------------------------------------------------

## 📚 Session 1 – Python Decorators

A decorator extends or modifies the behavior of another function without
changing its original code.

``` python
def execution_logger(func):
    def wrapper(*args, **kwargs):
        # additional behavior
        result = func(*args, **kwargs)
        return result
    return wrapper
```

### Practical Work

Created an `execution_logger` decorator that: - Records start time -
Executes the target function - Records end time - Calculates execution
time - Prints the function name - Reports completion

### Real-world uses

- Logging
- Monitoring
- Validation
- Authentication
- Retry logic
- Error tracking

------------------------------------------------------------------------

## 🔄 Session 2 – Python Generators

Generators produce values one at a time using `yield`.

``` python
def employees_generator():
    for employee in range(101, 106):
        yield employee

print(list(employees_generator()))
```

Output:

``` text
[101, 102, 103, 104, 105]
```

### Key Learning

Generators use lazy evaluation and are useful for: - Large datasets -
API response processing - Database records - File processing - Streaming
data - Automation pipelines

------------------------------------------------------------------------

## 📝 Session 3 – Employee Logger

Combined decorators and generators to build an employee processing
workflow.

### Features

- Employee data generation
- Employee processing
- Execution logging
- Total employee calculation
- Total salary calculation
- Average salary calculation
- Highest salary calculation
- Employee report generation

Example:

``` text
=== Employee Report ===
total employees: 5
total salary: 258000
average salary: 51600.0
highest salary: 60000
```

------------------------------------------------------------------------

## ⚙️ Session 4 – Employee Automation & Analytics

Built a practical employee automation system combining the day’s
concepts.

### Features

- 👥 Total employee count
- 💰 Total salary
- 📊 Average salary
- 🏆 Highest-paid employee
- 🏢 Department-wise analytics
- 🔄 Generator-based processing
- ⏱️ Execution-time logging
- 🛡️ Error handling

Final result:

``` text
Total Employees : 5
Total Salary    : ₹258000
Average Salary  : ₹51600.00
Highest Salary  : Priya - ₹60000

DEPARTMENT ANALYTICS
IT : 3 employees
HR : 1 employees
Finance : 1 employees
```

------------------------------------------------------------------------

## 🧠 Skills Learned

- Python decorators
- Wrapper functions
- `*args` and `**kwargs`
- Generators
- `yield`
- Lazy evaluation
- Iterator concepts
- Execution-time measurement
- Error handling
- Employee data processing
- Salary analytics
- Department analytics
- Reusable automation patterns

------------------------------------------------------------------------

## 💼 AI Automation Connection

These concepts will be useful later with:

- REST APIs
- OpenAI APIs
- LLM applications
- RAG pipelines
- AI agents
- n8n
- Make.com
- Database automation

------------------------------------------------------------------------

## 📁 Day 13 Files

``` text
Day13/
├── session1_decorators.py
├── session2_generators.py
├── session3_employee_logger.py
└── session4_employee_automation.py
```

------------------------------------------------------------------------

## ✅ Day 13 Status

**COMPLETED ✅**

**13 / 90 Days Completed**

**Progress: 14.4%**

> 🚀 Advanced Python today. AI Automation tomorrow.
