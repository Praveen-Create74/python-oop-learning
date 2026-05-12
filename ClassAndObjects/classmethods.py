class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_string(cls,string):
        name,age=string.split(",")
        return cls(name,age)
new_std=Student.from_string("Praveen,21")
print(new_std.name)
print(new_std.age)
print(type(new_std))
class Expense:
    tax=0.05
    def __init__(self,amount):
        self.amount=amount
    @classmethod
    def update(cls,new_tax):
        tax=new_tax
        return tax
new_tax=Expense.update(0.06)
print(new_tax)
print(type(new_tax))