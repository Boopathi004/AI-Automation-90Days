import csv

employee_id = input("Employee ID to Delete : ")

rows = []

with open("employee_data.csv", "r") as file:

    reader = csv.reader(file)

    header = next(reader)

    rows.append(header)

    for row in reader:

        if row[0] != employee_id:
            rows.append(row)

with open("employee_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(rows)

print("Employee Deleted Successfully")