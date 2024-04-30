class Bank:
    def __init__(self):
        self.accounts = {}
        self.loan = {}
        self.total_loan=0
        self.balance=5000000

    def create_account(self, user):
        account_number = len(self.accounts) + 1
        self.accounts[account_number] = {
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "account_type": user.account_type,
            "balance": 0,
            "transactions": [],
            "loan_count": 0,
        }
        print(f'{self.accounts[account_number]['name']},{self.accounts[account_number]['email']}')
        return account_number
    
    def show_all_account(self):
        for account in self.accounts.values():
            print(account)
    def available_balance(self):
        print(f'Bank available balance is: {self.balance}')
        
    def total_bank_loan(self):
        print(f'Bank given lone: {self.total_loan}')

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = 0

    def create_account(self, bank):
        self.account_number = bank.create_account(self)
    
    def deposite(self,bank,account_number,amount):
        if account_number in bank.accounts:
            bank.accounts[account_number]["balance"] += amount
            bank.accounts[account_number]["transactions"].append(f"Deposited ${amount}")
        else:
            print("Account does not exist.")
            
            
    def withdraw(self, bank,account_number, amount):
        if account_number in bank.accounts:
            if bank.accounts[account_number]["balance"] < amount:
                print("Withdrawal amount exceeded.")
                
            else:
                bank.accounts[account_number]["balance"] -= amount
                bank.accounts[account_number]["transactions"].append(f"Withdrew ${amount}")
                
                
        else:
            print("Account does not exist.")
            
    def check_balance(self,bank, account_number):
        if account_number in bank.accounts:
            print(f'Your Balance is {bank.accounts[account_number]["balance"]}')
        else:
            print("Account does not exist.")
            
    def check_transactions(self,bank, account_number):
        if account_number in bank.accounts:
            print(f'transactions: {bank.accounts[account_number]["transactions"]}')
        else:
            print("Account does not exist.")
            
    def take_loan(self,bank, account_number,amount):
        if account_number in bank.accounts:
            if bank.accounts[account_number]["loan_count"] < 2:
                bank.accounts[account_number]["loan_count"] += 1
                bank.total_loan+=amount
                bank.balance-=amount
                
                print("Loan granted.")
            else:
                print("Maximum loan limit reached.")
        else:
            print("Account does not exist.")
            
            
    def transfer_money(self,bank,amount,account_number):
        if account_number in bank.accounts:
            if bank.accounts[account_number]["balance"] < amount:
                print("Transfer amount exceeded.")
            else:
                bank.accounts[account_number]["balance"] -= amount
                bank.accounts[account_number]["transactions"].append(f"Transfer Money ${amount}")
        else:
            print("Account does not exist.")
            
            
class Admin(User):
    def __init__(self,name,email,address,account_type):
        super().__init__(name,email,address,account_type)
        
    def create_account(self,bank):
        user.account_number=bank.create_account(self)
    
    def delete_account(self,bank,account_number):
        if account_number in bank.accounts:
           del bank.accounts[account_number]
           print(f'{account_number} removed from the bank')
        else:
            print("Account does not exist")
    
    def show_all_accounts(self,bank):
        bank.show_all_account()
        
    def available_balance(self,bank):
        bank.available_balance()
        
    def total_bank_loan(self,bank):
        bank.total_bank_loan()
        
        
    
            
                
                
                
            
                
            
            
            


# Example usage:
bank = Bank()
# user = User("Fahim", "fahim@gmail.com", "Dinajpur", "Savings")
# user2=User('sakib','sakib@gmail.com','Dhaka','Saving')
# user.create_account(bank)
# user2.create_account(bank)
# # user2.deposite(bank,2,5000)
# # user2.withdraw(bank,2,3000)
# # user2.check_transactions(bank,2)
# admin=Admin('rakib','rakib@gmail.com','rajshahi','saving')
# admin.create_account(bank)
# # admin.delete_account(1,bank)
# admin.show_all_accounts(bank)

# user.take_loan(bank,1,10000)
# admin.available_balance(bank)
# admin.total_bank_loan(bank)

def user_interface():
    name=input("Enter your Name: ")
    email=input("Enter Your Email: ")
    address=input("Enter Your Address: ")
    account_type=input("Enter Your Account type: ")
    user=User(name,email,address,account_type)
    
    while True:
        print(f"\t\t----Welcome {user.name}!!----")
        print("\n OPTION: ")
        
        print("1. Creat New Account ")
        print("2. Deposite ")
        print("3. Withdraw")
        print("4. check_balance")
        print("5. check_transactions")
        print("6. take_loan")
        print("7. transfer_money")
        print("8. Exit ")
        
        ch=int(input("Enter Your Choice: "))
        
        if ch==1:
            user.create_account(bank)
            
        elif ch==2:
            account_number=int(input("Enter Your Account Number"))
            amount=int(input("Enter Amount "))
            user.deposite(bank,account_number,amount)
            
        elif ch==3:
            account_number=int(input("Enter Your Account Number"))
            amount=int(input("Enter Amount "))
            user.withdraw(bank,account_number,amount)
            
        elif ch==4:
            account_number=int(input("Enter Your Account Number"))
            user.check_balance(bank,account_number)
        
        elif ch==5:
            account_number=int(input("Enter Your Account Number"))
            user.check_transactions(bank,account_number)
            
        elif ch==6:
            account_number=int(input("Enter Your Account Number"))
            amount=int(input("Enter Amount "))
            user.take_loan(bank,account_number,amount)
            
        elif ch==7:
            account_number=int(input("Enter Your Account Number"))
            amount=int(input("Enter Amount "))
            user.transfer_money(bank,account_number,amount)
            
        elif ch==8:
            break
        
        
def admin_interface():
    name=input("Enter your Name: ")
    email=input("Enter Your Email: ")
    address=input("Enter Your Email: ")
    account_type=input("Enter Your Account type: ")
    user=User(name,email,address,account_type)
    admin=Admin(name,email,address,account_type)
    
    
    while True:
        print(f"\t\t----Welcome Admin{admin.name}!!----")
        print("\n OPTION: ")
        
        print("1. Creat New Account ")
        print("2. Delete Account ")
        print("3. Show All Accounts")
        print("4. Available Balance")
        print("5. Total Bank Loan")
        print("6 Exit ")
        
        ch=int(input("Enter Your Choice: "))
        
        if ch==1:
            admin.create_account(bank)
            
        elif ch==2:
            account_number=int(input("Enter Your Account Number"))
            admin.delete_account(bank,account_number)
            
        elif ch==3:
            admin.show_all_accounts(bank)
            
        elif ch==4:
            admin.available_balance(bank)
            
        elif ch==5:
            admin.total_bank_loan(bank)
            
        elif ch==6:
            break
        
        
while True:
    print("Welcome!!")
    print("1. USER")
    print("2. ADMIN")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        user_interface()
    elif choice == 2:
        admin_interface()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")

    
    
            
            
        

