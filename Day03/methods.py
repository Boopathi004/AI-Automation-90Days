#Exersise 1  Car Class in method 

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car1 = Car("BMW", 2022)
car1.display()

#Exersise 2 Student Method 
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Boopathi", 27)
s1.details()

#Exersise 3 Employe Method 
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def salary_info(self):
        print(self.name)
        print(self.salary)

emp = Employee("Arun", 55000)
emp.salary_info()

#Execsise 4 Laptop Method 
class Laptop:

    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def specs(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)

lap = Laptop("Dell", "16GB")
lap.specs()

#Exersise 5 Book Method 
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show(self):
        print("Title:", self.title)
        print("Author:", self.author)

book = Book("Atomic Habits", "James Clear")
book.show()

# Mini Project Create a Gym Member Management System.
#Fields:
#Name
#Age
#Plan
#Fee
class Gym :
    def __init__(self,name,age,plan,fee):
        self.name=name
        self.age=age
        self.plan=plan
        self.fee=fee

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("plan:",self.plan)
        print("fee:",self.fee) 
gym1=Gym("bala",45,"standed",1200)
gym1.display()

gym2=Gym("Boopathi",27,"preminum ",2000)
gym2.display()
        
        