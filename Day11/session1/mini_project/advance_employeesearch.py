import sqlite3
connection = sqlite3.connect('employee1.db')
name = input("Enter name to search: ")
if  name=="boopathi":
        connection = sqlite3.connect('employee1.db')
        cursor = connection.cursor()

        cursor.execute('''SELECT *
        FROM employees1
        WHERE name LIKE ?;''', ('%' + name + '%',))
        employees = cursor.fetchall()   
        print(f"Employees with name containing '{name}':")
        for emp in employees:
         print(emp)
        connection.close()
else:
    print("No employees found with the given name.")


connection = sqlite3.connect('employee1.db')
cursor = connection.cursor()
cursor.execute('''SELECT *
FROM employees1
WHERE department IN ('it', 'HR', 'admin');''')
employees = cursor.fetchall()
print(f"Employees in departments 'it', 'HR', 'admin':")
for emp in employees:
    print(emp)
connection.close()

connection = sqlite3.connect('employee1.db')
cursor = connection.cursor()
cursor.execute('''SELECT *
FROM employees1
WHERE salary BETWEEN 41000 AND 45000;''')
employees = cursor.fetchall()
print(f"Employees with salary between 41000 and 45000:")
for emp in employees:
    print(emp)
connection.close()

connection = sqlite3.connect('employee1.db')
cursor = connection.cursor()    
cursor.execute('''SELECT *
FROM employees1
LIMIT 5 OFFSET 5;''')
