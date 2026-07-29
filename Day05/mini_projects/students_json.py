import json

student = {
    "Name": "Boopathi",
    "Marks": 98,
    "Course": "Python"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON File Created Successfully")

with open("student.json", "r") as file:
    data = json.load(file)

print(data)