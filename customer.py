# customer.py
"""
Module for managing customer information.
"""

from utils import load_data, save_data, CUSTOMERS_FILE


class Customer:
    """Class representing a customer."""

    def __init__(self, name: str, email: str):
        """Initialize customer attributes."""
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert customer object to dictionary."""
        return {"name": self.name, "email": self.email}

    @staticmethod
    def create_customer(name: str, email: str):
        """Create a customer and store in file."""
        customers = load_data(CUSTOMERS_FILE)
        customers[name] = {"email": email}
        save_data(CUSTOMERS_FILE, customers)

    @staticmethod
    def delete_customer(name: str):
        """Delete a customer from file."""
        customers = load_data(CUSTOMERS_FILE)
        if name in customers:
            del customers[name]
            save_data(CUSTOMERS_FILE, customers)
