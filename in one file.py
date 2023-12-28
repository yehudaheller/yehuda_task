import tkinter as tk
from tkinter import ttk
import random
from threading import Thread
import time

class DataLayer:
    @staticmethod
    def load_currency_data():
        # Load data into Currency table (for simplicity, hardcoded values)
        return [
            {"Country": "United States", "Name": "Dollar", "Abbreviation": "USD"},
            {"Country": "Eurozone", "Name": "Euro", "Abbreviation": "EUR"},
            {"Country": "Japan", "Name": "Yen", "Abbreviation": "JPY"},
            {"Country": "United Kingdom", "Name": "Pound", "Abbreviation": "GBP"},
            {"Country": "Israel", "Name": "Shekel", "Abbreviation": "ILS"},
        ]

    @staticmethod
    def load_currency_pair_data():
        # Load data into CurrencyPair table (for simplicity, hardcoded values)
        return [
            {"Pair": "USD/EUR", "MinValue": 1.1, "MaxValue": 1.2},
            {"Pair": "USD/JPY", "MinValue": 100, "MaxValue": 110},
            {"Pair": "EUR/GBP", "MinValue": 0.8, "MaxValue": 0.9},
            {"Pair": "USD/ILS", "MinValue": 3.5, "MaxValue": 3.9},
        ]

    @staticmethod
    def save_currency_pair_data(pair_data):
        # Save data (for simplicity, print instead of using a database)
        print(f"Saved: {pair_data}")

class BusinessLayer:
    @staticmethod
    def simulate_trades():
        while True:
            # Simulate trade and value changes
            for pair in currency_pairs:
                pair["CurrentValue"] = random.uniform(pair["MinValue"], pair["MaxValue"])
                print(f"Trade: {pair['Pair']} - Current Value: {pair['CurrentValue']:.4f}")

            time.sleep(2)  # Sleep for 2 seconds

class UILayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Exchange App")

        # Create and place a Treeview for displaying data
        self.tree = ttk.Treeview(root, columns=("Pair", "Min Value", "Max Value", "Current Value"))
        self.tree.heading("#0", text="Currency Pair")
        self.tree.heading("#1", text="Min Value")
        self.tree.heading("#2", text="Max Value")
        self.tree.heading("#3", text="Current Value")
        self.tree.pack(pady=10)

        # Start BusinessLayer thread to simulate trades
        Thread(target=BusinessLayer.simulate_trades, daemon=True).start()

        # Update the UI with simulated trade data
        self.update_ui()

    def update_ui(self):
        # Clear existing data in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Update with new data
        for pair in currency_pairs:
            self.tree.insert("", "end", text=pair["Pair"], values=(pair["MinValue"], pair["MaxValue"], pair.get("CurrentValue", "")))

        # Schedule the next update after 2000 milliseconds (2 seconds)
        self.root.after(2000, self.update_ui)

if __name__ == "__main__":
    # Initialize data from DataLayer
    currencies = DataLayer.load_currency_data()
    currency_pairs = DataLayer.load_currency_pair_data()

    # Create the main Tkinter window
    root = tk.Tk()

    # Initialize the UI layer
    ui = UILayer(root)

    # Run the Tkinter event loop
    root.mainloop()
