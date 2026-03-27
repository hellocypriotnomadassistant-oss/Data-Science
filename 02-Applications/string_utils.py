import re

def format_price(price):
    """Formats a numeric price into a string with 2 decimal places."""
    return f"Price: ${price:.2f}"

def format_user(name, number):
    """Returns a greeting message for a specific user and ID."""
    return f"Hello {name}, your ID is {number}"

def clean_text(text):
    """Cleans the text: trims whitespace and converts to lowercase."""
    return text.strip().lower()

def has_pattern(text, pattern):
    """Checks if a specific regex pattern exists within the text."""
    return bool(re.search(pattern, text))

def format_percentage(value):
    """Converts a decimal value to a percentage format (e.g., 0.25 -> 25.00%)."""
    return f"{value:.2%}"