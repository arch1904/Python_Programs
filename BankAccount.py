class BankAccount:
    def __init__(self,x,y,z,a,b):
        self.accountno=x
        self.name=y
        self.balance=z
        self.depositamount=a
        self.withdrawamount=b
    def deposit(self,x):
        self.depositamount=x
        self.balance+=self.depositamount
    def withdraw(self,x):
        self.withdrawamount=x
        self.balance-=self.withdrawamount
    def enter(self):
        self.name=input("Enter Name ")
        self.accountno=input("Enter Account No ")
    def display(self):
        print("Name ",self.name)
        print("Account No ",self.accountno)
        print("Balance ",self.balance)
obj=BankAccount(0,'',0,0,0)
obj.enter()
c='y'
while c=='y':
    print("To Deposit Enter 1 ")
    print("To Withdraw Enter 2 ")
    print("To Display Enter 3 ")
    print("To Exit Enter 4 ")
    i=int(input())
    if i==1:
        x=int(input("Enter Amount To Be Deposited "))
        obj.deposit(x)
    elif i==2:
        x=int(input("Enter Amount To Be Withdrawn "))
        obj.withdraw(x)
    elif i==3:
        obj.display()
    elif i==4:
        break
    c=input("Do You Want to Continue? ")
