import json

employee = {
    "id":101,
    "name":"Boopathi",
    "department":"IT",
    "salary":50000
}

with open("employee.json","w") as file:
    json.dump(employee,file,indent=4)

print("JSON Created Successfully")