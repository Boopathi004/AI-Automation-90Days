try:

    number = int(input("Enter Number: "))

    result = 100 / number

    print(result)

except ValueError:
    print("Invalid Number")

except ZeroDivisionError:
    print("Division by Zero is not Allowed")

except Exception as error:
    print("Unexpected Error :", error)