from replit import clear

from art import coffee_machine_art

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def display_resources():
    """"""
    print("\n=== Maintainer =================")
    print("Current resources:")
    for resource_key in resources:
        print(f"   {resource_key.title()} : {resources[resource_key]}")

    print("\n================================\n")


def check_resources(order_requirements):
    """"""
    for resource_key in resources:

        if resource_key in order_requirements:
            current_stock = resources[resource_key]
            order_requirement = order_requirements[resource_key]

            if current_stock < order_requirement:
                return resource_key
            else:
                # reduce current resources
                resources[resource_key] -= order_requirement

    return "ok"


print("\n-------------- Welcome! --------------\n")


def start_machine():
    display_resources()

    print(
        f"====== Espresso: ${MENU['espresso']['cost']}, Latte: ${MENU['latte']['cost']}, Cappuccino: ${MENU['cappuccino']['cost']} ======\n"
    )
    order_input = input("What would you like? (espresso, latte, cappuccino): ").lower()
    order = MENU[order_input]

    # check if there are enough resources/ingredients
    resources_status = check_resources(order["ingredients"])

    if resources_status == "ok":
        # process coins
        print("\nPlease insert coins:")
        quarters = float(input("quarters: ")) * 0.25
        dimes = float(input("dimes: ")) * 0.1
        nickles = float(input("nickles: ")) * 0.05
        pennies = float(input("pennies: ")) * 0.01

        total_coins = round(quarters + dimes + nickles + pennies, 2)
        order_cost = order["cost"]

        change = round(total_coins - order_cost, 2)

        print(f"\nTotal Coins: ${total_coins}")
        print(f"Order cost: ${order['cost']}")
        if total_coins >= order_cost:
            print(f"Change: ${change}")
            # add payment to resources
            if "money" in resources:
                resources["money"] += order["cost"]
            else:
                resources["money"] = order["cost"]

            # successful transaction
            print("\n---------------------------------------")
            print("Here's your coffee ☕. Have a nice day!")
            print("---------------------------------------\n")

        else:
            print("\n---------------------------------------")
            print(
                f"\nSorry, not enough coins. Money refunded.\nOrder costs: ${order_cost}\n"
            )
            print("---------------------------------------\n")

        # print("\n")
        # display_resources()

    else:
        # not enough resources
        print("\n----------------")
        print(f"Not enough: {resources_status.title()}")
        print("----------------\n")


def main():
    clear()
    print(coffee_machine_art)
    start_machine()

    while True:
        order_again = input("Would you like to order again? Type 'y' or 'n': ").lower()

        if order_again == "y":
            main()
        else:
            print("\n=========== Happy coding! ===========\n")
            break


main()
