try:

    number = int(input("Enter Number: "))

    result = 100 / number

except Exception as error:

    print(error)

else:

    print("Division Successful")

    print("Result :", result)

finally:

    print("Program Finished")