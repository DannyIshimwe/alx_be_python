# File: match_case_calculator.py

def main():
    try:
        # Prompt the user for input and convert to int
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return

    # Prompt the user to choose an operation
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

if __name__ == "__main__":
    main()
