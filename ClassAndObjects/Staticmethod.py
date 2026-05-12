class User:
    def __init__(self,name,age,password):
        self.name=name
        self.age=age
        self.password=password
    @staticmethod
    def is_secure(password):
        return len(password)>8
new_User=User("Praveen",21,"123456789")
print(new_User.is_secure(new_User.password))
print(User.is_secure(new_User.password))
print(type(new_User))
