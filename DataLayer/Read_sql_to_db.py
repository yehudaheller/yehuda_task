"""
Read_sql_to_db.py - Script to initialize an SQLite database for a Stock Exchange application.

This script connects to an SQLite database, creates necessary tables ('Currency' and 'CurrencyPair') if they don't exist, clears existing data from these tables, and executes an initialization SQL script ('init_db.sql').

Usage:
    $ python Read_sql_to_db.py

Dependencies:
    - sqlite3: Python's built-in module for working with SQLite databases.

Functions:
    - initialize_database: Connects to the SQLite database, checks for table existence, creates tables if needed, clears existing data, and executes the 'init_db.sql' script to populate the database.

Main Flow:
    1. Connects to the SQLite database located at 'DataLayer/stock_exchange.db'.
    2. Checks if 'Currency' and 'CurrencyPair' tables exist; if not, creates them.
    3. Clears existing data from 'Currency' and 'CurrencyPair' tables.
    4. Reads and executes the 'init_db.sql' script to initialize the database with default data.
    5. Commits changes and closes the database connection.

Note:
    - The script assumes the presence of an 'init_db.sql' script in the 'DataLayer' directory for database initialization.

Example:
    $ python Read_sql_to_db.py
"""

import sqlite3
import os

def initialize_database():
    """
    Initializes the SQLite database for the Stock Exchange application.

    Connects to the database, creates tables if not exist, clears existing data, and executes 'init_db.sql' script.

    The script assumes the presence of 'init_db.sql' in the 'DataLayer' directory.

    Note: This script is intended to be run independently for database initialization.

    Example:
        $ python Read_sql_to_db.py
    """
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
