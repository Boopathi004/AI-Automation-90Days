# Exersice 1 Create a Car class with constuctor .
#Fields:
#Brand
#Model
#Price
#Create two objects.
class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
car1=Car("BMW",2012,4000000)
car2=Car("AUDi",2016,1300000)

print(car1.price,car1.model,car1.brand)
print(car2.price,car2.model,car2.brand)

#Exercise 2 Create a Laptop class.
#Fields:
#Brand
#RAM
#Processor
#Price
#Create two objects.

class Laptop:
    def __init__(self,Brand,Ram,Processer,Price):
        self.Brand=Brand
        self.Ram=Ram
        self.Processer=Processer
        self.Price=Price
lap1=Laptop("dell","4GB","i5",45000)
lap2=Laptop("ThinkPad","8GB","i10",55000)

print(lap1.Brand,lap1.Ram,lap1.Processer,lap1.Price)     
print(lap2.Brand,lap2.Ram,lap2.Price)          

#Exersise 3 Create a Book class.
#Fields:
#Title
#Author
#Price
#Create two objects.

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
book1=Book("Automic Habits","boo",230)
book2=Book("Game Of Money","lee",320)

print(book1.title,book1.author,book1.price)
print(book2.title,book2.author,book2.price)

#Exersise 4 Create a Movie class.
#Fields:
#Name
#Hero
#Rating
#Create two objects.
class Movie:
    def __init__(self,name,hero,rating):
        self.name=name
        self.hero=hero
        self.rating=rating
moe1=Movie("Kala","Rajini",8.5)
moe2=Movie("KGF","karthi",9.3)

print(moe1.name,moe1.hero,moe1.rating)
print(moe2.name,moe2.hero,moe2.rating)

#Mini Project
#Create a Student Management System.
#The Student class should contain:
#Roll No
#Name
#Age
#Course
#City
#Marks
class Student:
    def __init__(self,name,rollno,age,course,city,mark):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.course=course
        self.city=city
        self.mark=mark

stud1=Student("karthi",7,23,"computer Science","Madurai",95)
stud2=Student("karthi",21,22,"commerse","Dindigul",90)
stud3=Student("karthi",37,24,"Biology","Theni",75)

print(stud1.name,stud1.rollno,stud1.age,stud1.course,stud1.city,stud1.mark)
print(stud2.name,stud2.rollno,stud2.age,stud2.course,stud2.city,stud2.mark)
print(stud3.name,stud3.rollno,stud3.age,stud3.course,stud3.city,stud3.mark)