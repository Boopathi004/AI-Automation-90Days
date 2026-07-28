#Method overriding 

class Animal:

    def sound(self):
        print("Animals make sounds")

class Dog(Animal):

    def sound(self):
        print("Dog Barks")

class Cat(Animal):

    def sound(self):
        print("Cat Meows")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

#polymarpisam Using diffrent object 
class Car:

    def move(self):
        print("Car is Driving")

class Plane:

    def move(self):
        print("Plane is Flying")
class Boat:

    def move(self):
        print("Boat is Sailing")
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()


#DuckTyping in python 

class Dog:

    def speak(self):
        print("Dog Barks")

class Cat:

    def speak(self):
        print("Cat Meows")

def animal_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)

#Metord overloading 

print(10 + 20)
print("AI " + "Automation")
print([1,2] + [3,4])