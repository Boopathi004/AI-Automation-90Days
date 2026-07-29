# Exersise 1 Math module

import math

print("===== Math Module =====")

print("Square Root:", math.sqrt(64))
print("Power:", math.pow(2, 5))
print("Ceiling:", math.ceil(5.2))
print("Floor:", math.floor(5.9))
print("Factorial:", math.factorial(5))
print("Value of Pi:", math.pi)

#Exersise 2 random module 

import random

print("\n===== Random Module =====")

print("Random Number:", random.randint(1, 100))

fruits = ["Apple", "Banana", "Orange", "Mango"]

print("Random Fruit:", random.choice(fruits))

random.shuffle(fruits)

print("Shuffled List:", fruits)

# Exersise 3 date time Module 

from datetime import datetime

print("\n===== Datetime Module =====")

now = datetime.now()

print("Current Date & Time:", now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

print("Time:", now.strftime("%H:%M:%S"))

print("Date:", now.strftime("%d-%m-%Y"))

# Exersise 4 OS module 

import os

print("\n===== OS Module =====")

print("Current Folder:")

print(os.getcwd())

print("\nFiles:")

print(os.listdir())

# Exersise 5 Json module

import json

print("\n===== JSON Module =====")

student = {
    "Name": "Boopathi",
    "Age": 27,
    "Course": "AI Automation"
}

json_data = json.dumps(student, indent=4)

print(json_data)