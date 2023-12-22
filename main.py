from bank import *

print()

def main():

    bank = Bank('THE PYTHON')
    g = General('STUDENTS OF PHITRON')
    admin = Admin('PHITRON')

    print()
    print("**********************WELCOME TO THE ''BANK PYTHON''************************\n")
    while(True):
        print("ACCOUNT PANEL: ")
        print()
        print("1. GENERAL PANEL (FOR USERS ONLY)")
        print("2. ADMIN PANEL (FOR ADMINS ONLY)")
        print()
        choice = int(input("ENTER YOUR PREFERRED CHOICE: "))
        if choice == 1: 
            while(True):
                print()
                print("*******************WELCOME TO USER'S PANEL*********************\n")
                print("1. Don't Have An Account? REGISTER")
                print("2. Already Have An Account? LOGIN")
                print("3. GO TO THE ACCOUNT PANEL")
                print()
                ch = input("ENTER YOUR PREFERRED CHOICE (R/L/G): ")

                if ch == "R" or ch == 'r':
                    print()
                    print("*****************WELCOME TO USER'S REGISTER PANEL********************\n")
                    n = input("ENTER YOUR NAME: ")
                    m = input("ENTER YOUR MAIL ADDRESS: ")
                    adrs = input("ENTER YOUR ADRESS: ")
                    t = input("ENTER YOUR PREFERRED ACCOUNT TYPE (SAVINGS/ CURRENT): ")
                    print("----------------------------------------------------")
                    print(f"YOUT ACCOUNT ID is : {g.create_acc(n, m, adrs, t)}")
                    print("NOW CHOOSE LOGIN TO CONTINUE WITH YOUR PROFILE")
                    print("----------------------------------------------------")

                elif ch == "L" or ch == 'l': 
                    print()
                    print("*******************WELCOME TO LOGIN PANEL*******************\n")
                    u = input("ENTER USER'S NAME: ")
                    id = input("ENTER USER'S ACCOUNT ID: ")
                    print()
                    flag = False
                    while(True):
                        for j in g.list:
                            for key, value in j.items():
                                if key == id and value == u: # checking account validity
                                    flag = True 
                                    while(True):
                                        print("---------------------------------------------------------")
                                        print("ACCOUNT OPTIONS: ")
                                        print("1. CREATE NEW ACCOUNT")
                                        print("2. DEPOSIT MONEY")
                                        print("3. WITHDRAW MONEY")
                                        print("4. VIEW TRANSACTION HISTORY") 
                                        print("5. REQUEST LOAN")
                                        print("6. TRANSFER BALANCE")
                                        print("7. CHECK BALANCE")
                                        print("8. LOGOUT")
                                        print("---------------------------------------------------------")
                                        a = int(input("ENTER YOUR PREFERRED ACTION: "))
                                        if a == 1:
                                            print("--------------------------------------------")
                                            n = input("ENTER USER'S NAME: ")
                                            m = input("ENTER USER'S MAIL ADDRESS: ")
                                            adrs = input("ENTER USER'S ADDRESS: ")
                                            t = input("ENTER USER'S PREFERRED ACCOUNT TYPE (SAVINGS/ CURRENT): ")
                                            print()
                                            print(f"USER ACCOUNT ID IS : {g.create_acc(n, m, adrs, t)}")
                                            print("--------------------------------------------")
                                        elif a == 2:
                                            print('.............................................')
                                            d = int(input("ENTER THE AMOUNT TO BE DEPOSITED: "))
                                            g.deposit(d, admin, bank)
                                            print('.............................................')
                                            
                                        elif a == 3:
                                            print('.............................................')
                                            w = int(input("ENTER THE AMOUNT OF WITHDRAWAL: "))
                                            g.withdraw(w, admin, bank)
                                            print('.............................................')

                                        elif a == 4:
                                            print('.............................................')
                                            g.transaction_history()
                                            print('.............................................')

                                        elif a == 5:
                                            print('.............................................')
                                            l = int(input("ENTER YOUR PREFFERRED LOAN AMOUNT: "))
                                            g.loan(l, admin, bank)
                                            print('.............................................')

                                        elif a == 6:
                                            print('.............................................')
                                            i = input("ENTER RECEIVER'S ACCOUNT ID: ")
                                            a = int(input("ENTER THE AMOUNT TO BE TRANSFERRED: "))
                                            g.balance_transfer(i, a, admin, bank)
                                            print('.............................................')
                                        
                                        elif a == 7:
                                            print()
                                            g.check_balance()
                                            print()

                                        elif a == 8:
                                            print('.............................................')
                                            print("ACCOUNT LOGOUT SUCCESSFUL")
                                            print('.............................................')
                                            break
                                        else:
                                            print()
                                            print("INVALID ACTION!!! TRY AGAIN...")
                                            print()
                        if not flag:
                            print()
                            print("YOUR PROVIDED INFORMATION DOESN'T EXISTS")
                            print("TRY RE-CHECKING YOUR GIVEN INFORMATION")
                            print("OR")
                            print("IF YOU DON'T HAVE ANY USER ACCOUNT, PLEASE REGESTER FIRST!!!")
                            print()
                        else:
                             break
                elif ch == "G" or ch == "g":
                     break
                else:
                    print()
                    print("INVALID CHOICE!!! TRY AGAIN...")
                    print()

        elif choice == 2: 
            print()
            print("WELCOME TO ADMIN'S LOGIN PANEL")
            print()
            while(True):
                print("1. NEW ADMIN REGISTER")
                print("2. ADMIN LOGIN")
                print("3. GO TO ACCOUNT PANEL")
                print()
                op = int(input("ENTER YOUR PREFERRED CHOICE: "))
                if op == 1:
                    print("------------------------------------------------------------")
                    print()
                    n = input("PROVIDE YOUR NAME: ")
                    m = input("ENTER YOUR MAIL ADDRESS: ")
                    t = input("ENTER YOUR ACCOUNT TYPE AS ADMIN: ")
                    print()
                    aID = admin.add_admin(n, m, t) # NEW ADMIN REGISTRATION
                    print(f"YOUR ADMIN ACCOUNT ID IS : {aID}")
                    print("NOW GO TO THE ADMIN LOGIN PANEL AND CHOOSE LOGIN TO CONTINUE WITH YOUR ADMIN ACCOUNT")
                    print()
                    print("------------------------------------------------------------") 
                elif op == 2:
                    while(True):
                        id = input("ENTER YOUR ADMIN ID FOR SECURING THE PROCESS: ")
                        flag = False # for inner for loop
                        for v in bank._Bank__admins:
                            if id in v.keys():
                                flag = True 
                                flg = False # for inner while loop
                                while(True):
                                    flg = True
                                    print()
                                    print(f">>>>>>>>>>>>>>>>>>>>>WELCOME {v[id]} SIR<<<<<<<<<<<<<<<<<<<<\n") 
                                    print("---------------------------------------")                   
                                    print("1. CREATE NEW USER'S ACCOUNT")
                                    print("2. CHECK USERS LIST")
                                    print("3. DELETE AN USER ACCOUNT")
                                    print("4. LOAN FLOW CONTROL") 
                                    print("5. CHECK TOTAL BALANCE")
                                    print("6. CHECK TOTAL LOAN")
                                    print("7. BANKRUPT MODE")
                                    print("8. LOGOUT")
                                    print("---------------------------------------")
                                    a = int(input("ENTER YOUR PREFERRED OPTION: "))
                                    if a == 1:
                                        print("........................................................")
                                        n = input("ENTER USER'S NAME: ")
                                        m = input("ENTER USER'S MAIL ADDRESS: ")
                                        adrs = input("ENTER USER'S CURRENT ADDRESS: ")
                                        t = input("ENTER USER'S ACCOUNT TYPE (SAVINGS/ CURRENT): ")
                                        print()
                                        
                                        print(f" USER'S ACCOUNT ID IS : {admin.create_acc(n, m, adrs, t)}")
                                        print()
                                        print("........................................................")
                                            
                                    elif a == 2:
                                            print("........................................................")
                                            print()
                                            admin.view_users()
                                            print()
                                            print("........................................................")
                                    elif a == 3:
                                            print("........................................................")
                                            n = input("ENTER USER'S NAME: ")
                                            i = input("ENTER USER'S ID: ")
                                            admin.remove_user(n, i)
                                            print("........................................................")

                                    elif a == 4:
                                            print("........................................................")
                                            if admin.check_Lstatus(bank):
                                                print("CURRENT LOAN STATUS IS ON")
                                                c =  input("WANT TO TURN OFF THE FEATURE? Y/N: ")
                                                if c == 'Y' or c == 'y':
                                                    admin.loan_feature(False, bank)
                                            
                                            else:
                                                print("CURRENT LOAN STATUS IS OFF")
                                                c =  input("WANT TO TURN ON THE FEATURE? Y/N: ")
                                                if c == 'Y' or c == 'y':
                                                    admin.loan_feature(True, bank)
                                            print("........................................................")

                                    elif a == 5:
                                            print("....................................")
                                            admin.balance_check()
                                            print("....................................")
                                    elif a == 6:
                                            print("....................................")
                                            admin.loan_check()
                                            print("....................................")
                                    
                                    elif a == 7:
                                        print("........................................................")
                                        if admin.check_Bmode(bank):
                                            print("BANKRUPT MODE IS ON")
                                            c =  input("DISABLE BANKRUPT MODE? Y/N: ")
                                            if c == 'Y' or c == 'y':
                                                admin.bankrupt(False, bank)
                                        else:
                                            print("BANKRUPT MODE IS OFF")
                                            c =  input("ENABLE BANKRUPT MODE? Y/N: ")
                                            if c == 'Y' or c == 'y':
                                                admin.bankrupt(True, bank)
                                        print("........................................................")
                                        
                                    elif a == 8:
                                            print("....................................")
                                            print()
                                            print("ACCOUNT LOGOUT SUCCESSFUL")
                                            print()
                                            print("....................................")
                                            flg = False
                                            break
                                    else:
                                            print("....................................")
                                            print("INVALID ACTION. TRY AGAIN...")
                                            print("....................................")
                                if not flg:
                                    break
                            
                        if not flag: 
                            print("....................................")
                            print("NO ADMIN ACCOUNT FOUND")
                            print("TRY RECHECKING YOUR INFORMATION")
                            print("....................................")
                        break
                elif op == 3:
                     print()
                     break 
                else:
                    print("....................................")
                    print("INVALID CHOICE. TRY AGAIN...")
                    print("....................................")      
        else:
            print("....................................")
            print("INVALID CHOICE. TRY AGAIN...")
            print("....................................")

if __name__ == '__main__': # calling main function
    main()


