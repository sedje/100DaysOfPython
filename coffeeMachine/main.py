from data import MENU, resources

PROFIT = 0.0


def check_and_vend(ingredients):
    """ check if resources are available and if they are, subtract them """
    available = []
    for resource in ingredients:
        if ingredients[resource] > resources[resource]:
            available.append(resource)

    if len(available) == 0:
        for resource in ingredients:
            resources[resource] -= ingredients[resource]
        return True
    else:
        print("Sorry, the following resources are not available: %s" % ', '.join(available))
        return False


def insert_money():
    """ Insert more coins to top up"""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)


def report():
    """ Report on current resources and MONEY """
    for value in resources:
        resource = "%s: %iml" % (value, resources[value])
        print(resource)
    print("Profit: $%.2f" % PROFIT)


def refund(funds):
    """ Refund all money and reset to 0 """
    print("Here is $%.2f in return." % funds)
    return 0


def run():
    """ Run the main machine """
    # Use a breakpoint in the code line below to debug your script.
    global PROFIT
    funds = 0
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == 'report':
            report()
        elif choice == 'refund':
            funds = refund(funds)
        elif choice == 'off':
            is_on = False
        else:
            while funds < MENU[choice]['cost']:
                print("Please insert coins")
                funds = insert_money()

            if check_and_vend(MENU[choice]['ingredients']):
                funds -= MENU[choice]['cost']
                PROFIT += MENU[choice]['cost']
                print("Here is $%.2f in change." % funds)
                funds = 0
                print("Here is your %s. ☕ Enjoy!" % choice)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
