import csv

with open("employees.csv", "a", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([104, "Karthik", "Testing", 47000])

print("Employee Added Successfully")