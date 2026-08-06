import logging

logging.basicConfig(

    filename="error.log",

    level=logging.ERROR,

    format="%(asctime)s - %(levelname)s - %(message)s"

)

try:

    number = int(input("Enter Number: "))

    print(100 / number)

except Exception as e:

    logging.exception("Exception Occurred")

    print("Error Logged Successfully")