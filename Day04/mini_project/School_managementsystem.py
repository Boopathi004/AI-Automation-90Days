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
stud2=Student("man",21,"PG")

stud1.student_details()
stud2.student_details()