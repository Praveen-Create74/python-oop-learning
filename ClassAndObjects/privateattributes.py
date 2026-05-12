class Person:
    def __init__(self, name, age):
        self.__name = name   # private attribute
        self.__age = age     # private attribute

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, new_name):
        self.__name = new_name
obj=Person("Praveen",21)
print(obj.get_name())
print(obj.get_age())
'''self.__name → The double underscore tells Python: “This attribute should not be accessed directly from outside the class.”

self.__age → Same idea.

Interpreter’s logic:
“I’ll store these values inside the object, but I’ll mangle their names internally (like _Person__name) so they’re harder to reach directly.'''

'''p1 = Person("Alice", 20)
print(p1.__name)   # ❌ Error: Attribute not found
The interpreter says: “You’re asking for __name, but that doesn’t exist in the public view of this object.”

Internally, it’s stored as _Person__name, but you’re not supposed to touch it directly.

👉 This is the data hiding part of encapsulation.'''