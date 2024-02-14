Coffee Machine Program Readme
Overview
This Python script simulates a coffee machine with basic functionalities. It uses three classes: CoffeeMaker, Menu, and MoneyMachine to handle coffee making, menu items, and payment transactions, respectively.

Components
CoffeeMaker: Manages the coffee-making process and resources.

Menu: Stores the available drinks and their corresponding costs.

MoneyMachine: Handles payment transactions and provides a report.

Usage
Run the script, and it will prompt you to select a drink or perform specific actions.

bash
Copy code
Which drink do you want? ['espresso', 'latte', 'cappuccino']:
Enter the desired drink name or use the command "report" to get a report on resources and money status.

bash
Copy code
Which drink do you want? ['espresso', 'latte', 'cappuccino']: report
This will display the current resources status and money report.

To turn off the coffee machine, enter "off".

bash
Copy code
Which drink do you want? ['espresso', 'latte', 'cappuccino']: off
Functionality
Making a Drink: Enter the name of the desired drink, and the script will check if there are enough resources. If sufficient, it will prompt for payment. Upon successful payment, it will make the selected drink.

Reporting: Use the "report" command to get a report on available resources (Coffee, Milk, Water) and the current amount of money.

Turning Off: Enter "off" to exit the program.

Classes and Methods
1. CoffeeMaker
report(): Displays the current status of resources (coffee, milk, water).

is_resource_sufficient(drink_cost): Checks if there are enough resources to make a specific drink.

make_coffee(drink_cost): Makes the selected drink and updates resource levels.

2. Menu
get_items(): Returns a list of available drinks.

find_drink(drink_name): Returns the cost of the specified drink.

3. MoneyMachine
report(): Displays the current amount of money.

make_payment(amount): Handles the payment transaction. Returns True if payment is successful.

Example
bash
Copy code
Which drink do you want? ['espresso', 'latte', 'cappuccino']: latte
Please insert coins.
How many quarters?: 2
How many dimes?: 1
How many nickels?: 1
How many pennies?: 4
Payment successful. Here is your latte. Enjoy!
Notes
The script runs indefinitely until the user enters "off" to turn off the coffee machine.

Make sure to provide the correct input when prompted for coin amounts during payment.

Ensure the coffee_maker, menu, and money_machine modules are available in the same directory or specified in the Python path.