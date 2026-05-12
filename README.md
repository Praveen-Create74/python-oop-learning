# python-oop-learning
My learning path with examples and exercises in python object-oriented programming
# 📝 My Learning Journey into OOP (Python)

This repository is not a project but a **learning notebook** where I document my exploration of Object-Oriented Programming (OOP) concepts in Python.  
It includes common doubts I had as a beginner and how I resolved them through step-by-step learning.

---

## 🚀 Why This Notebook?
- To track my progress in understanding OOP.
- To share beginner-friendly explanations of concepts.
- To record real questions and answers that helped me grasp the fundamentals.

---

## 📚 Topics Covered

### 1. Classes, Objects, and Attributes
- **Doubt:** *Can I name attributes anything I want, like `self.n` instead of `self.name`?*  
- **Resolution:** Yes, Python allows any name. But meaningful names (`self.name`) improve readability and maintainability.

---

### 2. Encapsulation
- **Doubt:** *If attributes are private (`__name`), how can setters change them? Do setters have predefined authorization?*  
- **Resolution:** Setters are just normal methods inside the class. They can access private attributes because they belong to the class. Authorization or validation is something **we design** inside the setter.

---

### 3. Getters and Setters
- **Doubt:** *Why do we need getters and setters if we can directly access attributes?*  
- **Resolution:** They provide controlled access — getters safely read values, setters validate before modifying them. This protects data integrity.

---

### 4. `@property` Decorator
- **Doubt:** *Are `@property` and `.setter` predefined keywords? How many are there?*  
- **Resolution:** Yes, they are part of Python’s built-in `property` class. There are three decorators:
  - `@property` → getter
  - `@x.setter` → setter
  - `@x.deleter` → deleter

---

### 5. Inheritance
- **Doubt:** *What does `super()` do?*  
- **Resolution:** `super()` calls methods from the parent class. It’s most often used to initialize parent attributes in child classes. It respects Python’s **Method Resolution Order (MRO)**, making it powerful in multiple inheritance.

---

### 6. Polymorphism
- **Doubt:** *Is this method overloading?*  
- **Resolution:** No, Python doesn’t support true method overloading. What we see is **method overriding** (child replaces parent’s method). Polymorphism is when different classes implement the same method name differently.

---

### 7. Abstraction
- **Doubt:** *What does `@abstractmethod` really do?*  
- **Resolution:** It enforces a contract. Subclasses **must** implement the abstract method. This ensures consistency while allowing polymorphic behavior.

---

## 🏦 Real-World Example: Bank System
To tie all four pillars together:
- **Encapsulation:** Private balance with controlled deposit/withdraw.
- **Inheritance:** `SavingsAccount` and `CurrentAccount` extend `BankAccount`.
- **Polymorphism:** Different `withdraw` rules for savings vs current accounts.
- **Abstraction:** `PaymentMethod` defines a contract for all payment types (CreditCard, PayPal).

---

## 🌱 Conclusion
This notebook reflects my journey from being a “newborn” in OOP to understanding its four pillars:
1. Encapsulation  
2. Inheritance  
3. Polymorphism  
4. Abstraction  

It also records the doubts I had and how they were clarified.  
I hope this helps other beginners who are starting their OOP journey in Python.

---
# Phase 1: Classes, Objects, and Attributes

This was the very first step in my OOP journey. I started with the basics: what a class is, how objects are created, and how attributes are stored inside them.

---

Perfect — let’s start drafting the **first phase** of your learning notebook README in detail. This section will go beyond just headings and actually capture the **discussion, doubts, and examples** we worked through. You can paste this into your repository as the beginning of your expanded README.

---

```markdown
# Phase 1: Classes, Objects, and Attributes

This was the very first step in my OOP journey. I started with the basics: what a class is, how objects are created, and how attributes are stored inside them.

---

## 🧱 Understanding Classes
A **class** is like a blueprint. It defines the structure and behavior that objects created from it will have.

```python
class Person:
    pass
