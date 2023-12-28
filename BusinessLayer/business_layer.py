# business_layer.py
from random import uniform
import time
from DataLayer.data_layer import update_in_db_min_value, update_in_db_max_value



def simulate_trades(currency_pairs):
    while True:
        for pair in currency_pairs:
            min_value = pair["MinValue"]
            max_value = pair["MaxValue"]

            value_range = (max_value - min_value) * 0.1
            current_value = uniform(min_value - value_range, max_value + value_range)
            pair["CurrentValue"] = current_value

            # Update the min and max values in currency_pairs list
            if current_value < min_value:
                pair["MinValue"] = current_value
            elif current_value > max_value:
                pair["MaxValue"] = current_value

            # Update the database if the conditions are met
            if current_value < min_value:
                update_in_db_min_value(pair["Pair"], abs(current_value))
            elif current_value > max_value:
                update_in_db_max_value(pair["Pair"], abs(current_value))

            print(f"Trade: {pair['Pair']} - Current Value: {pair['CurrentValue']:.4f}")

        time.sleep(2)

