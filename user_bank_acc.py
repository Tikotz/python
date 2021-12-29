import datetime
user_bank_account = {
    "first": "Gal",
    "last": "Lavi",
    "username": "gallavi",
    "password": "gal123",
    "status_login": "True",
    "total": "0",
    "credit": "500"
}

def sayhola():
    time = datetime.datetime.now()
    x = time.hour
    if x >= 19:
        print("hello and good evening " + user_bank_account["first"] + ' ' + user_bank_account["last"])
    elif x <= 12 and x > 12:
        print("hello and good morning " + user_bank_account["first"] + ' ' + user_bank_account["last"])
    elif x >= 12 and x < 14:
        print("hello and good noon " + user_bank_account["first"] + ' ' + user_bank_account["last"])
    elif x >= 14 and x < 19:
        print("hello and good after noon " + user_bank_account["first"] + ' ' + user_bank_account["last"])
#sayhola()

def change_name():
    new_first = input("enter new name: ")
    new_last = input("enter new last")
    user_bank_account["first"] = new_first
    user_bank_account["last"] = new_last
    print(user_bank_account)
#change_name()

def login():
    username = input('enter username: ')
    password = input('enter password: ')
    if user_bank_account["username"] == username and user_bank_account["password"] == password:
        user_bank_account["status_login"] = "True"
    else:
        print("wrong username or password")
    print(user_bank_account["status_login"])
#login()

def logout():
    user_bank_account["status_login"] = "False"


def change_password():
    oldpass = input("enter old password: ")
    if oldpass == user_bank_account["password"]:
        newpass = input("enter new password: ")
        user_bank_account["password"] = newpass
    else:
        print("wrong password")


def insert_money():
    if user_bank_account["status_login"] == "True":
        money = int(input("enter how much money you want to insert: "))
        user_bank_account["total"] = str(money)
    else:
        print("something went wrong try to login first")
    print(user_bank_account)
#insert_money()


def withdrawal():
    if user_bank_account["status_login"] == "True":
        passw = input('enter your password: ')
        if user_bank_account["password"] == passw:
            withdrawal = int(input("how much money do you want to get?: "))
            if withdrawal <= (int(user_bank_account["total"] + user_bank_account["credit"])):
                (user_bank_account["total"]) = int(user_bank_account["total"]) - withdrawal
            else:
                print("\n CREDIT IS TO LOW ! please talk with the manager to increase your credit\n")
    print(user_bank_account)

#withdrawal()


def credit_change():
    if user_bank_account["status_login"] == "True":
        passw = input("enter your password: ")
        if passw == user_bank_account["password"]:
            change_credit = input("enter the amount of credit you want to increase: ")
            admin_pass = ('admin123456',)
            adpass = input('enter admin password to change the credit: ')
            if adpass == admin_pass:
                user_bank_account["credit"] = change_credit
            else:
                print('wrong admin password')
        else:
            print('wrong password')
    else:
        print('login first')

    print(user_bank_account)


#credit_change()


def play():
    sayhola()
    choise = input('OPTIONS: \n'
                   '0 = stop | '
                   '1 = change name | '
                   '2 = login | '
                   '3 = logout | '
                   '4 = change password | '
                   '5 = insert money | '
                   '6 = withdrawal money | '
                   '7 = credit change | '
                   '100 = info\n enter here: ')
    if choise == "0":
        return
    elif choise == "1":
        change_name()
    elif choise == "2":
        login()
    elif choise == "3":
        logout()
    elif choise == "4":
        change_password()
    elif choise == '5':
        insert_money()
    elif choise == '6':
        withdrawal()
    elif choise == '7':
        credit_change()
    elif choise == "100":
        print(user_bank_account)
    play()


play()