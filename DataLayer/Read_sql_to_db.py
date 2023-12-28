# Read_sql_to_db.py
import sqlite3
import os

def initialize_database():
    # Connect to SQLite database
    database_path = "DataLayer/stock_exchange.db"
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Check if tables exist, and create them if not
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Currency'")
    if not cursor.fetchone():
        print("Creating Currency table...")
        cursor.execute("CREATE TABLE IF NOT EXISTS Currency (Country TEXT, Name TEXT, Abbreviation TEXT)")

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='CurrencyPair'")
    if not cursor.fetchone():
        print("Creating CurrencyPair table...")
        cursor.execute("CREATE TABLE IF NOT EXISTS CurrencyPair (Pair TEXT, MinValue REAL, MaxValue REAL)")

    # Clear existing data from Currency and CurrencyPair tables
    cursor.execute("DELETE FROM Currency")
    cursor.execute("DELETE FROM CurrencyPair")

    # Read and execute init_db.sql script
    with open("DataLayer/init_db.sql", "r") as script_file:
        script = script_file.read()
        cursor.executescript(script)

    # Commit changes and close database connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Initializing database...")
    initialize_database()
    print("Database initialization complete.")
