from replit import clear  # run on replit.comn

from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()


def order_again():
    input_value = input("\nWould you like to order again? Type 'y' or 'n': ").lower()
    return True if input_value == "y" else False


def main():
    """Main"""

    clear()

    print(
        """
         ,-"-.
       _r-----i          _
       \      |-.      ,###.
        |     | |    ,-------.
        |     | |   c|       |                       ,--.
        |     |'     |       |      _______________ C|  |
        (=====)      =========      \_____________/  `=='   cww
(HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH)

"""
    )

    print("\n=== Maintainer =================")
    print("Current resources:")
    coffee_machine.report()
    money_machine.print_profits()
    print("================================\n")

    menu.display_prices()

    order_input = input(
        "\nWhat would you like? (espresso, latte, cappuccino): "
    ).lower()

    order = menu.find_drink(order_input)
    order_cost = order.cost
    print(f"\nOrder: {order.name.title()} \n")

    machine_report = coffee_machine.is_resource_sufficient(order)

    # if there's enough resources
    can_make_coffee = machine_report["can_make"]

    if can_make_coffee:
        # insert coins
        process_coffee = money_machine.make_payment(order_cost)

        # if payment is success, make coffee
        if process_coffee:
            coffee_machine.make_coffee(order)

            # check if the customer wants to order again
            process_order_again = order_again()

            if process_order_again:
                main()
            else:
                print("\n----------- Happy coding! -----------\n")

    else:
        lacking_item = machine_report["item"] if "item" in machine_report else ""
        print(f"Sorry there is not enough {lacking_item}.")

        process_order_again = order_again()
        if process_order_again:
            main()
        else:
            print("\n----------- Happy coding! -----------\n")


main()
