# Mini Project Create a Gym Member Management System.
#Fields:
#Name
#Age
#Plan
#Fee
class Gym :
    def __init__(self,name,age,plan,fee):
        self.name=name
        self.age=age
        self.plan=plan
        self.fee=fee

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("plan:",self.plan)
        print("fee:",self.fee) 
gym1=Gym("bala",45,"standed",1200)
gym1.display()

gym2=Gym("Boopathi",27,"preminum ",2000)
gym2.display()