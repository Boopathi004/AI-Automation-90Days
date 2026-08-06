class InsufficientBalanceError(Exception):
    """Custom Exception for insufficient balance."""
    pass


balance = 10000

while True:

    print("\n" + "=" * 40)
    print("      BANK MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    try:
        choice = int(input("\nEnter Your Choice: "))

        # Deposit
        if choice == 1:
            amount = float(input("Enter Deposit Amount: ₹"))

            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

            balance += amount

            print(f"\n✅ ₹{amount:.2f} Deposited Successfully.")
            print(f"Current Balance : ₹{balance:.2f}")

        # Withdraw
        elif choice == 2:
            amount = float(input("Enter Withdraw Amount: ₹"))

            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

            if amount > balance:
                raise InsufficientBalanceError("Insufficient Balance!")

            balance -= amount

            print(f"\n✅ ₹{amount:.2f} Withdrawn Successfully.")
            print(f"Remaining Balance : ₹{balance:.2f}")

        # Check Balance
        elif choice == 3:
            print(f"\n💰 Current Balance : ₹{balance:.2f}")

        # Exit
        elif choice == 4:
            print("\n🙏 Thank You for Using Bank Management System.")
            break

        else:
            print("\n❌ Invalid Choice. Please select between 1 and 4.")

    except ValueError as error:
        print(f"\n⚠ {error}")

    except InsufficientBalanceError as error:
        print(f"\n⚠ {error}")

    except Exception as error:
        print("\nUnexpected Error:", error)

    finally:
        print("-" * 40)