# protected member Uing(_)

class Employee:

    def __init__(self):
        self._salary = 50000

class Manager(Employee):

    def display(self):
        print(self._salary)

manager = Manager()
manager.display()

# private Member using(__)

class Bank:

    def __init__(self):
        self.__balance = 10000

    def show_balance(self):
        print(self.__balance)

account = Bank()
account.show_balance()

#Getter Method

class Bank:

    def __init__(self):
        self.__balance = 10000

    def get_balance(self):
        return self.__balance

account = Bank()

print(account.get_balance())

#setter Method 

class Bank:

    def __init__(self):
        self.__balance = 10000

    def set_balance(self, amount):
        self.__balance = amount

    def get_balance(self):
        return self.__balance

account = Bank()
account.set_balance(25000)
print(account.get_balance())