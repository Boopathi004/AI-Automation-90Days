import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Age", "Department"])

    writer.writerow([101, "Boopathi", 26, "IT"])

    writer.writerow([102, "Ram", 25, "HR"])

print("CSV Created Successfully")