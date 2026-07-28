class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def get_balance(self):
        return self.__salary  
    def set_balance(self,amount):
        if(amount>0):
          self.__salary=amount
        else:
         print("salery must be graterthen 0 ")

    def display(self):
         print("----------------------------")
         print("Name        :", self.name)
         print("Salary      :", self.__salary)
        
# instial salary
employee1=Employee("manoj",20000)
employee2=Employee("man",25000)
employee3=Employee("mani",30000)

# display 
print("Before updating the salary ")
employee1.display()
employee2.display()
employee3.display()
print("\n")

# Set salary
employee1.set_balance(30000)
employee2.set_balance(35000)
employee3.set_balance(40000)

# display 

print("after Updating the salary ")
employee1.display()
employee2.display()
employee3.display()
print("\n")

# Get Salary 
print("\nEmplyees salary ",employee1.get_balance())
print("\nEmplyees salary ",employee2.get_balance())
print("\nEmplyees salary ",employee3.get_balance())

        