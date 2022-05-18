import functions
#---------------------------------------------------------------------------------
def index_non_ac_holder():
    print('''
        1) Create account
        2) About us

        Press any other key to exit.
        ''')
def non_ac_holder():
    x='1'
    while(x=='1'):
        choice=input("What would you like to do(Enter i for index)\nSelect option: ")
        if(choice=='1'):
            n=functions.create_ac()
            print("\nAccount created successfully ...")
            print(n)
            x=functions.cont()
            index_ac_holder()
            ac_holder(n)
        elif(choice=='2'):
            functions.aboutus()
            x=functions.cont()
        elif(choice=='i' or choice=='I'):
            index_non_ac_holder()
            non_ac_holder()
        else:
            return None
#-----------------------------------------------------------------
def index_ac_holder():
    print('''
        1) Update account details
        2) Check Balance
        3) Transfer amount to other account
        4) Display my account details
        5) Withdraw amount
        6) Deposit amount
        7) About us
        8) Delete my account

        Press any other key to exit.
        ''')

def ac_holder(n):
    x='1'
    while(x=='1'):
        choice=input("What would you like to do(enter i for index)\nSelect option: ")
        if(choice=='1'):
            functions.update_acc(n)
            x=functions.cont()
        elif(choice=='2'):
            functions.check_balance(n)
            x=functions.cont()
        elif(choice=='3'):
            functions.transfer(n)
            x=functions.cont()
        elif(choice=='4'):
            functions.ac_details(n)
            x=functions.cont()
        elif(choice=='5'):
            functions.withdraw(n)
            x=functions.cont()
        elif(choice=='6'):
            functions.deposit(n)
            x=functions.cont()
        elif(choice=='7'):
            functions.aboutus()
            x=functions.cont()
        elif(choice=='8'):
            functions.delete(n)
            print("We are sorry to see you go")
            x='xyz'
        elif(choice=='i' or choice=='I'):
            index_ac_holder()
            ac_holder(n)
        else:
            return
#-----------------------------------------------------------------
print('''
     _________________________________
    <Welcome to My Bank! your own bank>
     ---------------------------------
                   0
                    O   ^__^
                     o  (oo)\_______
                        (__)\       )\/\

                            ||----w |
                            ||     ||
''')

print('''Who are you:
        1) Account holder
        2) Non account holder

    Enter any other key to exit 
        ''')
identity=str(input())
if(identity=='2'):
    index_non_ac_holder()
    non_ac_holder()
elif(identity=='1'):
    x,y=functions.check_login()
    if(x=='abc'):
        index_ac_holder()
        ac_holder(y)
    else:
        print("Account doesnt exist\n")
    
else:
    print("Invalid Input")

print("-----------------------------Thank-You----------------------------------")
