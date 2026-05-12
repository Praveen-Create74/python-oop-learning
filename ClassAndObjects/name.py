'''if you write self.name the attribute name will be created inside the p1 object
so you can write the name in anyway like self.n it won't be a problem but
we write self.name to give a meaningful name to the attribute.'''
class Person:
    def __init__(self, name, age):
        self.n = name
        self.age = age
obj=Person("Praveen",21)
print(obj.n)
print(obj.age)