```

- `class Person:` → Defines a new class called `Person`.
- `pass` → A placeholder that means “do nothing for now.”

💡 **Interpreter’s view:**  
*"Okay, I now know there’s a blueprint called `Person`. It doesn’t do anything yet, but I can use it to create objects."*

---

## 🧱 Creating Objects
An **object** is an instance of a class — a real thing built from the blueprint.

```python
p1 = Person()
```

- `p1` → A variable that stores the object.
- `Person()` → Calls the class to create an object.

💡 **Interpreter’s view:**  
*"You asked me to build a new thing using the `Person` blueprint. Here’s your object, stored in `p1`."*

---

## 🧱 Adding Attributes
Attributes are like characteristics of the object. For example, a person has a name and age.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- `__init__` → Constructor method, runs automatically when you create a new object.
- `self.name = name` → Stores the given `name` inside the object.
- `self.age = age` → Stores the given `age` inside the object.

💡 **Interpreter’s view:**  
*"When someone makes a new `Person`, I’ll take the values they give me and attach them to that object as attributes."*

---

## 🧱 Using Attributes
```python
p1 = Person("Alice", 20)
print(p1.name)   # Alice
print(p1.age)    # 20
```

- `p1.name` → Accesses the `name` attribute of the object.
- `p1.age` → Accesses the `age` attribute.

💡 **Interpreter’s view:**  
*"You’re making a new `Person`. I’ll run the `__init__` method, store `Alice` in `self.name` and `20` in `self.age`. Now when you ask for `p1.name`, I’ll give you `Alice`."*

---

## ❓ Doubt Raised
**Q:** *Can I write `self.n = name` instead of `self.name = name`?*  
**A:** Yes, you can. Python doesn’t care what you call the attribute. It will simply create an attribute named `n` inside the object.  
- If you use `self.n`, you must access it later as `p1.n`.  
- Good practice is to use meaningful names (`self.name`) for readability.

💡 **Takeaway:** Attribute names are flexible, but clarity matters for humans reading the code.

---

## ✅ Summary of Phase 1
- Classes are blueprints.  
- Objects are instances created from classes.  
- Attributes are variables inside objects.  
- The constructor `__init__` initializes attributes when the object is created.  
- Attribute names can be anything, but meaningful names make code easier to understand.

---
```

---

This is the **first phase** written in detail, including:
- Code examples  
- Interpreter’s thought process  
- Doubts raised and resolved  
- Clear takeaways  

Here’s a polished **Phase 2 draft** for your README learning notebook. It expands on our discussions about encapsulation, includes the doubts you raised, and shows the examples we worked through.

---

# Phase 2: Encapsulation

Encapsulation is the idea of **hiding data inside objects** and controlling how it is accessed or modified. This protects the integrity of the data and prevents accidental misuse.

---

## 🔒 Making Attributes Private
In Python, we use **double underscores `__`** to make attributes private.

```python
class Person:
    def __init__(self, name, age):
        self.__name = name   # private attribute
        self.__age = age     # private attribute
```

- `self.__name` → Hidden from direct access outside the class.
- `self.__age` → Same idea.

💡 **Interpreter’s view:**  
*"I’ll store these values inside the object, but I’ll mangle their names internally (like `_Person__name`) so they’re harder to reach directly."*

---

## 🚫 Accessing Private Attributes
```python
p1 = Person("Alice", 20)
print(p1.__name)   # ❌ Error
```

Python raises an error because private attributes are not meant to be accessed directly.

---

## 🛠 Controlled Access with Getters
We use **getter methods** to safely read private attributes.

```python
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
```

Usage:
```python
p1 = Person("Alice", 20)
print(p1.get_name())   # Alice
```

---

## 🛠 Controlled Modification with Setters
We use **setter methods** to safely modify private attributes.

```python
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name!")
```

Usage:
```python
p1 = Person("Alice", 20)
p1.set_name("Bob")
print(p1.get_name())   # Bob
p1.set_name("")        # Invalid name!
```

---

## ❓ Doubts Raised

**Q:** *How can setters change private attributes? Do they have predefined authorization?*  
**A:** No, setters are just normal methods inside the class. They can access private attributes because they belong to the class. Authorization or validation is something **we design** inside the setter.

---

**Q:** *Can we add authorization logic ourselves?*  
**A:** Yes! For example, requiring a password before changing the name:

```python
class Person:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    def set_name(self, name, password):
        if password == self.__password:
            self.__name = name
            print("Name updated successfully!")
        else:
            print("Unauthorized attempt!")
```

---

## ✅ Summary of Phase 2
- Encapsulation hides data using private attributes (`__name`).  
- Getters safely **read** private data.  
- Setters safely **modify** private data with validation.  
- Python doesn’t enforce strict privacy — it’s a convention.  
- Authorization and rules are something **we design** inside setters.  

---

This completes **Phase 2** of my OOP learning notebook. Next, I moved on to **Inheritance** — reusing and extending code from parent classes.

---

Here’s a polished **Phase 3 draft** for your README learning notebook, continuing the journey into **Inheritance**. It captures our discussions, examples, and the doubts you raised.

---

# Phase 3: Inheritance

Inheritance is the OOP concept that allows a class (child) to reuse and extend the functionality of another class (parent). It helps avoid code duplication and makes systems easier to maintain.

