def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on the provided operation parameter.
    
    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. Accepts 'add', 'subtract', 'multiply', or 'divide'.
    
    Returns:
        float or str: The result of the arithmetic operation, or a message if division by zero occurs.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"

if __name__ == "__main__":
    print(perform_operation(5, 6, 'add'))       
    print(perform_operation(5, 6, 'subtract'))  
    print(perform_operation(5, 6, 'multiply'))  
    print(perform_operation(5, 0, 'divide'))    
    print(perform_operation(5, 6, 'divide'))    

