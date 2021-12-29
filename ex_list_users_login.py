users = ["ori@gmail.com", "gal@hackeru.com"]
usres_login = []
x = 0
menu = '''
0 - "הפסק פעולה"
1- "הרשמה"
2 - "כניסה"
3 - "יציאה"
4 - "מחיקה"
'''

def register():
    global users
    global usres_login
    user = input("enter mail: ")
    if user not in users:
        users.append(user)
        print("nice! you are login :)")
    else:
        print("user is already taken try again")
        register()

def login():
    global x
    user = input("enter your email: ")
    if user not in users:
        print("user is not exist please register...")
        x += 1
    else:
        if user in usres_login:
            print("you already login... please logout first!")
        else:
            usres_login.append(user)
            print("welcome you are now login")
def logout():
    global x
    user = input("please enter your email: ")
    if user not in users:
        print("user is not exist please register first...")
        x += 1
    else:
        if user in usres_login:
            usres_login.remove(user)
        else:
            print("user is not login...")
def delete():
    global x
    user = input("please enter your email: ")
    if user not in users:
        print("user is not exist please register first...")
        x += 1
    else:
        if user in usres_login:
            users.remove(user)
            usres_login.remove(user)
            print("this user is successfully logout and deleted")
        else:
            print("user is not login you need to login to logout")

def info():
    print(users)
    print(usres_login)

def play():
    if x == 3:
        return
    choise = input('OPTIONS: \n'
                   '0 = stop | '
                   '1 = register | '
                   '2 = login | '
                   '3 = logout | '
                   '4 = delete | '
                   '100 = info\n enter here: ')
    if choise == "0":
        return
    elif choise == "1":
        register()
    elif choise == "2":
        login()
    elif choise == "3":
        logout()
    elif choise == "4":
        delete()
    elif choise == "100":
        info()
    play()
play()