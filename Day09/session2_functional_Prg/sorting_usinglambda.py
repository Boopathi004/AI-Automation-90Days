employees=[
    ("Boopathi",50000),
    ("Ram",35000),
    ("Arjun",60000),
    ("John",45000)
]

employees.sort(key=lambda employee:employee[1])

print(employees)