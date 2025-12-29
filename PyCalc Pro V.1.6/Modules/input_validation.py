"""Input validation for calculator expressions."""

from decimal import Decimal, InvalidOperation


def is_valid_input(text):
    """Check if input contains only safe characters."""
    allowed_chars = set('0123456789+-*/%().pi,')
    return all(c in allowed_chars or c.isspace() for c in text.lower())


def has_invalid_patterns(expression):
    """Check for common invalid patterns."""
    invalid_patterns = ['++', '--', '**', '//']
    return any(pattern in expression for pattern in invalid_patterns)


def validate_and_parse_expression(expression):
    """
    Validate expression and return errors if found.
    
    Args:
        expression: The user's input expression
    
    Returns:
        (is_valid, message) tuple
    """
    expression = expression.strip()
    
    if not expression:
        return True, ""
    
    # Check for invalid characters
    if not is_valid_input(expression):
        return False, "Error: Invalid characters in input"
    
    # Check for invalid patterns
    if has_invalid_patterns(expression):
        return False, "Error: Invalid expression"
    
    return True, ""


def sanitize_expression(expression):
    """Prepare expression for evaluation."""
    return expression.replace(',', '.')
