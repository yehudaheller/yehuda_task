"""
ui_layer.py - User Interface (UI) layer script for a Stock Exchange application.

This script uses the Tkinter library to create a simple UI for displaying currency pair data in a Treeview widget. It also utilizes threading to run a simulation of trades in the background.

Usage:
    $ python ui_layer.py

Dependencies:
    - Tkinter: Python's standard GUI (Graphical User Interface) package.

Functions:
    - update_ui: Updates the UI by clearing the existing data in the Treeview and inserting new data from the provided currency_pairs.

Main Flow:
    1. Initializes data by loading currency pair information using the 'load_currency_pair_data' function from 'DataLayer.data_layer'.
    2. Creates the main Tkinter window titled "Stock Exchange App".
    3. Creates a Treeview widget to display currency pair information with columns: "Currency Pair", "Min Value", "Max Value", and "Current Value".
    4. Starts a thread using the 'simulate_trades' function from 'BusinessLayer.business_layer' to simulate trades in the background.
    5. Updates the UI with simulated trade data using the 'update_ui' function.
    6. Runs the Tkinter event loop to display the UI.

Note:
    The script uses threading to allow the UI to be updated concurrently while the background simulation of trades is ongoing.

Example:
    $ python ui_layer.py
"""

import tkinter as tk
from tkinter import ttk
from threading import Thread
import sys
import os

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Now you can use relative imports
from DataLayer.data_layer import load_currency_pair_data
from BusinessLayer.business_layer import simulate_trades

# Remove the parent directory from the Python path to avoid interference
sys.path.remove(parent_dir)


def update_ui(tree, currency_pairs):
    """
    Updates the UI with currency pair data in the Treeview widget.

    Clears existing data and inserts new data from the provided currency_pairs.

    Args:
        tree (ttk.Treeview): The Treeview widget to update.
        currency_pairs (list): List of currency pair dictionaries.
    """
    # Clear existing data in the Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Update with new data
    for pair in currency_pairs:
        tree.insert("", "end", text=pair["Pair"],
                    values=(pair["MinValue"], pair["MaxValue"], pair.get("CurrentValue", "")))

    # Schedule the next update after 2000 milliseconds (2 seconds)
    root.after(2000, update_ui, tree, currency_pairs)


if __name__ == "__main__":
    # Initialize data
    currency_pairs = load_currency_pair_data()

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Stock Exchange App")

    # Create and place a Treeview for displaying data
    tree = ttk.Treeview(root, columns=("Pair", "Min Value", "Max Value", "Current Value"))
    tree.heading("#0", text="Currency Pair")
    tree.heading("#1", text="Min Value")
    tree.heading("#2", text="Max Value")
    tree.heading("#3", text="Current Value")
    tree.pack(pady=10)

    # Start BusinessLayer thread to simulate trades
    Thread(target=simulate_trades, args=(currency_pairs,), daemon=True).start()

    # Update the UI with simulated trade data
    update_ui(tree, currency_pairs)

    # Run the Tkinter event loop
    root.mainloop()
