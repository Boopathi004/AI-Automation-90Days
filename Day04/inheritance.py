# Exersise 1 Single inheritance 
class Animal:
    def sound(self):
        print("Animals make sounds")
class Dog(Animal):
    pass
dog = Dog()
dog.sound()

#Exersise 2 Parent and child 
class Person:
    def introduce(self):
        print("I am a Person")
class Student(Person):
    pass
student = Student()
student.introduce()

#Exersise 3 vehicle 
class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass
car = Car()
car.start()

# Exersise 4 Employee
class Employee:
    def work(self):
        print("Employee is working")
class Manager(Employee):
    pass

manager = Manager()
manager.work()

#Exersise 5 mobile 
class Mobile:
    def call(self):
        print("Calling...")
class SmartPhone(Mobile):
    pass

phone = SmartPhone()
phone.call()

#mini project School manangement 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
class Student(Person) :
    def __init__(self, name, age, course):
     super().__init__(name, age)
     self.course=course
   
    def student_details(self):
        self.display()
        print("course:",self.course)

stud1=Student("mnoo",23,"compute")

stud1.student_details()


     

        