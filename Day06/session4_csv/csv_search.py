import csv

student = input("Enter Student Name : ")

found = False

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        if student.lower() == row[1].lower():

            print(row)

            found = True

if not found:
    print("Student Not Found")