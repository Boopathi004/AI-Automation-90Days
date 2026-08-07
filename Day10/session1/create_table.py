import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employee1
                  (id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL, join_date TEXT , phone_number TEXT, email TEXT)''')

print("Table Created Successfully!")
connection.commit()
connection.close()