# data_layer.py
from random import uniform

def load_currency_data():
    # Load data into Currency table (for simplicity, hardcoded values)
    return [
        {"Country": "United States", "Name": "Dollar", "Abbreviation": "USD"},
        {"Country": "Eurozone", "Name": "Euro", "Abbreviation": "EUR"},
        {"Country": "Japan", "Name": "Yen", "Abbreviation": "JPY"},
        {"Country": "Israel", "Name": "Shekel", "Abbreviation": "ILS"},  # Added for ILS
    ]

def load_currency_pair_data():
    # Load data into CurrencyPair table (for simplicity, hardcoded values)
    return [
        {"Pair": "USD/EUR", "MinValue": 1.1, "MaxValue": 1.2},
        {"Pair": "USD/JPY", "MinValue": 100, "MaxValue": 110},
        {"Pair": "USD/ILS", "MinValue": 3.5, "MaxValue": 3.8},  # Added for USD/ILS
    ]

def save_currency_pair_data(pair_data):
    # Save data (for simplicity, print instead of using a database)
    print(f"Saved: {pair_data}")
