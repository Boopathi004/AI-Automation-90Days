import json

employees = [

{
"id":101,
"name":"Boopathi",
"department":"IT",
"salary":50000
},

{
"id":102,
"name":"Ram",
"department":"HR",
"salary":45000
},

{
"id":103,
"name":"Arjun",
"department":"Sales",
"salary":55000
}

]

with open("employees.json","w") as file:
    json.dump(employees,file,indent=4)

print("Employees Saved")