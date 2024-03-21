Coffee Machine Program
This Python script simulates a basic coffee machine with a menu of three
drinks: espresso, latte, and cappuccino. Users can choose a drink, check
the availability of resources, and make a purchase by inserting coins. 
The program handles the payment, checks resource availability, and dispenses
the chosen drink if all conditions are met.

Menu and Resources
The menu and available resources are defined at the beginning of the script:

python
Copy code
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
}
Functions
resource_check(drink_chosen)
This function checks the availability of resources needed to make 
a chosen drink.

take_money(drink_chosen, customer_paid)
This function processes the payment and determines if the customer
has paid enough for the chosen drink.

Main Program
The main program runs in a continuous loop, prompting the user to 
choose a drink. It allows users to check the resources, and if the
necessary ingredients are available, it prompts the user to insert 
coins for payment. The program then processes the payment, updates the
resources, and serves the drink if the conditions are met.

Usage
Run the script.
Enter the desired drink (espresso, latte, cappuccino) or use the 
commands "off" to exit or "report" to check resources.
Follow the prompts to insert coins for payment.
Enjoy your drink!