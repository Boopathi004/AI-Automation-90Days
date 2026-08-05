import csv

employees = [
    [101, "Boopathi", "IT", 50000],
    [102, "Ram", "HR", 45000],
    [103, "Arjun", "Sales", 55000]
]

with open("employees.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Department", "Salary"])

    writer.writerows(employees)

print("Employee Data Written Successfully")