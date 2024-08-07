def safe_divide(numerator, denominator):
    """Perform division with error handling for zero division and non-numeric input."""
    try:
        # Attempt to convert to float
        num = float(numerator)
        denom = float(denominator)
        
        # Perform the division
        result = num / denom
        return f"The result of the division is {result:.2f}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
