class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):   # setter
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name!")

    def get_name(self):
        return self.__name
obj=Person("Praveen",21)
print(obj.get_name())
'''In Python, “private” attributes (like __name) are not truly locked away. They’re just name-mangled — meaning Python renames them internally (e.g., self.__name becomes self._Person__name).

This makes them harder to access directly from outside the class, but inside the class methods (like setters), you still have full access to them'''
'''interpreter logic:-
You’re inside the class, so you’re allowed to touch __name.”

“I’ll update the hidden attribute _Person__name with the new value.”'''
'''
why setters used?
They let you add rules (e.g., only allow positive ages, only allow non-empty names).

They make your code cleaner and safer by centralizing how attributes are changed.

They signal to other programmers: “Don’t mess with this attribute directly — use the setter.”'''
