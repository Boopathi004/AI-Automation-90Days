#Mutiple level inheritance 
class Animal:

    def sound(self):
        print("Animals make sounds")

class Dog(Animal):

    def bark(self):
        print("Dog barks")

class Puppy(Dog):

    def play(self):
        print("Puppy is playing")

puppy = Puppy()

puppy.sound()
puppy.bark()
puppy.play()

# Multiple Inheritance 
'''Parent1      Parent2
     \        /
      \      /
        Child 
'''
class Father:

    def skills(self):
        print("Programming")

class Mother:

    def hobbies(self):
        print("Painting")

class Child(Father, Mother):
    pass
child = Child()

child.skills()
child.hobbies()

#hirachial inheritance 
'''
        Vehicle
       /       \
     Car      Bike
'''
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


car = Car()
bike = Bike()

car.start()
bike.start()

#Method overriding 

class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Dog Barks")

dog = Dog()
dog.sound()

#Use of Super Keyword 

class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog Barks")
dog = Dog()
dog.sound()