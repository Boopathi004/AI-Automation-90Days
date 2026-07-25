#Exercise 1: creating a file and writing data to it Write(w)

file = open("notes.txt", "w")

file.write("Welcome to Python File Handling\n")
file.write("Today I learned File Handling.\n")

file.close()
print("Data written successfully.")

#Exercise 2: reading data from a file Read(r)
file = open("notes.txt", "r")

content = file.read()
print(content)
file.close()

#Exercise 3: appending data to a file Append(a)

file = open("notes.txt", "a")
file.write("This is an appended line.\n")
file.close()
print("Data appended successfully.")

#exercise 4: using with open() as context manager
with open("notes.txt", "r") as file:
    content = file.read()
print(content)

 #Exercise 5: reading a file line by line
with open("notes.txt", "r") as file:

    for line in file:
        print(line)

#exercise 6: student report 

student = "Boopathi"
marks = 98

with open("student_report.txt", "w") as file:

    file.write("Student Report\n")
    file.write("----------------\n")
    file.write(f"Name : {student}\n")
    file.write(f"Marks : {marks}\n")

print("Report Created.")

#Exercise 7: reading student report
with open("student_report.txt", "r") as file:
    content = file.read()
    print(content)


#mini project: daily learning journal

day = input("Enter Day: ")
topic = input("Topic Learned: ")

with open("journal.txt", "a") as file:

    file.write(f"{day} - {topic}\n")

print("Journal Updated.")

#reading the journal
with open("journal.txt", "r") as file:

    print(file.read())