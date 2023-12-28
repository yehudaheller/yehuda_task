# data_layer.py
import sqlite3

def load_currency_data():
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
    # Connect to SQLite database
    conn = sqlite3.connect("DataLayer/stock_exchange.db")
    cursor = conn.cursor()

    # Save data to CurrencyPair table
    cursor.executemany("INSERT OR REPLACE INTO CurrencyPair (Pair, MinValue, MaxValue) VALUES (?, ?, ?)",
                      [(pair["Pair"], pair["MinValue"], pair["MaxValue"]) for pair in pair_data])

    # Commit changes and close database connection
    conn.commit()
    conn.close()