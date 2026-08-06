class InsufficientBalanceError(Exception):
    pass

balance = 5000

withdraw = int(input("Withdraw Amount: "))

try:

    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient Balance")

    balance -= withdraw

    print("Remaining Balance :", balance)

except InsufficientBalanceError as error:

    print(error)