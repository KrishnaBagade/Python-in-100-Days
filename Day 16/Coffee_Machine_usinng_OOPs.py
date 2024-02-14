from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

command = CoffeeMaker()
name_of_drinks = Menu()
money = MoneyMachine()



while True:
  user_input = input(f"Which drink do you want? {name_of_drinks.get_items()}")
  if user_input == "report":
    command.report()
    money.report()
  elif user_input == "off":
    break
  else:
    drink_cost = name_of_drinks.find_drink(user_input)
    drink_make=command.is_resource_sufficient(drink_cost)
    if drink_make is True :
      transaction = money.make_payment(drink_cost)
      if transaction is True :
        command.make_coffee(drink_cost)
      
      
      
  
#report(`money`), make_payment(cost), make_coffee(order),name,cost,ingredints

