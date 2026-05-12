'''1. A class in Python is like a blueprint. Imagine you want to build houses — the class is the design plan, and each house you build from it is an object.

python
class Person:
    pass
class Person: → This defines a new class called Person.

pass → A placeholder that means “do nothing for now.” It keeps the class valid even though it has no content yet.

👉 The interpreter sees this and says: “Okay, I now know there’s a blueprint called Person.'''
'''2. An object is an actual thing created from the class blueprint.

python
p1 = Person()
p1 → A variable that stores the object.

Person() → Calls the class to create an object.

The interpreter says: “You asked me to build a new thing using the Person blueprint. Here’s your object, stored in p1.”'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
'''Line by line:

def __init__(self, name, age): → This is a constructor method. It runs automatically when you create a new object.

self → Refers to the current object being created.

self.name = name → Stores the given name inside the object.

self.age = age → Stores the given age inside the object.

👉 Interpreter logic: “When someone makes a new Person, I’ll take the values they give me and attach them to that object as attributes.”'''
p1 = Person("Alice", 20)
print(p1.name)   # Alice
print(p1.age)    # 20
''''Person("Alice", 20) → Creates a new person with name "Alice" and age 20.

p1.name → Accesses the name attribute of the object.

p1.age → Accesses the age attribute.

Interpreter’s thought process:

“You’re making a new Person. I’ll run the __init__ method.”

“Store Alice in self.name and 20 in self.age.”

“Now, when you ask for p1.name, I’ll give you Alice.”'''