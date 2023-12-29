"""
data_layer.py - Data layer script for interacting with the SQLite database in a Stock Exchange application.

This script provides functions to load, save, and update data related to currency and currency pairs in the SQLite database.

Functions:
    - load_currency_data: Loads data from the 'Currency' table in the database.
    - load_currency_pair_data: Loads data from the 'CurrencyPair' table in the database.
    - save_currency_pair_data: Saves data to the 'CurrencyPair' table in the database.
    - update_in_db_min_value: Updates the minimum value for a specific currency pair in the 'CurrencyPair' table.
    - update_in_db_max_value: Updates the maximum value for a specific currency pair in the 'CurrencyPair' table.

Note:
    - The script assumes the presence of an SQLite database named 'stock_exchange.db' in the same directory for loading currency data.
    - For loading, saving, and updating currency pair data, the script connects to the 'stock_exchange.db' database located in the 'DataLayer' directory.

Example:
    - Usage of these functions is typically done within the Stock Exchange application to interact with the underlying database.
"""

import sqlite3

def load_currency_data():
    """
    Loads data from the 'Currency' table in the database.

    Returns:
        list: A list of dictionaries, where each dictionary represents a currency with 'Country', 'Name', and 'Abbreviation' attributes.
    """
    # Connect to SQLite database
    conn = sqlite3.connect("stock_exchange.db")
    cursor = conn.cursor()

    # Fetch data from Currency table
    cursor.execute("SELECT * FROM Currency")
    currency_data = cursor.fetchall()

    # Close database connection
    conn.close()

    return [{"Country": country, "Name": name, "Abbreviation": abbreviation} for country, name, abbreviation in currency_data]

def load_currency_pair_data():
    """
    Loads data from the 'CurrencyPair' table in the database.

    Returns:
        list: A list of dictionaries, where each dictionary represents a currency pair with 'Pair', 'MinValue', and 'MaxValue' attributes.
    """
    # Connect to SQLite database
    conn = sqlite3.connect("DataLayer/stock_exchange.db")
    cursor = conn.cursor()

    # Fetch data from CurrencyPair table
    cursor.execute("SELECT * FROM CurrencyPair")
    currency_pair_data = cursor.fetchall()

    # Close database connection
    conn.close()

    return [{"Pair": pair, "MinValue": min_value, "MaxValue": max_value} for pair, min_value, max_value in currency_pair_data]

def save_currency_pair_data(pair_data):
    """
    Saves data to the 'CurrencyPair' table in the database.

    Args:
        pair_data (list): A list of dictionaries, where each dictionary represents a currency pair with 'Pair', 'MinValue', and 'MaxValue' attributes.
    """
    # Connect to SQLite database
    conn = sqlite3.connect("DataLayer/stock_exchange.db")
    cursor = conn.cursor()

    # Save data to CurrencyPair table
    cursor.executemany("INSERT OR REPLACE INTO CurrencyPair (Pair, MinValue, MaxValue) VALUES (?, ?, ?)",
                      [(pair["Pair"], pair["MinValue"], pair["MaxValue"]) for pair in pair_data])

    # Commit changes and close database connection
    conn.commit()
    conn.close()

def update_in_db_min_value(pair, new_min_value):
    """
    Updates the minimum value for a specific currency pair in the 'CurrencyPair' table.

    Args:
        pair (str): The currency pair identifier.
        new_min_value (float): The new minimum value for the currency pair.
    """
    # Connect to SQLite database
    conn = sqlite3.connect("DataLayer/stock_exchange.db")
    cursor = conn.cursor()

    # Update the minimum value in CurrencyPair table
    cursor.execute("UPDATE CurrencyPair SET MinValue = ? WHERE Pair = ?", (new_min_value, pair))

    # Commit changes and close database connection
    conn.commit()
    conn.close()

def update_in_db_max_value(pair, new_max_value):
    """
    Updates the maximum value for a specific currency pair in the 'CurrencyPair' table.

    Args:
        pair (str): The currency pair identifier.
        new_max_value (float): The new maximum value for the currency pair.
    """
    # Connect to SQLite database
    conn = sqlite3.connect("DataLayer/stock_exchange.db")
    cursor = conn.cursor()

    # Update the maximum value in CurrencyPair table
    cursor.execute("UPDATE CurrencyPair SET MaxValue = ? WHERE Pair = ?", (new_max_value, pair))

    # Commit changes and close database connection
    conn.commit()
    conn.close()
