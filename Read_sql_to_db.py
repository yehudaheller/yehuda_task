# init_db.py
import sqlite3

def initialize_database():
    # Connect to SQLite database
    conn = sqlite3.connect("stock_exchange.db")
    cursor = conn.cursor()

    # Read and execute init_db.sql script
    with open("init_db.sql", "r") as script_file:
        script = script_file.read()
        cursor.executescript(script)

    # Commit changes and close database connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
