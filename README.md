yehuda heller task


The Stock Exchange App is a simple application that simulates trades for currency pairs. It consists of three main components: Read_sql_to_db.py for initializing the SQLite database, data_layer.py for interacting with the database, and ui_layer.py for creating a Tkinter-based user interface. Trades are simulated in the business_layer.py script.
Generates random numbers for each currency, updates in a database, and in the display of the software window the new minimum and maximum if they have changed.


<h1>Usage</h1>

Run the Stock Exchange App:
Run StockExchangeApp.py to start the application. This script loads currency data, initializes the Tkinter UI, and simulates trades in the background.

>> python StockExchangeApp.py

UI Layer:
The Tkinter-based UI displays currency pair information, including minimum and maximum values. Trades are simulated in the background, and the UI is updated every 2 seconds.

<h1>Files</h1>

- Read_sql_to_db.py:
Initializes the SQLite database by creating tables and executing an initialization SQL script.

- data_layer.py:
Provides functions to load, save, and update data related to currency and currency pairs in the SQLite database.

- business_layer.py:
Simulates trades for currency pairs, updating their current values and the underlying database as needed.

- ui_layer.py:
Creates a Tkinter-based UI to display currency pair information and visualizes simulated trades.

- init_db.sql:
SQL script containing initial data for populating the database tables.

Dependencies
sqlite3: Python's built-in module for working with SQLite databases.
tkinter: Python's standard GUI package.
