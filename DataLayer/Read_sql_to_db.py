# Read_sql_to_db.py
import sqlite3

def initialize_database():
    # Connect to SQLite database
    conn = sqlite3.connect("DataLayer/stock_exchange.db")
    cursor = conn.cursor()

    # Clear existing data from Currency and CurrencyPair tables
    # Without deleting otherwise the database will be filled with duplicate tables
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
    initialize_database()