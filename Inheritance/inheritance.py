# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Child class
class Student(Person):
    def __init__(self, name, age, roll_number):
        # Call parent constructor
        super().__init__(name, age)
        self.roll_number = roll_number

    def show_info(self):
        # Override parent method
        print(f"Name: {self.name}, Age: {self.age}, Roll: {self.roll_number}")
p1 = Person("Alice", 30)
p1.show_info()   # Name: Alice, Age: 30

s1 = Student("Bob", 20, "A101")
s1.show_info()   # Name: Bob, Age: 20, Roll: A101
