# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. One of:
                         'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or str: The result of the arithmetic operation, or an
                      error message if operation is invalid or if
                      division by zero occurs.
    """

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    else:
        return "Error: Invalid operation"
