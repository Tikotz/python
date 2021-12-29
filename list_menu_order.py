menu = ['Pizza', 'Sushi', 'Burger', 'Salad', 'ice cream']
orders = ['Pizza', 'Pizza', 'Burger']
total = 0

def print_menu():
    count = 1
    for i in menu:
        print(str(count) + "." + i)
        count += 1


def add():
    global orders
    index = input("enter meal code or enter 0 to end")
    while index != "0":
        if int(index) > len(menu):
            print("this meal is not exist")
        else:
            orders.append(menu[int(index) - 1])
        index = input("enter meal code or press 0 to end")
    print("the order is add succssfully")
    print(orders)


def remove():
    food = input("enter which meal you want to cancel: ")
    for i in orders:
        if i == food:
            orders.remove(food)
    print(orders)


#remove()


def order_print():
    for i in menu:
        count = orders.count(i)
        if count != 0:
            print(str(count)+' '+i)


def order_time(count):
    global total
    if 1 <= count <= 2:
        total += 10 * count
    elif 2 < count <= 4:
        total += 7 * count
    else:
        total += 4 * count

def total_time():
    global total
    total = 0
    for i in menu:
        count = orders.count(i)
        if count > 0:
            order_time(count)
            print(str(count)+ ' ' + i)
    print('the order will be ready in ' + str(total)+ ' min')


def play():
    num = input("enter number: ")
    if num == '1':
        print_menu()
    elif num == '2':
        add()
    elif num == '3':
        remove()
    elif num == '4':
        order_print()
    elif num == '5':
        total_time()
    elif num == '300':
        return
    play()


play()