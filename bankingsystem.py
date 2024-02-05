# basing abnking system using  
# 1.basic OOPS
# 2.CRUD

# entities and their behavious
# bank:
#     -bank should contain all accounts
#     -we should be able to fetch an account using acc. number
#     -bank should be able to delete and add account using account number

# account:
#     -every account should have a account no. and balance
#     -we should be able to withdear and deposite money in the account

# customer:
#     -a customer can have multiple accounts , he should also have a name
#     -a customer should be able to add acc to his name.

class bank:
    def __init__(self):
        self.all_accounts={}
    
    def get_account(self,acc_no):
        return self.all_accounts[acc_no] #returning acc from list based on acc no.

    def add_account(self,account):
        self.all_accounts[account.acc_no]=account

    def del_account(self,acc_no):
        del self.all_accounts[acc_no]

class account:
    def __init__(self,acc_no,initial_balance):
        self.acc_no=acc_no
        self.balance=initial_balance
        print(f"Account initiated- account number {acc_no}, balance {initial_balance}")

    def deposite(self,amount):
        self.balance +=amount
        print(f"{amount} deposited. cuttent balance = {self.balance}")

    def withdraw(self,amount):
        if self.balance < amount:
            print("insufficient bamance")
            return
        else:
            self.balance -=amount
            print(f"{amount} withdrawn. cuttent balance = {self.balance}")

class customer:
    def __init__(self,name):
        self.name=name
        self.my_accounts={}

    def add_account(self,account):
        self.my_accounts[account.acc_no]=account

    def get_account(self,acc_no):
        return self.my_accounts[acc_no]
    
hdfc=bank() #initialise the bank
account1=account(111,100)#creating 1st account
account2=account(222,200)#creating 2nd account

hdfc.add_account(account1) #added account to the bank
hdfc.add_account(account2) #added account to the bank

customer1=customer("tanmay") #initialise the customer

customer1.add_account(account1) #assign account1 to the customer
customer1.add_account(account2) #assign account2 to the same customer

account=customer1.get_account(111)
if account:
    account.deposite(50)
    account.withdraw(30)


