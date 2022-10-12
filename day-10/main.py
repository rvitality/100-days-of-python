print(
    """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

-- ASCII art by Jeremy J. Olson --  

"""
)


def display_result(num1, num2, operator, res):
    """Display formatted computation."""
    return f"\n{num1} {operator} {num2} = {res}"


def calculate(num1, num2, operator):
    """Takes two numbers and an operator to perform the calculation"""
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2,
    }

    return operations[operator]


def calculator():

    first_num = float(input("Enter first number: "))
    while True:
        # operators
        print("+ - * /")
        operator = input("Select an operator: ")
        next_num = float(input("Enter next number: "))
        result = calculate(first_num, next_num, operator)

        print(display_result(first_num, next_num, operator, result))

        print(f"\nType 'y' to continues calculating with {result}")
        print("Type 'n' to EXIT")
        print("Type 'new' to start a new calculation")
        decision = input("Answer: ")
        print("\n")

        if decision == "n":
            print("\n----- Happy coding! -----\n")
            break

        # continues with prev result
        if decision == "y":
            first_num = result

        else:
            calculator()


calculator()
