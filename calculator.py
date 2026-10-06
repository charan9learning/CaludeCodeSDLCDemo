"""
Simple Python Calculator
A beginner-friendly calculator that performs basic arithmetic operations.
"""


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


def get_first_number():
    """Get and validate the first number from user."""
    while True:
        user_input = input("Enter first number: ")
        if is_valid_number(user_input):
            return float(user_input)
        else:
            print("Error: Please enter a valid number.")


def get_second_number():
    """Get and validate the second number from user."""
    while True:
        user_input = input("Enter second number: ")
        if is_valid_number(user_input):
            return float(user_input)
        else:
            print("Error: Please enter a valid number.")


def get_operation():
    """Get and validate the operation from user."""
    valid_operations = ['+', '-', '*', '/']
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in valid_operations:
            return operation
        else:
            print(f"Error: Unsupported operation. Please choose from {', '.join(valid_operations)}")


def perform_calculation(num1, num2, operation):
    """Perform the calculation based on the operation."""
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
        if result is None:
            print("Error: Cannot divide by zero.")
            return None
        return result


def main():
    """Main function to run the calculator."""
    print("=" * 40)
    print("Welcome to the Python Calculator!")
    print("=" * 40)

    num1 = get_first_number()
    num2 = get_second_number()
    operation = get_operation()

    result = perform_calculation(num1, num2, operation)

    if result is not None:
        print("=" * 40)
        print(f"Result: {num1} {operation} {num2} = {result}")
        print("=" * 40)


if __name__ == "__main__":
    main()
