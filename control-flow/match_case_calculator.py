# File: match_case_calculator.py

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def main():
    # Prompt the user for input
    num1 = get_number("Enter the first number: 10")
    num2 = get_number("Enter the second number: 5")
    operation = input("Choose the operation (+, -, *, /): ")
    # Perform the calculation using match case
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}.")
            else:
                print("Cannot divide by zero.")
        case _:
            print("Invalid operation. Please choose from +, -, *, /.")