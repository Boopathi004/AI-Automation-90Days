balance = 5000

try:
    amount = float(input("Enter Withdrawal Amount: "))

    if amount > balance:
        raise Exception("Insufficient Balance")

    balance -= amount

    print("Withdrawal Successful")
    print("Remaining Balance:", balance)

except Exception as e:
    print("Error:", e)