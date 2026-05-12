class student:
    def __inti__(self,name,age):
        self.name=name
        self.age=age
    def about(self):
        print(f"{self.name} age is {self.age}")
a=student()
b=student()
name=input("Enter your name:-")
age=int(input("Enter your age:-"))
a.about(name, age)
b.about(name, age)
