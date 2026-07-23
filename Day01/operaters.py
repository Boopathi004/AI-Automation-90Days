'''exercises1 arithmetic operators'''

first_number=int(input("Enter first number: "))
second_number=int(input("Enter second number: "))
addition=first_number+second_number
subtraction=first_number-second_number
multiplication=first_number*second_number  
division=first_number/second_number
print("Addition:",addition)
print("Subtraction:",subtraction)   
print("Multiplication:",multiplication)
print("Division:",division) 

'''exercises2 comparison operators'''
first_number=int(input("Enter first number: "))
second_number=int(input("Enter second number: "))
if first_number == second_number:
    print("Both numbers are equal")
elif first_number > second_number:
    print("First number is greater than second number") 
else:
    print("First number is not greater than second number")


'''exercises3 logical operators'''
Name=input("Enter your name: ")
age=int(input("Enter your age: "))
if age >= 18 and age <= 30:
    print(Name,"is eligible to apply for the job")