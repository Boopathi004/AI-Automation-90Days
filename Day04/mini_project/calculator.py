try:

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    print("Addition:", num1 + num2)
    print("Division:", num1 / num2)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Enter numbers only.")