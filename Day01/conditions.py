'''exe1'''
Name=input("Enter your name: ")
age=int(input("Enter your age: "))
if age <18:
    print("you are minor")
elif age >= 18 and age <= 65:
    print("you are middle-aged")
else:
    print("you are a senior citizen")

    '''exe2'''
    number1=int(input("Enter a number1: "))
    number2=int(input("Enter a number2: "))
    if number1 > number2:
        print(number1, "is greater than", number2)
    else:
        print(number2, "is greater than", number1)

'''exe3'''
year=int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

'''exe4'''
name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
if marks >= 90:
    print(name, "has scored an A grade")
elif marks >= 80:
    print(name, "has scored a B grade")
elif marks >= 70 and marks < 80:
    print(name, "has scored a C grade")
elif marks >= 60 and marks < 70:
    print(name, "has scored a D grade")
elif marks >50:
    print(name, "has scored an F grade")
elif marks >=35:
    print(name, "has scored an G grade")
else:
    print(name, "you failed the exam")