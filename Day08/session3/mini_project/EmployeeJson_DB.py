import json

employees = [

{
"id":101,
"name":"Boopathi",
"department":"IT",
"salary":50000,
"email":"boopathi@gmail.com"
},

{
"id":102,
"name":"Ram",
"department":"HR",
"salary":45000,
"email":"ram@gmail.com"
},

{
"id":103,
"name":"Arjun",
"department":"Sales",
"salary":55000,
"email":"arjun@gmail.com"
}

]

with open("employee_database.json","w") as file:

    json.dump(employees,file,indent=4)

print("Database Created")

with open("employee_database.json","r") as file:

    database=json.load(file)

print()

print("Employee List")

for employee in database:

    print(employee)