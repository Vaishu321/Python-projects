#Let’s create simple helper functions for
#our sales analysis. In your sales-analysis folder, create a new file called helpers.py


def calculate_total(quantity, price):
    """Calculate total for a single item"""
    return quantity * price

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"