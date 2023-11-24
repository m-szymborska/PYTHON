MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = [12, 12, 14]
water_r = resources['water']
coffee_r = resources['coffee']
milk_r = resources['milk']



def choice():
    my_choice = input("What would you like? (espresso/latte/cappuccino):")
    return my_choice


my_choice = choice()


if my_choice == 'report':
    j = 0
    for i in money:
        j = j + i
    water_r = resources['water']
    milk_r = resources['milk']
    coffee_r = resources['coffee']
    water_c = 0
    coffee_c = 0
    milk_c = 0
    print(f" Water: {water_r} ml\n Milk: {milk_r} ml\n Coffee: {coffee_r} g \n Money: ${j}")
    my_choice = choice()
if my_choice == 'espresso':
    water_c = MENU['espresso']['ingredients']['water']
    coffee_c = MENU['espresso']['ingredients']['coffee']
    milk_c = 0

elif my_choice == 'latte':
    water_c = MENU['latte']['ingredients']['water']
    coffee_c = MENU['latte']['ingredients']['coffee']
    milk_c = MENU['latte']['ingredients']['milk']

elif my_choice == 'cappuccino':
    water_c = MENU['cappuccino']['ingredients']['water']
    coffee_c = MENU['cappuccino']['ingredients']['coffee']
    milk_c = MENU['cappuccino']['ingredients']['milk']


def check_money():
    print("Please insert coins.")
    qu = int(input("how many quarters?:"))
    dim = int(input("how many dimes?:"))
    nic = int(input("how many nickles?:"))
    pen = int(input("how many pennies?:"))
    my_suma = (qu * 0.01) + (dim * 0.1) + (nic * 0.05) + (pen * 0.25)

    if my_choice == 'espresso':
        price = MENU['espresso']['cost']
        money.append(price)
    elif my_choice == 'latte':
        price = MENU['latte']['cost']
        money.append(price)
    elif my_choice == 'cappuccino':
        price = MENU['cappuccino']['cost']
        money.append(price)
    if my_suma - price < 0:
        print("“Sorry that's not enough money. Money refunded")
    elif my_suma - price >= 0:
        change = round((my_suma - price), 2)
        print(f"Here is ${change} in change")
        print(f"Here is your {my_choice} ☕️. Enjoy!")


def change_resources():
    resources['water'] = water_r - water_c
    resources['milk'] = milk_r - milk_c
    resources['coffee'] = coffee_r - coffee_c


while water_r - water_c >= 0 and coffee_r - coffee_c >= 0 and milk_r - milk_c >= 0 and my_choice != 'report':
    check_money()
    change_resources()
    water_r = resources['water']
    coffee_r = resources['coffee']
    milk_r = resources['milk']
    print(resources)
    my_choice = choice()
    if my_choice == 'report':
        j = 0
        for i in money:
            j = j + i
        water_r = resources['water']
        milk_r = resources['milk']
        coffee_r = resources['coffee']
        print(f" Water: {water_r} ml\n Milk: {milk_r} ml\n Coffee: {coffee_r} g \n Money: ${j}")
        my_choice = choice()
    if my_choice == 'espresso':
        water_c = MENU['espresso']['ingredients']['water']
        coffee_c = MENU['espresso']['ingredients']['coffee']
        milk_c = 0

    elif my_choice == 'latte':
        water_c = MENU['latte']['ingredients']['water']
        coffee_c = MENU['latte']['ingredients']['coffee']
        milk_c = MENU['latte']['ingredients']['milk']

    elif my_choice == 'cappuccino':
        water_c = MENU['cappuccino']['ingredients']['water']
        coffee_c = MENU['cappuccino']['ingredients']['coffee']
        milk_c = MENU['cappuccino']['ingredients']['milk']

else:
    if water_r - water_c < 0:
        print("Sorry there is not enough water.")
    if coffee_r - coffee_c < 0:
        print("Sorry there is not enough coffee.")
    if milk_r - milk_c < 0:
        print("Sorry there is not enough milk.")









