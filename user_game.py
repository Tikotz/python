import datetime
x = 0

users = [{"email": "admin@admin123.gmail.com", "first": "admin", "last": "super", "username": "admin", "password": "admin123", "status_login": True, "points": 0},
         {"email": "oritikozki@gmail.com", "first": "ori", "last": "tikozki", "username": "oritiko", "password": "tiko123", "status_login": True, "points": 100}]


player = {"email": "", "first": "", "last": "", "username": "", "password": "", "status_login": False, "points": 0}

def sayhola(player):
    time = datetime.datetime.now()
    x = time.hour
    if x >= 19:
        print("hello and good evening " + player["first"] + ' ' + player["last"])
    elif x <= 12 and x > 12:
        print("hello and good morning " + player["first"] + ' ' + player["last"])
    elif x >= 12 and x < 14:
        print("hello and good noon " + player["first"] + ' ' + player["last"])
    elif x >= 14 and x < 19:
        print("hello and good after noon " + player["first"] + ' ' + player["last"])


def register():
    user = input("enter mail: ")
    for e in users:
        if user not in e["email"]:
            player.update({"email": user})
            print("nice! you now created your user :)")
            print("now you need to create your account")
            first = input("enter your name: ")
            last = input("enter your last name: ")
            username = input("enter a username: ")
            password = input("enter a password: ")
            player.update({"first": first, "last": last, "username": username, "password": password, "status_login": False, "points": 0})
            users.append(player)
            print(player)
        else:
            print("user is already taken try again")
            register()


def change_name(users):
    new_first = input("enter new name: ")
    new_last = input("enter new last")
    for u in users:
        if new_first == u["first"] and new_last == u["last"]:
            u["first"] = new_first
            u["last"] = new_last
        print(u)


def login(users):
    username = input('enter username: ')
    password = input('enter password: ')
    for u in users:
        if u["username"] == username and u["password"] == password:
            u["status_login"] = "True"
        else:
            print("wrong username or password")
        print(u["status_login"])


def logout():
    for u in users:
        u["status_login"] = "False"


def change_password():
    oldpass = input("enter old password: ")
    if oldpass == player["password"]:
        newpass = input("enter new password: ")
        player["password"] = newpass
    else:
        print("wrong password")


def info():
    Email = input('enter email: ')
    password = input('enter password: ')
    for u in users:
        if u["email"] == Email and u["password"] == password:
            print(u)


def user_info():
    choise = input('OPTIONS: \n'
                   '0 = stop | '
                   '1 = register | '
                   '2 = change name| '
                   '3 = login | '
                   '4 = logout | '
                   '5 = change password | '
                   '100 = info'
                   '\n enter here: ')

    if choise == "0":
        return play_center()
    elif choise == "1":
        register()
    elif choise == "2":
        change_name(users)
    elif choise == "3":
        login(users)
    elif choise == "4":
        logout()
    elif choise == "5":
        change_password()
    elif choise == "100":
        info()
    user_info()


def play_center():
    menu = '1 - user info |' \
           '2 - game center |'
    print(menu)
    choise = int(input("enter choise: "))
    if choise == 1:
        user_info()
    elif choise == 2:
        user_name = input("enter username")
        user_pass = input("enter password")
        for u in users:
            if user_name == u["username"] and user_pass == u["password"]:
                if u["status_login"] == True:
                    sayhola(u)
                    play(u)
                else:
                    print("you are not logged")
