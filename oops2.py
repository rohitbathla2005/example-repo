class Account():
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,dp_amount):
        self.balance =  self.balance + dp_amount
        print( f"added {dp_amount} to balance")

    def withdrawal(self, wd_amount):
        if self.balance >= wd_amount:
            self.balance = self.balance - wd_amount
            print(f"deduct {wd_amount} from balance")
        else:
            print("sorry")
    def __str__(self):
        return f" owner name{self.owner} balance {self.balance}"
a = Account('rohit')
print(a)
y = int(input("press 1 for deposit 2 for withdrawl"))

x = int(input("enter amount"))
if y == 1:
    a.deposit(x)
    print(a)
elif y==2:
    a.withdrawal(x)
    print(a)