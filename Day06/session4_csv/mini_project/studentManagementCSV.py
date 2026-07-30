import csv
import os

FILE_NAME = "students.csv"

# Create CSV file with header if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Department"])


# ---------------- ADD STUDENT ----------------

def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, department])

    print("\n✅ Student Added Successfully.\n")


# ---------------- VIEW STUDENTS ----------------

def view_students():

    print("\n========== STUDENT LIST ==========\n")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

    print()


# ---------------- SEARCH STUDENT ----------------

def search_student():

    name = input("Enter Student Name: ")

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) > 1 and row[1].lower() == name.lower():
                print("\nStudent Found")
                print(row)
                found = True
                break

    if not found:
        print("\nStudent Not Found")


# ---------------- UPDATE STUDENT ----------------

def update_student():

    name = input("Enter Student Name to Update: ")

    rows = []

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) > 1 and row[1].lower() == name.lower():

                print("\nCurrent Record:", row)

                row[3] = input("Enter New Department: ")

                found = True

            rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(rows)

    if found:
        print("\n✅ Student Updated Successfully")
    else:
        print("\nStudent Not Found")


# ---------------- DELETE STUDENT ----------------

def delete_student():

    name = input("Enter Student Name to Delete: ")

    rows = []

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) > 1 and row[1].lower() == name.lower():

                found = True

                continue

            rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(rows)

    if found:
        print("\n✅ Student Deleted Successfully")
    else:
        print("\nStudent Not Found")


# ---------------- COUNT STUDENTS ----------------

def total_students():

    count = 0

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:
            count += 1

    print(f"\nTotal Students : {count}")


# ---------------- MENU ----------------

while True:

    print("\n" + "=" * 40)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        total_students()

    elif choice == "7":
        print("\n👋 Thank you for using Student Management System!")
        break

    else:
        print("\n❌ Invalid Choice")