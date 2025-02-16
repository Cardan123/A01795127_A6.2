# reservation.py
"""
Module for managing reservations.
"""

from utils import load_data, save_data, RESERVATIONS_FILE


class Reservation:
    """Class representing a reservation."""

    def __init__(self, customer_name: str, hotel_name: str):
        """Initialize reservation attributes."""
        self.customer_name = customer_name
        self.hotel_name = hotel_name

    def to_dict(self):
        """Convert reservation object to dictionary."""
        return {"customer": self.customer_name, "hotel": self.hotel_name}

    @staticmethod
    def create_reservation(customer_name: str, hotel_name: str):
        """Create a reservation and store in file."""
        reservations = load_data(RESERVATIONS_FILE)
        key = f"{customer_name}_{hotel_name}"
        reservations[key] = {"customer": customer_name, "hotel": hotel_name}
        save_data(RESERVATIONS_FILE, reservations)

    @staticmethod
    def cancel_reservation(customer_name: str, hotel_name: str):
        """Cancel a reservation from file."""
        reservations = load_data(RESERVATIONS_FILE)
        key = f"{customer_name}_{hotel_name}"
        if key in reservations:
            del reservations[key]
            save_data(RESERVATIONS_FILE, reservations)
