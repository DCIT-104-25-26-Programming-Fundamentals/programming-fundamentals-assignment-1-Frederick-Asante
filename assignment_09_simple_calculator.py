# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def display_menu():
    print("============================")
    print("     SIMPLE CALCULATOR      ")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
def get_numbers():
    try:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return None, None


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return round(num1 / num2, 2)


def modulus(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 % num2


def exponentiate(num1, num2):
    return num1 ** num2


def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Error: Invalid choice. Please enter a number from 1 to 7.")
            continue

        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
            continue

        try:
            if choice == "1":
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result:.2f}")
            elif choice == "5":
                result = modulus(num1, num2)
                print(f"Result: {num1} % {num2} = {result}")
            elif choice == "6":
                result = exponentiate(num1, num2)
                print(f"Result: {num1} ** {num2} = {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")


if __name__ == "__main__":
    main()