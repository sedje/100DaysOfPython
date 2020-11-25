from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    cm = CoffeeMaker()
    mm = MoneyMachine()
    menu = Menu()

    is_on = True
    while is_on:
        print()
        choice = input("What would you like? (%s): " % menu.get_items())
        if choice == 'report':
            cm.report()
            mm.report()
        elif choice == 'off':
            is_on = False
        else:
            drink = menu.find_drink(choice)
            if drink and cm.is_resource_sufficient(drink):
                if mm.make_payment(drink.cost):
                    cm.make_coffee(drink)


if __name__ == "__main__":
    main()
