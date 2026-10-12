print("Create a class without constructor")
class Account():
    #attributes or properties
    actnum=0
    name=" "
    bank=" "
    branch=" "
    balance=0
    def createAccount(self,actnum,name,bank,branch):
        self.actnum=actnum
        self.name = name
        self.bank = bank
        self.branch = branch
        print("Your account creation is successful")
    def deposit(self,actnum,amttodeposit):
        if (self.actnum ==actnum):
            self.balance = self.balance + amttodeposit
        print("Your account is deposited with ",amttodeposit)
        print("Your latest balance is ",self.balance)

    def withdraw(self,actnum,amttowithdraw):
        if (self.actnum ==actnum):
            self.balance = self.balance - amttowithdraw
        print("Your account is withdrawn with ",amttowithdraw)
        print("Your latest balance is ",self.balance)

print("Create account")
act1 = Account()
act1.createAccount(1,"raghu","ICICI","Marathahalli")
act1.deposit(1,10000)
act1.deposit(1,20000)
act1.withdraw(1,5000)




        
