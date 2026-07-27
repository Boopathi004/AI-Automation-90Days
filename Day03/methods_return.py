#Exersise 1  With return type 
class Calculator:

    def add(self, a, b):
        return a + b

cal = Calculator()
result = cal.add(10, 20)
print("Addition:", result)

# Emplyee Salary 
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_salary(self):
        return self.salary * 12

emp = Employee("Boopathi", 50000)

print("Employee:", emp.name)
print("Yearly Salary:", emp.yearly_salary())

# Student Percentage 

class Student:

    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def percentage(self):
        total = self.mark1 + self.mark2 + self.mark3
        return total / 3

student = Student("Boopathi", 95, 90, 98)

print(student.name)
print("Percentage:", student.percentage())

#Exersise 4 Area of rectangle 
class Rectangle:

    def area(self, length, width):
        return length * width

rect = Rectangle()

print("Area:", rect.area(20, 10))


# Todays Chanllenge and mini project Movie ticket booking 

class Movie :
    def __init__(self,movie_name,price,ticket_count ):
        self.movie_name=movie_name
        self.price=price
        self.ticket_count=ticket_count

    def total_price (self):
        total=self.price*self.ticket_count
        return total
moe1=Movie("sarthar",200,3)
print("movie Name :",moe1.movie_name, "Total Price :",moe1.total_price())
   

        