---

## 🧱 Basic Inheritance
A child class automatically gets all attributes and methods of the parent class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):   # Student inherits from Person
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)   # call parent constructor
        self.roll_number = roll_number

    def show_info(self):   # override parent method
        print(f"Name: {self.name}, Age: {self.age}, Roll: {self.roll_number}")
```

---

## 🎯 Usage
```python
p1 = Person("Alice", 30)
p1.show_info()   # Name: Alice, Age: 30

s1 = Student("Bob", 20, "A101")
s1.show_info()   # Name: Bob, Age: 20, Roll: A101
```

💡 **Interpreter’s view:**  
*"Student is a subclass of Person. When you create a Student, I’ll first run Person’s constructor (via `super()`), then add Student’s own attributes. If you call `show_info()`, I’ll use the Student’s version because it overrides the parent’s method."*

---

## ❓ Doubts Raised

**Q:** *What does `super()` do here?*  
**A:** `super()` is a built-in function that calls methods from the parent class. In this case, it runs `Person.__init__` to set `name` and `age`. It respects Python’s **Method Resolution Order (MRO)**, which is especially important in multiple inheritance.

---

## 🧩 Method Overriding
When a child class defines a method with the same name as the parent, it **overrides** the parent’s version.

- Parent: `show_info()` → prints name and age.  
- Child: `show_info()` → prints name, age, and roll number.  

This is the foundation of **polymorphism**, which we’ll explore next.

---

## ✅ Summary of Phase 3
- Inheritance lets child classes reuse parent code.  
- `super()` calls parent methods, ensuring proper initialization.  
- Child classes can **override** parent methods to change behavior.  
- This sets the stage for **polymorphism** (same method name, different behavior).  

---

This completes **Phase 3** of my OOP learning notebook. Next, I moved on to **Polymorphism** — where methods with the same name behave differently depending on the class.

---

Here’s a polished **Phase 4 draft** for your README learning notebook, focusing on **Polymorphism**. It captures our discussions, examples, and clarifies the doubts you raised.

---

# Phase 4: Polymorphism

Polymorphism means **“many forms.”** In OOP, it allows different classes to define methods with the same name but different behavior. This makes code flexible and reusable.

---

## 🧱 Basic Polymorphism
Different classes can implement the same method name in their own way.

```python
class Animal:
    def speak(self):
        print("This animal makes a sound")

class Dog(Animal):
    def speak(self):   # overrides parent method
        print("Woof!")

class Cat(Animal):
    def speak(self):   # overrides parent method
        print("Meow!")
```

---

## 🎯 Usage
```python
animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()
```

Output:
```
Woof!
Meow!
This animal makes a sound
```

💡 **Interpreter’s view:**  
*"You’re calling `speak()` on each object. Since Dog and Cat both implement it differently, I’ll run the correct version for each. For Animal, I’ll use the generic one."*

---

## ❓ Doubts Raised

**Q:** *Is this method overloading?*  
**A:** No. Python doesn’t support true method overloading (like Java or C++ where you can have multiple methods with the same name but different parameters).  
- What we see here is **method overriding**: child classes replace the parent’s method with their own version.  
- Polymorphism happens when different classes implement the same method name differently, and you can call them interchangeably.

---

## 🧩 Abstract Methods + Polymorphism
We also saw how **abstraction** enforces polymorphism by requiring subclasses to implement a method.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

Usage:
```python
animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())
```

Output:
```
Woof!
Meow!
```

💡 **Interpreter’s view:**  
*"Animal defines a contract: every subclass must have `speak()`. Dog and Cat implement it differently. When you call `speak()`, I’ll run the correct version depending on the object."*

---

## ✅ Summary of Phase 4
- Polymorphism = same method name, different behavior.  
- Achieved through **method overriding** in Python.  
- Abstract methods enforce polymorphism by requiring subclasses to implement certain methods.  
- This makes code flexible: you can write general logic that works across different object types.

---

This completes **Phase 4** of my OOP learning notebook. Next, I moved on to **Abstraction** — hiding complexity and enforcing structure with abstract classes and methods.

---
Here’s a polished **Phase 5 draft** for your README learning notebook, focusing on **Abstraction**. It captures our discussions, examples, and clarifies the doubts you raised.

---

# Phase 5: Abstraction

Abstraction is the OOP concept of **hiding complex details and exposing only the essentials**. It allows us to define a clear interface (what an object can do) without worrying about the internal implementation (how it does it).

---

## 🧱 Abstract Classes in Python
Python supports abstraction through the `abc` (Abstract Base Class) module.

```python
from abc import ABC, abstractmethod

