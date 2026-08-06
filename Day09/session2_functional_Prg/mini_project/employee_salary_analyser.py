import json
from functools import reduce

with open("employee_salary.json", "r") as file:
    employees = json.load(file)

print("=" * 50)
print("EMPLOYEE SALARY ANALYZER")
print("=" * 50)

# Employee Names
names = list(map(lambda emp: emp["name"], employees))

print("\nEmployee Names")
for name in names:
    print(name)

# High Salary Employees
high_salary = list(filter(lambda emp: emp["salary"] >= 50000, employees))

print("\nEmployees with Salary >= 50000")
for emp in high_salary:
    print(f'{emp["name"]} : {emp["salary"]}')

# Total Salary
total_salary = reduce(lambda total, emp: total + emp["salary"], employees, 0)

print("\nTotal Salary :", total_salary)

# Average Salary
average_salary = total_salary / len(employees)

print("Average Salary :", average_salary)

# Highest Salary
highest = max(employees, key=lambda emp: emp["salary"])

print("\nHighest Paid Employee")
print(highest)

# Lowest Salary
lowest = min(employees, key=lambda emp: emp["salary"])

print("\nLowest Paid Employee")
print(lowest)

# Sort by Salary
sorted_employees = sorted(employees, key=lambda emp: emp["salary"])

print("\nEmployees Sorted by Salary")

for emp in sorted_employees:
    print(f'{emp["name"]} - {emp["salary"]}')