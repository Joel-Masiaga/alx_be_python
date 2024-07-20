def perform_operation(num1, num2):

    if perform_operation == 'add':
        return num1 + num2
    elif perform_operation == 'subtract':
        return num1 - num2
    elif perform_operation == 'multiply':
        return num1 * num2
    elif perform_operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."
