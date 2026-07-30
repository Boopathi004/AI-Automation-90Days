import csv

rows = []

student = input("Enter Student Name : ")

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        if len(row) > 1 and row[1].lower() == student.lower():

            row[3] = "AI"

        rows.append(row)

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(rows)

print("Student Updated")