class Animal:
    def speak(self):
        print("This animal makes a sound")

class Dog(Animal):
    def speak(self):   # overrides parent method
        print("Woof!")

class Cat(Animal):
    def speak(self):   # overrides parent method
        print("Meow!")
animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()
