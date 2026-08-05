import json

with open("employees.json","r") as file:
    employees = json.load(file)

employees.append({

"id":104,
"name":"Priya",
"department":"Finance",
"salary":60000

})

with open("employees.json","w") as file:
    json.dump(employees,file,indent=4)

print("Employee Added Successfully")