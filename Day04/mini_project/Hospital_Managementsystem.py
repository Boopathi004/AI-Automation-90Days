class Person:
    def __init__(self ,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
class Doctor(Person):
    def __init__(self, name, age,specification,experience):
        super().__init__(name, age)
        self.specification=specification
        self.experience=experience

    def display(self):
        super().display()
        print ("specification:",self.specification)
        print("expirience:",self.experience)

doct=Doctor("boopathi",28,"artho",2)
doct1=Doctor("mano",32,"child",3)
doct2=Doctor("sudha",40,"Gendral",10)

doct2.display()
doct.display()
doct1.display()



        
    