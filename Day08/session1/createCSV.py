import csv

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Department", "Salary"])

print("CSV File Created Successfully")