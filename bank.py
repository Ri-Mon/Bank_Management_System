class Account():
    list = []
    balance = 0 # initial total balance will be 0
    loan = 0 # initial total loan balance will be 0

    def __init__(self, name):
        self.name = name
        self.loan_count = 0 # 0 < maximum loan count <= 2  

class Bank():
    __admins = [] # private admin list
    __users = Account.list # private user list
    Bankrupt = False # initial bankrupt status = False
    
    def __init__(self, name):
        self.name = name
        self.loan_status = True
        
    def create_acc(self, acc):
        self.__users.append(acc)
    
    def is_bankrupt(self, st):
        Bank.Bankrupt = st

class General(Account): # class for general users
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.transactions = []

    def create_acc(self, name, mail, address, type):
        self.mail = mail
        self.address = address
        self.name = name
        account_num = f'{type}_{len(self.list) + 101}' # generating automatic account id
        print(f"NEW {type} ACCOUNT NAMED: {self.name} CREATED SUCCESSFULLY")
        self.list.append({account_num: self.name})
        return account_num

    def deposit(self, amount, admin_obj, Bank_obj): # accepting Admin object 'a', Bank object 'obj'
        if not admin_obj.check_Bmode(Bank_obj): # checking bankrupt mode
            if amount > 0:
                self.balance += amount
                Account.balance += amount
                self.transactions.append(f'DEPOSITED - TK{amount}')
                print(f"\n--> DEPOSITED TK{amount}.\n-> NEW BALANCE: TK{self.balance}")
            else:
                print("\n--> INVALID DEPOSITE AMOUNT. PROVIDE A VALID AMOUNT")
        else:
            print()
            print("CAN'T MAKE ANY TRANSACTION")
            print("THE BANK IS BANKRUPT")

    def withdraw(self, amount, adminObj, bankObj):
        if not adminObj.check_Bmode(bankObj): # checking bankrupt mode
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                Account.balance -= amount
                self.transactions.append(f'WITHDRAWN - TK{amount}')
                print(f"\n--> WITHDRAWN TK{amount}.\n-> NEW BALANCE: TK{self.balance}")
            else:
                print("\n--> WITHDRAWAL AMOUNT EXCEEDED. PROVIDE A VALID AMOUNT")
        else:
            print()
            print("CAN'T MAKE ANY TRANSACTION")
            print("THE BANK IS BANKRUPT")

    def check_balance(self): # checking balance of an instance of the General class
        print(f"Available Balance: TK{self.balance}")
    
    def transaction_history(self):
        for i, v in enumerate(self.transactions):
            print(f"{i+1}. {v}")
    
    def loan(self, amount, adminObj, bankObj):
        if not adminObj.check_Bmode(bankObj): # checking bankrupt mode
            if bankObj.loan_status: # checking loan status
                if self.loan_count < 2:
                    self.loan_count += 1
                    print()
                    print(f"LOAN REQUEST ACCEPTED FOR TK{amount}")
                    self.balance += amount
                    Account.loan += amount
                    print(f"NEW BALANCE: TK{self.balance}")
                    print()
                else:
                    print("YOU'VE EXCEEDED MAXIMUM POSSIBLE LOAN REQUEST")
                    print()
            else:
                print()
                print("SORRY, LOAN FEATURE IS CURRENTLY UNAVAILABLE")
                print()
        else:
            print()
            print("CAN'T TAKE ANY LOAN REQUEST")
            print("THE BANK IS BANKRUPT")
            print()

# checking account validity using name & accNumber for less complexity
    def balance_transfer(self, accNumber, amount, adminObj, bankObj): 
        if not adminObj.check_Bmode(bankObj): # checking bankrupt mode
            flag = False
            for d in self.list:
                if accNumber in d and amount <= self.balance and amount > 0:
                    print()
                    print(f'TRANSFERRING TK{amount} TO ACCOUNT: {accNumber}...')
                    self.transactions.append(f'TRANSFERRED - TK{amount}')
                    self.balance -= amount
                    
                    print(f'YOUR TRANSACTION IS SUCCESSFUL!!!')
                    print(f'CURRENT BALANCE = TK{self.balance}')
                    print()
                    flag = True
                    break
            if not flag:
                print()
                print("ACCOUNT DOESN'T EXIST. TRY AGAIN...")
                print()
        else:
                print()
                print("CAN'T MAKE ANY TRANSACTION")
                print("THE BANK IS BANKRUPT")
                print()
""" checking validity using account id only:
    def balance_transfer(accNumber, amount): 
        flag = false
        for d in list:
            for key,value in d.items():
                if accNumber == key:
                        print("OK")
                        flag = true
                        break
                if flag: break
"""
class Admin(Account):
    def __init__(self, name):
        super().__init__(name)
    
    def create_acc(self, name, mail, address, type):
        self.mail = mail
        self.address = address
        self.name = name
        self.account_num = f'{type}_{len(self.list) + 101}' # generating automatic account id
        print(f"NEW USER ACCOUNT NAMED:{self.name} TYPE:{type} CREATED SUCCESSFULLY ")
        self.list.append({self.account_num: self.name})
        return self.account_num
    
    def add_admin(self, name, mail, type):
        self.name = name
        self.mail = mail 
        account_num = f'{type}_{len(Bank._Bank__admins) + 505}' # generating automatic account id
        print(f"SUCCESSFULLY ADDED {self.name} AS AN ADMIN")
        Bank._Bank__admins.append({account_num: self.name})
        return account_num
        
    def view_users(self):
        for i, v in enumerate(self.list):
            for key, value in v.items():
                print(f"{i+1}. {value}: {key}")

    def remove_user(self, name, id):
        flag = False
        for i in self.list:
            for key, value in i.items():
                if name == value and id == key:
                    self.list.remove(i)
                    print(f'SUCCESSFULLY REMOVED USER WITH ACCOUNT ID: {id}')
                    flag = True
                    break
        if not flag:
                print('INVALID USER NAME OR ID')
                print('TRY AGAIN...')                    

    def balance_check(self):
        print(f"CURRENT AVAILABLE BANK BALANCE IS: TK{self.balance}")

    def loan_check(self):
        print(f"TOTAL ACCEPTED LOAN REQUESTS: TK{self.loan}")
    
    def check_Lstatus(self,st): # for checking current loan status
        s = st.loan_status
        return s

    def loan_feature(self, status, st): # for updating loan status
        if status:
            st.loan_status = True
            print()
            print("=) LOAN STATUS ENEABLED")
        else: 
            st.loan_status = False
            print()
            print("=) LOAN STATUS DISABLED")

    def check_Bmode(self, st): # for chceking bankrupt status
        s = st.Bankrupt
        return s 
    
    def bankrupt(self, status, st): # for disabling all transactions
        if status:
            st.Bankrupt = True 
            print()
            print("BANKRUPT MODE IS ENABLED")
            print("ALL TRANSACTIONS WILL BE OFF")
            print()
        else:
            st.Bankrupt = False
            print()
            print("BANKRUPT MODE IS DESABLED")
            print("NOW USERS CAN MAKE TRANSACTIONS")
            print()
