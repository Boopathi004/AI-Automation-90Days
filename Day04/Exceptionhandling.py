#try and expect 

try:
    number = int(input("Enter a number: "))
    print(100 / number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid number.")

#Multiple Exception 

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot divide by zero")

#else 
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ZeroDivisionError:
    print("Division by zero")

else:
    print("Result:", result)

#finally
try:
    file = open("sample.txt")

except FileNotFoundError:
    print("File not found")

finally:
    print("Program Finished")

#raise
age = int(input("Enter Age: "))

if age < 18:
    raise Exception("You must be 18 or above.")

print("Eligible")

#Custom 
class InvalidAgeError(Exception):
    pass


age = int(input("Enter Age: "))

if age < 18:
    raise InvalidAgeError("Age must be 18 or above.")

print("Welcome")