import user_game,game_play_oron,game_x_o,blackjack,csv

x = 0

users = [{"email": "admin@admin123.gmail.com", "first": "admin", "last": "super", "username": "admin", "password": "admin123", "status_login": True, "points": 0},
         {"email": "oritikozki@gmail.com", "first": "ori", "last": "tikozki", "username": "oritiko", "password": "tiko123", "status_login": True, "points": 100}

]


def file(users):
    with open("info.csv", 'w', newline='')as file1:
        writer = csv.writer(file1)
        writer.writerow(['email', 'first', 'last', 'username', 'password', 'status_login', 'points'])
        for l in users:
            writer.writerow([l['email'], l['first'], l['last'], l['username'], l['password'], l['status_login'], l['points']])
        file1.close()


def play_center2():
    menu = '1 - user info |'\
           '2 - game center |'
    print(menu)
    choise = int(input("enter choise: "))
    if choise == 1:
        user_game.user_info()
    elif choise == 2:
        for u in users:
            play(u)


def play_center():
    menu = '1 - user info |'\
           '2 - game center |'
    print(menu)
    choise = int(input("enter choise: "))
    if choise == 1:
        user_game.user_info()
    elif choise == 2:
        user_name = input("enter username")
        user_pass = input("enter password")
        for u in users:
            if user_name == u["username"] and user_pass == u["password"]:
                if u["status_login"] == True:
                    user_game.sayhola(u)
                    play(u)
                else:
                    print("you are not logged")
            else:
                print("register first2")



def play(user):
    choise = int(input('0 - go back to menu |\n'
                       "1 - play oron game to earn points |\n"
                       "2 - play X & O to earn points |\n"
                       "3 - play black jack (you need at least 50 points)\n"
                       "what game do you want to play?\n"))
    if choise == 0:
        play_center2()
    if choise == 1:
        x = game_play_oron.play_oron()
        user["points"] = x
        print(user)
        play_center2()
    elif choise == 2:
        x = game_x_o.play()
        user["points"] = x
        print(user)
        play_center2()
    elif choise == 3:
        if user["points"] < 50:
            print("you don't have enough points... go earn sum points")
            play(user)
        else:
            user["points"] -= 50
            x = blackjack.game_50(int(user["points"]))
            if x == 0:
                print("you don't have any points")
            else:
                user["points"] += x
                print(user)
    play_center2()


play_center()
file(users)