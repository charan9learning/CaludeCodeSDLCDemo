"""
Simple Python Calculator
A beginner-friendly calculator that performs basic arithmetic operations.
"""

import math


def is_valid_number(input_string):
    """Validate if input string is a valid number (int or float)."""
    try:
        float(input_string)
        return True
    except ValueError:
        return False


def add(num1, num2):
    """Add two numbers."""
    return num1 + num2


def subtract(num1, num2):
    """Subtract two numbers."""
    return num1 - num2


def multiply(num1, num2):
    """Multiply two numbers."""
    return num1 * num2


def divide(num1, num2):
    """Divide two numbers."""
    if num2 == 0:
        return None  # Return None for division by zero
    return num1 / num2


def cosine(num1):
    """Calculate cosine of a number (in radians)."""
    return math.cos(num1)


def get_number(position="number"):
    """Get and validate a number from user with custom prompt."""
    while True:
        prompt = f"Enter {position}: " if position != "number" else "Enter number: "
        user_input = input(prompt)
        if is_valid_number(user_input):
            return float(user_input)
        else:
            print("Error: Please enter a valid number.")


def get_first_number():
    """Get and validate the first number from user."""
    return get_number("first number")


def get_second_number():
    """Get and validate the second number from user."""
    return get_number("second number")


def get_operation():
    """Get and validate the operation from user."""
    valid_operations = ['+', '-', '*', '/', 'cos']
    while True:
        operation = input("Choose an operation (+, -, *, /, cos): ")
        if operation in valid_operations:
            return operation
        else:
            print(f"Error: Unsupported operation. Please choose from {', '.join(valid_operations)}")


def _safe_divide(num1, num2):
    """Safely divide with error handling."""
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        return None
    return divide(num1, num2)


OPERATIONS = {
    '+': lambda n1, n2: add(n1, n2),
    '-': lambda n1, n2: subtract(n1, n2),
    '*': lambda n1, n2: multiply(n1, n2),
    '/': _safe_divide,
    'cos': lambda n1, n2: cosine(n1),
}


def perform_calculation(num1, num2, operation):
    """Perform the calculation based on the operation."""
    if operation in OPERATIONS:
        return OPERATIONS[operation](num1, num2)
    return None


def _display_result(num1, operation, result, num2=None):
    """Format and display calculation result."""
    print("=" * 40)
    if operation == 'cos':
        print(f"Result: cos({num1}) = {result}")
    else:
        print(f"Result: {num1} {operation} {num2} = {result}")
    print("=" * 40)


def main():
    """Main function to run the calculator."""
    print("=" * 40)
    print("Welcome to the Python Calculator!")
    print("=" * 40)

    num1 = get_first_number()
    operation = get_operation()

    if operation == 'cos':
        result = perform_calculation(num1, None, operation)
        if result is not None:
            _display_result(num1, operation, result)
    else:
        num2 = get_second_number()
        result = perform_calculation(num1, num2, operation)
        if result is not None:
            _display_result(num1, operation, result, num2)


if __name__ == "__main__":
    main()
