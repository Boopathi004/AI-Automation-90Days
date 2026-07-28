class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name :", self.name)
        print("Salary :", self.salary)


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department :", self.department)


manager = Manager("Boopathi", 80000, "AI Automation")

manager.display()