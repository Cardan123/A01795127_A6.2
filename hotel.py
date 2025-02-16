# hotel.py
"""
Module for managing hotel information.
"""

from utils import load_data, save_data, HOTELS_FILE


class Hotel:
    """Class representing a hotel."""

    def __init__(self, name: str, location: str, rooms: int):
        """Initialize hotel attributes."""
        self.name = name
        self.location = location
        self.rooms = rooms

    def to_dict(self):
        """Convert hotel object to dictionary."""
        return {"name": self.name, "location": self.location,
                "rooms": self.rooms}

    @staticmethod
    def create_hotel(name: str, location: str, rooms: int):
        """Create a hotel and store in file."""
        hotels = load_data(HOTELS_FILE)
        hotels[name] = {"location": location, "rooms": rooms}
        save_data(HOTELS_FILE, hotels)

    @staticmethod
    def delete_hotel(name: str):
        """Delete a hotel from file."""
        hotels = load_data(HOTELS_FILE)
        if name in hotels:
            del hotels[name]
            save_data(HOTELS_FILE, hotels)
