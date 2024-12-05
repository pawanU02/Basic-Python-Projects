# Create a Python script that performs addition, subtraction, multiplication, and division.
import time

def basic_calculator():
    """
    A basic calculator program that performs basic arithmetic operations
    such as Addition, Subtraction, Multiplication and Division.

    - The program accepts two numbers as inputs.
    - Provide a menu for operations: Addition, Subtraction, Multiplication or Division.
    - Result based on the selected operation.
    - Ensures no invalid inputs are accepted using Exception Handling.
    - Handles the Division by Zero error.
    - Prompts the user to continue or exit the program after each operation.
    """
    try:
        ask_num_one = input("Enter number: ")
        ask_num_one = float(ask_num_one)

        ask_num_two = input("Enter number: ")
        ask_num_two = float(ask_num_two)
    except ValueError:
        print("ENTER ONLY NUMBERS AS INPUT!")
        quit()

    # Operations
    print(
        """Choices:
        Addition/Add/+ 
        Subtraction/Sub/-
        Multiplication/Mul/Product/* 
        Division/Div 
        """
    )
    choice = input("Choice: ").capitalize()

    while True:
        match choice:
            case "Addition" | "Add" | "+":
                print(f"Sum: {ask_num_one + ask_num_two}")
            case "Subtraction" | "Sub" | "-":
                print(f"Difference: {ask_num_one - ask_num_two}")
            case "Multiplication" | "Mul" | "Product" | "*":
                print(f"Product: {ask_num_one * ask_num_two}")
            case "Division" | "Div" | "/":
                if ask_num_two == 0:
                    print("DIVISION BY ZERO ERROR!!")
                else:
                    print(f"Division: {ask_num_one / ask_num_two}")
            case _:
                print("Not a valid Operation. Try again!")

        another_calculation = input("Want to continue? (yes or no?: ").lower()
        if another_calculation not in ["yes", "y"]:
            print("Exiting...")
            time.sleep(1)
            print("Exited")
            break

# Calling the calculator function
if __name__ == "__main__":
    basic_calculator()