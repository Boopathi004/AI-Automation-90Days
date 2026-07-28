class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Boopathi", 50000)

account.deposit(10000)
account.withdraw(15000)

print("Account Holder:", account.account_holder)
print("Balance:", account.get_balance())