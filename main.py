from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

print("\n===================== COFFEE MACHINE =====================")

def report():
    coffee_machine.report()
    money_machine.report()

machine_ON = True

while machine_ON:  
    customer_choice = input(f"\nType REPORT to see if the ingredients are enough." +
                            f"\nType OFF if you want to turn the machine off" + 
                            f"\nWhat would ypu like? {items_menu.get_items()}\n -> ").lower()
    if customer_choice == "report":
        report()
    elif customer_choice == "off":
        machine_ON = False
    else:
        drink = items_menu.find_drink(customer_choice)
        if coffee_machine.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_machine.make_coffee(drink)
        else:
            break


 
