import json

with open("employees.json","r") as file:

    employees = json.load(file)

for employee in employees:

    print(employee)