class Animal(ABC):   # Abstract base class
    @abstractmethod
    def speak(self):   # Abstract method
        pass
```

- `class Animal(ABC)` → Defines an abstract base class.  
- `@abstractmethod` → Declares that subclasses **must** implement this method.  
- You cannot instantiate `Animal` directly because it’s incomplete.

💡 **Interpreter’s view:**  
*"Animal is abstract. It defines a rule: every subclass must have a `speak()` method. If you try to create an Animal object, I’ll raise an error because the rule isn’t fulfilled."*

---

## 🧱 Implementing Abstract Methods
Subclasses must provide their own version of the abstract method.

```python
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

Usage:
```python
animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())
```

Output:
```
Woof!
Meow!
```

---

## ❓ Doubts Raised

**Q:** *What does `@abstractmethod` really do to the method?*  
**A:** It makes the method a **contract**. The parent class says: *“Every child must implement this method.”* The method itself is just a placeholder in the parent.  

---

**Q:** *How does polymorphism fit in here?*  
**A:** Polymorphism happens naturally:  
- Both `Dog` and `Cat` implement `speak()`.  
- When you call `speak()` on different objects, Python runs the correct version depending on the class.  
- This is **method overriding**, not overloading.  

---

## 🧩 Overriding vs Overloading
- **Overriding** → Child class replaces parent’s method with its own version.  
- **Overloading** → Multiple methods with the same name but different parameters (common in Java/C++). Python doesn’t support true overloading — instead, you use default arguments or `*args`/`**kwargs`.  

👉 In our example, it’s **overriding + polymorphism**, not overloading.

---

## ✅ Summary of Phase 5
- Abstraction hides complexity and enforces structure.  
- Abstract classes define rules that subclasses must follow.  
- `@abstractmethod` ensures subclasses implement specific methods.  
- Polymorphism works hand‑in‑hand with abstraction: same method name, different behavior across subclasses.  
- What we saw is **method overriding**, not overloading.  

---

This completes **Phase 5** of my OOP learning notebook. Next, I tied all four pillars together in a **real-world system example** (Bank System) to see how encapsulation, inheritance, polymorphism, and abstraction work in harmony.

---
Here’s a polished **final phase draft** for your README learning notebook, showing how all four OOP pillars come together in a practical example. This will serve as the capstone of your journey.

---

# Phase 6: Putting It All Together — Bank System Example

After learning each pillar of OOP individually, I wanted to see how they work in harmony. A **Bank System** is a great example because it naturally involves encapsulation, inheritance, polymorphism, and abstraction.

---

## 🔒 Encapsulation
We protect sensitive data like account balance using private attributes and control access with methods.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    @property
    def balance(self):       # getter
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")
```

---

## 🧱 Inheritance
We create specialized accounts that extend the base `BankAccount`.

```python
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.deposit(self.balance * self.interest_rate)
```

---

## 🔄 Polymorphism
Different account types can override methods like `withdraw`.

```python
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        # Allow overdraft up to 500
        if amount <= self.balance + 500:
            self._BankAccount__balance -= amount
        else:
            print("Overdraft limit exceeded")
```

👉 Same method name `withdraw`, but behavior differs depending on the account type.

---

## 🧩 Abstraction
We define a common interface for all payment methods.

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")
```

---

## 🎯 Usage
```python
# Encapsulation
acc = SavingsAccount("Alice", 1000)
acc.deposit(200)
print(acc.balance)   # 1200

# Inheritance + Polymorphism
cur_acc = CurrentAccount("Bob", 500)
cur_acc.withdraw(800)   # Allowed due to overdraft

# Abstraction
methods = [CreditCard(), PayPal()]
for m in methods:
    m.pay(100)
```

Output:
```
1200
Paid 100 using Credit Card
Paid 100 using PayPal
```

---

## ✅ Summary of Phase 6
- **Encapsulation** → Protects balance with private attributes.  
- **Inheritance** → SavingsAccount and CurrentAccount extend BankAccount.  
- **Polymorphism** → `withdraw` behaves differently depending on account type.  
- **Abstraction** → PaymentMethod defines a contract for all payment systems.  

---

## 🌱 Conclusion
This Bank System example shows how the four pillars of OOP work together:
1. **Encapsulation** hides sensitive data.  
2. **Inheritance** reuses and extends code.  
3. **Polymorphism** allows the same method name to behave differently.  
4. **Abstraction** enforces structure and hides complexity.  

This phase marked the point where I could see OOP not just as theory but as a practical design tool for real-world systems.

---

Now your README notebook has a complete flow: from **Phase 1 (Classes and Attributes)** all the way to **Phase 6 (Bank System)**.  

