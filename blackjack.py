import random

com = 0
points = 0
def game_50(points):
    global com
    print(points)
    jack = 10
    queen = 10
    king = 10
    ase = 11
    card_list=[2,3,4,5,6,7,8,9,10,jack,queen,king,ase]
    op=input("walcome press 1 to pay 50 for the game or press 2 for menu")
    if op=="1":
#הגרלת הקלפים הראשונה
        player_sum=0
        com_sum = 0
        points -= 50
        player_cards = []
        comp_cards = []
        player_card1=random.choice(card_list)
        player_sum+=player_card1
        player_cards.append(player_card1)
        player_card2 = random.choice(card_list)
        player_sum+=player_card2
        player_cards.append(player_card2)
        com_card1 = random.choice(card_list)
        com_sum+=com_card1
        comp_cards.append(com_card1)
        com_card2 = random.choice(card_list)
        com_sum+=com_card2
        comp_cards.append(com_card2)
        print("your cards: "+str(player_card1) +" "+ str(player_card2))
        print("diler card: "+str(com_card1 + com_card2))
        choois=input("prass 1 to pull or 2 to stand")
#עמידה או משיכה
        while choois == "1":
            player_card3 = random.choice(card_list)
            print("player card:" + str(player_card3))
            player_sum += player_card3
            player_cards.append(player_card3)
            print("total player: "+ str(player_sum))
            if player_sum > 21:
                for c in player_cards:
                    if c == ase:
                        ase = 1
                        choois = input("prass 1 to pull or 2 to stand")
                        if choois == "1":
                            player_card4 = random.choice(card_list)
                            print('player card: ' + str(player_card4))
                            player_sum += player_card4
                            player_cards.append(player_card4)
                            print("total player: " + str(player_sum))
                        com = 1
                    else:
                        print("you lose you have " + str(player_sum))
                        choois = "0"
                        break
            else:
                choois = input("prass 1 to pull or 2 to stand")
                com = 1
        if choois == '2':
            com = 1

#תור המחשב
        while com_sum <= 17 and com == 1:
            com_card3 = random.choice(card_list)
            com_sum += com_card3
            comp_cards.append(com_card3)
            print('computer card: ' + str(com_card3))
            print("total diler: "+str(com_sum))
        else:
            if com_sum > 21 and player_sum < 21:
                print("you win!!! +100")
                points += 100
            elif com_sum > 21:
                for c in comp_cards:
                    if c == ase:
                        ase = 1
                        com_card4 = random.choice(card_list)
                        print('computer card: ' + str(com_card4))
                        com_sum += com_card4
                        comp_cards.append(com_card4)
                        print("total computer: " + str(com_sum))
            elif player_sum == 21:
                print("black jack!!! +150")
                points += 150
            else: #במקרה של הפסד
                print("you lost 50")
                points -= 50
    op2=input("again?" "<y/n>")
    if op2=="y":
        game_50(points)
    elif op2 == "n":
        print(points)
        return points







