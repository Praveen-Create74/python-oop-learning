class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    @property
    def balance(self):       # getter
        return self.__balance

    def deposit(self, amount):  # setter-like method
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount): # setter-like method
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.deposit(self.balance * self.interest_rate)
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        # Allow overdraft up to 500
        if amount <= self.balance + 500:
            self._BankAccount__balance -= amount
        else:
            print("Overdraft limit exceeded")
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
