"""
PyCalc Pro - Calculator Operations Module

This module contains all mathematical operations and conversions.
"""

import math
import re
from decimal import Decimal, InvalidOperation


def convert_mass(value, initial_unit, final_unit):
    """Convert mass between different units."""
    conversions = {
        'kg': 1,
        'g': 1000,
        'mg': 1e6,
        'lb': 2.20462,
        'oz': 35.274,
        'ton': 0.001,
        'tonne': 0.001
    }
    return value * (conversions[final_unit] / conversions[initial_unit])


def convert_length(value, initial_unit, final_unit):
    """Convert length between different units."""
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
    return value * (conversions[final_unit] / conversions[initial_unit])


def evaluate_expression(expression, save_callback=None):
    """
    Safely evaluate calculator expression with Decimal precision.
    
    - Prevents arbitrary code execution
    - Uses Decimal for precision (no floating-point artifacts)
    - Returns user-friendly error messages
    
    Args:
        expression: String containing the mathematical expression
        save_callback: Optional callback function to save the operation
    
    Returns:
        String containing the result or error message
    """
    try:
        original_expression = expression  # Save original expression for logging
        expression = expression.strip()
        if not expression:
            return ""
        
        expression = expression.replace(',', '.')
        original_expression = expression  # Update original after comma replacement
        
        # Input validation: only allow safe characters
        allowed_chars = set('0123456789+-*/%().piabcgilnoqrstx^|')
        for c in expression.lower():
            if c not in allowed_chars and not c.isspace():
                return "Error: Invalid characters in input"
        
        # Prevent multiple operations without operands
        if '++' in expression or '--' in expression or '**' in expression or '//' in expression:
            return "Error: Invalid expression"

        # Replace pi with its Decimal value
        expression = expression.replace('pi', str(Decimal(str(math.pi))))

        # Convert all numbers in expression to Decimal
        def convert_to_decimal(match):
            num_str = match.group(0)
            try:
                Decimal(num_str)
                return f"Decimal('{num_str}')"
            except:
                return num_str
        
        # Match all numbers (with decimal points)
        expression = re.sub(r'\d+\.?\d*', convert_to_decimal, expression)

        # Handle percentage operator
        if '%' in expression:
            for operator in ['+', '-', '*', '/']:
                if operator in expression:
                    parts = expression.split(operator)
                    if len(parts) == 2:
                        left, right = parts
                        if '%' in right:
                            right_val = right.replace('%', '').strip()
                            try:
                                result = eval(left, {"__builtins__": None, "Decimal": Decimal}) * eval(right_val, {"__builtins__": None, "Decimal": Decimal}) / Decimal(100)
                                expression = f"({left}){operator}({result})"
                            except (InvalidOperation, ValueError):
                                return "Error: Invalid expression"
                    break

        # Define safe functions for evaluation
        safe_namespace = {
            "Decimal": Decimal,
            "abs": abs,
            "sqrt": lambda x: Decimal(str(math.sqrt(float(x)))),
            "cos": lambda x: Decimal(str(math.cos(math.radians(float(x))))),
            "sin": lambda x: Decimal(str(math.sin(math.radians(float(x))))),
            "tan": lambda x: Decimal(str(math.tan(math.radians(float(x))))),
            "log": lambda x: Decimal(str(math.log10(float(x)))),
            "ln": lambda x: Decimal(str(math.log(float(x)))),
        }
        
        # Evaluate with restricted namespace
        result = eval(expression, {"__builtins__": None}, safe_namespace)
        
        # Convert result to Decimal if not already
        if not isinstance(result, Decimal):
            result = Decimal(str(result))
        
        # Format result: remove trailing zeros and unnecessary decimal point
        result_str = str(result)
        if '.' in result_str:
            result_str = result_str.rstrip('0').rstrip('.')
        
        if save_callback:
            save_callback(f"{original_expression} = {result_str}")
        
        return result_str
        
    except ZeroDivisionError:
        return "Error: Division by zero"
    except ValueError:
        return "Error: Invalid number format"
    except SyntaxError:
        return "Error: Invalid expression"
    except TypeError:
        return "Error: Invalid input"
    except Exception as e:
        return "Error: Invalid input"
