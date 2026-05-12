class bankmanagement:
    def __init__(self,name,balance,password):
        self.name=name
        self.__balance=balance
        self.__password=password
    def deposit(self,amount,password):
        self.amount=amount
        if password==self.__password and amount>0:
            self.__balance+=self.amount
        return "deposited successfully from {self.amount} to {self.__balance}"
    def withdraw(self,amount,password):
        if amount<=self.__balance:
            self.amount=amount
            if password==self.__password:
                self.__balance-=self.amount
            return "wtihdraw succesfully from {self.amount} to {self.__balance}"
        else:
            return "insufficient balance"
    @property
    def check_balance(self):
        return self.__balance
check=bankmanagement("praveen",10000,"Praveen123")
print(check.deposit(1000,"Praveen123"))
print(check.withdraw(500,"Praveen123"))
print(check.check_balance)


