# ui_layer.py
import tkinter as tk
from tkinter import ttk
from threading import Thread
from data_layer import load_currency_pair_data
from business_layer import simulate_trades

def update_ui(tree, currency_pairs):
    # Clear existing data in the Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Update with new data
    for pair in currency_pairs:
        tree.insert("", "end", text=pair["Pair"], values=(pair["MinValue"], pair["MaxValue"], pair.get("CurrentValue", "")))

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
