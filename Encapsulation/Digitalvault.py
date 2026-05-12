class CredentialManager:
    def __init__(self,name,password):
        self.n=name
        self.__p=password
    @property
    def name(self):
        return self.__p
    @name.setter
    def name(self,value):
        old,new=value
        if self.__p==old:
            if len(new)>=8:
                self.__p=new
                print(f"password changed successfully from {old} to {self.__p}")
p1=CredentialManager("Praveen","Praveen#123")
print(f"Current password: {p1.name}")
old=input("Enter your old password:-")
new=input("Enter your new password:-")
p1.name=(old,new)