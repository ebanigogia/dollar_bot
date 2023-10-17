import helper
import logging
from matplotlib import pyplot as plt

def calculate_total_expenses(user_history):
    total_expenses = {}
    for record in user_history:
        date, category, amount = record.split(",")
        amount = float(amount)
        if category not in total_expenses:
            total_expenses[category] = amount
        else:
            total_expenses[category] += amount
    return total_expenses
