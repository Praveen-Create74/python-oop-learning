class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):   # getter
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, new_name):
        self.__name = new_name
p1=Person("Praveen",21)
print(p1.get_name())
print(p1.get_age())
'''def get_name(self): → Defines a method.

return self.__name → Gives back the private value safely.

Interpreter’s thought:
“Okay, if someone calls get_name(), I’ll fetch the hidden __name and return it.”'''