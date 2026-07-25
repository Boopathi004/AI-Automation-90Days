#exercise 1:

#creating a tuple
city=("Chennai", "Bangalore", "Hyderabad", "Mumbai", "Delhi")
print(city)

#Exercise 2 print 1st and last city
print(city[0])
print(city[-1])

#Exercise 3: print negative indexing
print(city[-2])

#exercise 4: print slicing
print(city[2:4])

#exercise 5: 
numbers = (10,20,30,20,40,20)
print(numbers.count(20))

#exercise 6: find the index of 40
print(numbers.index(40))

#exercise 7 : unboxing a tuple
student = ("Boopathi",27,"Python")
student_name, student_age, student_course = student
print(student_name)
print(student_age)
print(student_course)

#mini Project 

# creating a employee tuple 
employee = (
    1001,
    "Boopathi",
    "Software Engineer",
    800000
)
employee_id, employee_name, employee_designation, employee_salary = employee
print("Employee ID:", employee_id)
print("Employee Name:", employee_name)
print("Employee Designation:", employee_designation)
print("Employee Salary:", employee_salary)