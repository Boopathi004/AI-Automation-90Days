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