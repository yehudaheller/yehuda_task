"""
business_layer.py - Business layer script for simulating trades in a Stock Exchange application.

This script contains a function to simulate trades for currency pairs. It updates the current values of currency pairs and, if conditions are met, updates the minimum and maximum values in both the currency_pairs list and the underlying database.

Functions:
    - simulate_trades: Simulates trades for currency pairs by updating their current values and, if needed, updating the database.

Dependencies:
    - random: Python's built-in module for generating random numbers.
    - time: Python's built-in module for handling time-related operations.
    - DataLayer.data_layer: Module containing functions to update minimum and maximum values in the database.

Main Flow:
    - In a continuous loop, the function simulates trades for each currency pair.
    - For each pair, it generates a random current value within a range based on the minimum and maximum values.
    - It updates the currency_pairs list with the new current value and adjusts the minimum and maximum values if necessary.
    - If the current value is below the minimum value or above the maximum value, it updates the corresponding values in the database using functions from the data_layer module.
    - The trade details are printed to the console.
    - The loop pauses for 2 seconds before repeating.

Example:
    - The 'simulate_trades' function is typically called in a separate thread in the Stock Exchange application to continuously update currency pair values.

Note:
    - The script assumes the availability of a currency_pairs list containing dictionaries with 'Pair', 'MinValue', and 'MaxValue' attributes.
"""

from random import uniform
import time
from DataLayer.data_layer import update_in_db_min_value, update_in_db_max_value

def simulate_trades(currency_pairs):
    """
    Simulates trades for currency pairs.

    Updates the current values of currency pairs and, if conditions are met,
    updates the minimum and maximum values in both the currency_pairs list and the underlying database.

    Args:
        currency_pairs (list): A list of dictionaries representing currency pairs with 'Pair', 'MinValue', and 'MaxValue' attributes.
    """
    while True:
        for pair in currency_pairs:
            min_value = pair["MinValue"]
            max_value = pair["MaxValue"]

            value_range = (max_value - min_value) * 0.1
            current_value = uniform(min_value - value_range, max_value + value_range)
            pair["CurrentValue"] = current_value

            # Update the min and max values in currency_pairs list
            if current_value < min_value:
                pair["MinValue"] = current_value
            elif current_value > max_value:
                pair["MaxValue"] = current_value

            # Update the database if the conditions are met
            if current_value < min_value:
                update_in_db_min_value(pair["Pair"], abs(current_value))
            elif current_value > max_value:
                update_in_db_max_value(pair["Pair"], abs(current_value))

            print(f"Trade: {pair['Pair']} - Current Value: {pair['CurrentValue']:.4f}")

        time.sleep(2)
