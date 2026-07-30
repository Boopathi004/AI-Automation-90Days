import csv

with open("students.csv", "a", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([103, "Ajay", 24, "Sales"])

print("Student Added Successfully")