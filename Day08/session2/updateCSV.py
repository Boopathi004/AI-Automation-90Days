import csv

employee_id = input("Employee ID to Update : ")

rows = []

with open("employee_data.csv", "r") as file:

    reader = csv.reader(file)

    header = next(reader)

    rows.append(header)

    for row in reader:

        if row[0] == employee_id:

            row[1] = input("New Name : ")
            row[2] = input("Department : ")
            row[3] = input("Salary : ")
            row[4] = input("Email : ")
            row[5] = input("Joining Date : ")

        rows.append(row)

with open("employee_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(rows)

print("Employee Updated Successfully")