# business_layer.py
from random import uniform
import time

def simulate_trades(currency_pairs):
    while True:
        # Simulate trade and value changes
        for pair in currency_pairs:
            pair["CurrentValue"] = uniform(pair["MinValue"], pair["MaxValue"])
            print(f"Trade: {pair['Pair']} - Current Value: {pair['CurrentValue']:.4f}")

        time.sleep(2)  # Sleep for 2 seconds
