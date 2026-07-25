#Exersise1 : creatin g a dictionary with key value pairs
student = {
    "name":"Boopathi",
    "age":27,
    "course":"Python"
}
print(student)

#exercise2: accessing values from a dictionary
print(student["name"])
print(student["course"])

#exercise3: adding a new key value pair to a dictionary
student["city"]="Chennai"
print(student)

#exercise4: updating a value in a dictionary
student["age"]=28
print(student)

#exercise5: removing a key value pair from a dictionary
student.pop("course")
print(student)

#exercise6: print all key value and items in a dictionary
print(student.keys())
print(student.values())
print(student.items())

#exercise7: looping through a dictionary
for key, value in student.items():
    print(key, ":", value)

#exercise8: nested dictionary
students1 = { 101: {"name": "Boopathi", "age": 27, "salary": 80000}, 
             102: {"name": "Arun", "age": 25, "salary": 70000}, 
             103: {"name": "Vijay", "age": 30, "salary": 90000} }
print(students1)
print(students1[101]["name"])

#Mini Project: creating a dictionary of students with their details
student2 = {
    "Name":"Boopathi",
    "Age":27,
    "Course":"AI Automation",
    "City":"Chennai",
    "Marks":95
}
student2["Marks"]=98
student2["Grade"]="A"

for key, value in student2.items():
    print(key, ":", value)
    


             
