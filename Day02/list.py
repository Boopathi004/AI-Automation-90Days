# creating a list 

students = ["Boopathi", "Arun", "Vijay", "Kumar"]
print(students)

# accessing elements in a listusing index
print(students[0]) 
print(students[1])  
print(students[2])
print(students[3]) 

#Negative indexing
print(students[-1])
print(students[-2])

#slicing a list
print(students[0:3])

# adding elements to a list
students.append("Ramesh")
print(students)

#inserting elements to a list
students.insert(2, "Suresh")
print(students)

#removing elements from a list
students.remove("Vijay")
print(students)

#popping elements from a list
students.pop()
print(students)

# remove an element by index
students.pop(1)
print(students) 

#sorting a list
students.sort()
print(students)

#reversing a list
students.reverse()
print(students)

#length of a list
print(len(students))
print("The number of students in the list is:", len(students))

#Exercise1: 
Fruits = ["Apple", "Banana", "Mango", "Orange","strawberry"]
print(Fruits)

# Exercise2:
print(Fruits[0])
print(Fruits[4])

#exercise3:
Fruits.append("Grapes")
print(Fruits)

#exercise4:
Fruits.insert(2, "Pineapple")
print(Fruits)

#exercise5:
Fruits.sort()
print(Fruits)

#exercise6:
Fruits.reverse()
print(Fruits)

#exercise7:
Fruits.remove("Banana")
print(Fruits)

#exercise8:
fruits_length = len(Fruits)
print("The number of fruits in the list is:", fruits_length)

# Mini Project Creating a students list 
#1. View Students
#2. Add Student
#3. Remove Student
#4. Exit

Students1=["bala","karthi","Rishak","ram","Rohan"]
print(Students1)

# adding a new student to the list
new_student = input("Enter a new student name to add: ")
Students1.append(new_student)
print(Students1)

# removing a student from the list
removed_student = input("Enter the name of the student to remove: ")
Students1.remove(removed_student)
print(Students1)

#exiting the program
end = input("Do you want to exit? (yes/no): ")
if end.lower() == "yes":
    print("Exiting the program.")