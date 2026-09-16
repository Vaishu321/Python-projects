# At first the formatting was like this but saving - Ruff corrected the formatting itself

"""import os
def   calculate_total(items):
    total=0
    for item in items:
        total+=item['price']*item['quantity']
    return total

shopping_cart=[{'name':'apple','price':0.5,'quantity':6},{'name':'banana','price':0.3,'quantity':8}]
print(calculate_total(shopping_cart))"""

import os


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


shopping_cart = [
    {"name": "apple", "price": 0.5, "quantity": 6},
    {"name": "banana", "price": 0.3, "quantity": 8},
]
print(calculate_total(shopping_cart))


"""Ruff follows Python’s style guide (PEP 8) automatically:
4 spaces for indentation
Spaces around operators (x = 1, not x=1)
Two blank lines between functions
Maximum line length of 88 characters
You don’t need to memorize these - Ruff handles them for you!"""
