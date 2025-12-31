"""Calculator operations and math functions."""

import math
from decimal import Decimal, InvalidOperation


def evaluate_expression(expression):
    """
    Safely evaluate calculator expression with Decimal precision.
    
    Args:
        expression: The calculator expression (already validated)
    
    Returns:
        Formatted result string or error message
    """
    try:
        expression = expression.strip()
        if not expression:
            return ""
        
        # Prepare expression
        expression = expression.replace(',', '.')
        
        # Handle percentage operator
        expression = handle_percentage(expression)
        
        # Replace pi with its Decimal value
        expression = expression.replace('pi', str(Decimal(str(math.pi))))
        
        # Define safe functions for evaluation
        safe_functions = {
            "abs": abs,
            "sqrt": lambda x: Decimal(str(math.sqrt(float(x)))),
            "cos": lambda x: Decimal(str(math.cos(math.radians(float(x))))),
            "sin": lambda x: Decimal(str(math.sin(math.radians(float(x))))),
            "tan": lambda x: Decimal(str(math.tan(math.radians(float(x))))),
            "log": lambda x: Decimal(str(math.log10(float(x)))),
            "ln": lambda x: Decimal(str(math.log(float(x)))),
        }
        
        # Evaluate with restricted namespace
        result = eval(expression, {"__builtins__": None}, safe_functions)
        
        # Convert result to Decimal if not already
        if not isinstance(result, Decimal):
            result = Decimal(str(result))
        
        # Format result: remove trailing zeros
        result_str = str(result)
        if '.' in result_str:
            result_str = result_str.rstrip('0').rstrip('.')
        
        return result_str
        
    except ZeroDivisionError:
        return "Error: Division by zero"
    except ValueError:
        return "Error: Invalid number format"
    except SyntaxError:
        return "Error: Invalid expression"
    except Exception:
        return "Error: Invalid input"


def handle_percentage(expression):
    """Handle percentage calculations in expressions."""
    if '%' not in expression:
        return expression
    
    for operator in ['+', '-', '*', '/']:
        if operator in expression:
            parts = expression.split(operator)
            if len(parts) == 2:
                left, right = parts
                if '%' in right:
                    right_val = right.replace('%', '').strip()
                    try:
                        left_decimal = Decimal(left.strip())
                        right_decimal = Decimal(right_val)
                        result = left_decimal * right_decimal / Decimal(100)
                        expression = f"{left}{operator}{result}"
                    except (InvalidOperation, ValueError):
                        return expression
            break
    
    return expression


def convert_mass(value, initial_unit, final_unit):
    """Convert between mass units."""
    conversions = {
        'kg': 1,
        'g': 1000,
        'mg': 1e6,
        'lb': 2.20462,
        'oz': 35.274,
        'ton': 0.001,
        'tonne': 0.001
    }
    try:
        return value * (conversions[final_unit] / conversions[initial_unit])
    except KeyError:
        return None


def convert_length(value, initial_unit, final_unit):
    """Convert between length units."""
    conversions = {
        'km': 0.001,
        'm': 1,
        'cm': 100,
        'mm': 1000,
        'µm': 1e6,
        'in': 39.3701,
        'ft': 3.28084,
        'yd': 1.09361,
        'mile': 0.000621371
    }
    try:
        return value * (conversions[final_unit] / conversions[initial_unit])
    except KeyError:
        return None
