# utils.py
"""
Utility functions for data handling.
"""

import json
import os

HOTELS_FILE = "hotels.json"
CUSTOMERS_FILE = "customers.json"
RESERVATIONS_FILE = "reservations.json"


def load_data(file_path: str):
    """Load data from a JSON file."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print(f"Error loading {file_path}, initializing empty.")
                return {}
    return {}


def save_data(file_path: str, data):
    """Save data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# Creating test JSON files with initial data
initial_hotels = {
    "Grand Hotel": {"location": "New York", "rooms": 150},
    "Ocean View": {"location": "Miami", "rooms": 100}
}
save_data(HOTELS_FILE, initial_hotels)

initial_customers = {
    "Alice Smith": {"email": "alice@example.com"},
    "Bob Johnson": {"email": "bob@example.com"}
}
save_data(CUSTOMERS_FILE, initial_customers)

initial_reservations = {
    "Alice Smith_Grand Hotel": {"customer": "Alice Smith",
                                "hotel": "Grand Hotel"},
    "Bob Johnson_Ocean View": {"customer": "Bob Johnson",
                               "hotel": "Ocean View"}
}
save_data(RESERVATIONS_FILE, initial_reservations)
