# exercise 1: functions
def greet():
    print("welcome to python")

greet()

# exercise 2: functions with parameters
def add(num1, num2):
    return num1 + num2

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
result = add(number1, number2)
print("The sum of", number1, "and", number2, "is:", result)

# exercise 3: find largest number using function
def find_largest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

a =int(input("Enter first number: "))
b =int(input("Enter second number: "))

largest = find_largest(a, b)
print("The largest number between", a, "and", b, "is:", largest)

# exercise 4: check if number is even or odd using function
def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("Enter a number: "))
result = check_even_odd(number)
print(result)

# exercise 5: student information using function
def student_info(name, age, Course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", Course)

student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))    
student_course = input("Enter your course: ")
student_info(student_name, student_age, student_course) 
