from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


ingredients = CoffeeMaker()
mon = MoneyMachine()
is_on = True
drink = Menu()


while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        ingredients = CoffeeMaker()
        mon = MoneyMachine()
        ingredients.report()
        mon.report()
    else:
        drink = Menu()
        drink.find_drink(choice)
        if ingredients.is_resource_sufficient(choice):
            payment = MoneyMachine()
            payment.process_coins()
            if payment.make_payment(payment, drink["cost"]):
                ingredients.make_coffee(choice)
 
