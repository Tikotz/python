import random
import operator
import datetime


def sayhola():
    time = datetime.datetime.now()
    x = time.hour
    first = input('enter your first name')
    last = input('enter your last name')
    if x >= 19:
        print("hello and good evening " + first + ' ' + last)
    elif x <= 12 and x > 12:
        print("hello and good morning " + first + ' ' + last)
    elif x >= 12 and x < 14:
        print("hello and good noon " + first + ' ' + last)
    elif x >= 14 and x < 19:
        print("hello and good after noon " + first + ' ' + last)

sum_points = 0
def level1(sum_points):
    points = 0
    while points < 100:
        num1 = random.randrange(1, 11)
        num2 = random.randrange(1, 11)
        print('to exit write "exit"')
        user_sum = input(str(num1) + " + " + str(num2) + " = ")
        if user_sum == "exit":
            print("\npoints = ", sum_points)
            sum_points += points
            return sum_points
        elif (int(user_sum) == num1 + num2):
            points += 10
            print("points = ", points)
        else:
            points -= 5
            print('-5 points', 'TRY again')
    else:
        sum_points += points
        return level2(sum_points)


def level2(sum_points):
    points = 0
    while points < 100:
        num1 = random.randrange(1, 51)
        num2 = random.randrange(1, 51)
        print('to exit write "exit"')
        user_sum = input(str(num1) + " + " + str(num2) + " = ")
        if user_sum == "exit":
            print("\npoints = ", sum_points)
            sum_points += points
            return sum_points
        elif int(user_sum) == num1 + num2:
            points += 10
            print("points = ", points)
        else:
            points -= 5
            print('-5 points', 'TRY again')
    else:
        sum_points += points
        return level3(sum_points)


def level3(sum_points):
    points = 0
    ops = [("+", operator.add), ('-', operator.sub), ('*', operator.mul)]
    while points < 100:
        num1 = random.randrange(1, 21)
        num2 = random.randrange(1, 21)
        print('to exit write "exit"')
        op, fn = random.choice(ops)
        user_sum = input("what is {} {} {}? ".format(num1, op, num2))
        if user_sum == "exit":
            print('\npoints = ', sum_points)
            sum_points += points
            return sum_points
        elif int(user_sum) == fn(num1, num2):
            points += 10
            print("points = ", points)
        else:
            points -= 5
            print('-5 points', 'TRY again')
            print("points = ", points)

    else:
        sum_points += points
        return level4(sum_points)


def level4(sum_points):
    points = 0
    ops = [("+", operator.add), ('-', operator.sub), ('*', operator.mul)]
    while points < 100:
        num1 = random.randrange(1, 21)
        num2 = random.randrange(1, 21)
        print('to exit write "exit"')
        op, fn = random.choice(ops)
        user_sum = input("what is {} {} {}? ".format(num1, op, num2))
        if user_sum == "exit":
            print('\npoints = ', points)
            sum_points += points
            return sum_points
        elif (int(user_sum) == fn(num1, num2)):
            points += 10
            print("points = ", points)
        else:
            points -= 5
            print('-5 points', 'TRY again')
            print("points = ", points)
    else:
        sum_points += points
        return sum_points


def play_oron():
    rules = '''
    if you choose level 1 you will test in math from num: 1-10.
    if you choose level 2 you will test in math from num: 1-50.
    if you choose level 3 you will test in math form num: 1-10 with "+, -, *".
    if you choose level 4 you will test in math form num: 1-20 with "+, -, *".
    if you choose level 0 you will exit.
    *** if you got 100 points you automatic leveled up ***
    '''
    #sayhola()
    print(rules)
    level = int(input("enter level 1 - 4: "))
    if level == 1:
        x = level1(sum_points)
        print(x)
    elif level == 2:
        x = level2(sum_points)
        print(x)
    elif level == 3:
        x = level3(sum_points)
        print(x)
    elif level == 4:
        x = level4(sum_points)
        print(x)
    return x