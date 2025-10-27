"""
Inventory Management System
Performs add, remove, save, and load operations with proper logging,
error handling, and static code analysis compliance.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global variable for stock
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the stock.
    """
    if logs is None:
        logs = []

    if not isinstance(item, str):
        logging.warning("Ignored invalid item type: %s", item)
        return

    if not isinstance(qty, int):
        logging.warning("Ignored invalid quantity type for %s: %s", item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s to stock.", qty, item)


def remove_item(item, qty):
    """
    Remove an item from the stock safely.
    """
    try:
        if item not in stock_data:
            logging.warning("Attempted to remove non-existent item: %s", item)
            return

        if not isinstance(qty, int) or qty <= 0:
            logging.warning("Invalid quantity for removal: %s", qty)
            return

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Removed item '%s' completely from stock.", item)
        else:
            logging.info("Removed %d of %s. Remaining: %d", qty, item, stock_data[item])
    except KeyError as e:
        logging.error("Error removing item %s: %s", item, e)


def get_qty(item):
    """
    Get quantity of an item.
    """
    return stock_data.get(item, 0)


def load_data(file_name="inventory.json"):
    """
    Load inventory data from a JSON file.
    """
    global stock_data
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
            logging.info("Data loaded successfully from file.")
    except FileNotFoundError:
        logging.warning("File not found. Starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError as e:
        logging.error("Error decoding JSON file: %s", e)
        stock_data = {}
    except OSError as e:
        logging.error("File access error while loading data: %s", e)


def save_data(file_name="inventory.json"):
    """
    Save inventory data to a JSON file.
    """
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=4)
            logging.info("Data saved successfully to file.")
    except (OSError, TypeError) as e:
        logging.error("Error saving data: %s", e)


def print_data():
    """
    Print all stock items.
    """
    print("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """
    Return list of items below the threshold quantity.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """
    Main function for testing the inventory system.
    """
    logging.info("Inventory system started.")

    add_item("apple", 10)
    add_item("banana", 2)
    add_item("orange", 1)
    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    load_data()
    print_data()

    logging.info("Inventory system completed successfully.")


if __name__ == "__main__":
    main()
