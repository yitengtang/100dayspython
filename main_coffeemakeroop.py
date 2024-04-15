from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True


while is_on:
    choice = input(f"What would you like?({Menu().get_items()}): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        report_rest=coffee_maker.report()
    else:
        item = menu.find_drink(choice)
        #drink = MenuItem(choice)
        #print(drink)
        enough_materials = coffee_maker.is_resource_sufficient(item)
        if enough_materials == True:
            cost = item.cost
            print(cost)

            if money_machine.make_payment(cost):
                coffee_maker.make_coffee(item)
                money_machine.report()



