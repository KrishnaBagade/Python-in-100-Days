MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0,
}


def resource_check(drink_chosen):
    ingredients_available = []
    if resources["water"] >= MENU[drink_chosen]["ingredients"]["water"]:
        ingredients_available.append("water")
    if resources["milk"] >= MENU[drink_chosen]["ingredients"]["milk"]:
        ingredients_available.append("milk")
    if resources["coffee"] >= MENU[drink_chosen]["ingredients"]["coffee"]:
        ingredients_available.append("coffee")
    return ingredients_available


def take_money(drink_chosen, customer_paid):
    drink_cost = MENU[drink_chosen]["cost"]
    if drink_cost > customer_paid:
        print(f"Sorry that's not enough money for {drink_chosen} which costs ${drink_cost}.")
        print(f"Refunding your ${customer_paid} .")
    elif drink_cost == customer_paid:
        make_drink = True
        with open("profit.txt",mode="r") as file:
            profit = file.read()
        profit += drink_cost
        with open("profit.txt",mode="w") as file:
            file.write(f"{profit}")
        return make_drink
    elif drink_cost < customer_paid:
        make_drink = True
        with open("profit.txt",mode="r") as file:
            profit = file.read()
        profit += drink_cost
        with open("profit.txt",mode="w") as file:
            file.write(f"{profit}")
        return make_drink


refund = 0
while True:
    drink_chosen = input("What drink would you like(espresso/latte/cappuccino): ").lower()
    if drink_chosen == "off":
        break
    elif drink_chosen == "report":
        print(resources)
        continue
    elif drink_chosen != "espresso" and drink_chosen != "latte" and drink_chosen != "cappuccino":
        continue
    resources_available = resource_check(drink_chosen)
    if "water" not in resources_available:
        print(f"Sorry not enough water to make {drink_chosen}.")
    if "milk" not in resources_available:
        print(f"Sorry not enough milk to make {drink_chosen}")
    if "coffee" not in resources_available:
        print(f"Sorry not enough coffee to make {drink_chosen}")
    if len(resources_available) == 3:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        customer_paid = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.10) + (pennies * 0.01)
        should_make = take_money(drink_chosen, customer_paid)
        if MENU[drink_chosen]["cost"] < customer_paid:
            refund = (customer_paid - MENU[drink_chosen]["cost"])
        if should_make == True:
            resources["water"] -= MENU[drink_chosen]["ingredients"]["water"]
            resources["milk"] -= MENU[drink_chosen]["ingredients"]["milk"]
            resources["coffee"] -= MENU[drink_chosen]["ingredients"]["coffee"]
            resources["money"] += MENU[drink_chosen]["cost"]
            print(f"Here is your {drink_chosen} enjoy!")
            if refund > 0:
                print(f"Here's your ${refund} which was extra.")