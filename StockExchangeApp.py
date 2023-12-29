"""
StockExchangeApp.py - Automated script for initializing a database and running a UI layer for a stock exchange application.

This script provides a convenient way to automate the initialization of a database and the execution of a UI layer for a stock exchange application. It uses subprocess to run other Python scripts responsible for database initialization and UI layer execution.

Usage:
    $ python StockExchangeApp.py

Functions:
    - run_init_db: Initializes the database by calling the 'Read_sql_to_db.py' script located in the 'DataLayer' directory.
    - run_ui_layer: Executes the UI layer by calling the 'ui_layer.py' script located in the 'UILayer' directory.

Note:
    This script is intended to be run as the main module. It sequentially calls the 'run_init_db' function to initialize the database and the 'run_ui_layer' function to execute the UI layer.

Example:
    $ python StockExchangeApp.py
"""

import subprocess

def run_init_db():
    """
    Initializes the database by calling the 'Read_sql_to_db.py' script.

    Prints status messages before and after the initialization process.
    """
    print("Initializing database...")
    subprocess.run(["python", "DataLayer/Read_sql_to_db.py"])
    print("Database initialization complete.")

def run_ui_layer():
    """
    Executes the UI layer by calling the 'ui_layer.py' script.

    Prints status messages before and after the execution of the UI layer.
    """
    print("Running UI layer...")
    subprocess.run(["python", "UILayer/ui_layer.py"])
    print("UI layer execution complete.")

if __name__ == "__main__":
    # Run the database initialization and UI layer sequentially when the script is executed.
    run_init_db()
    run_ui_layer()
