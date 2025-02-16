# test.py
"""
Unit tests for the hotel reservation system.
"""

import unittest
from hotel import Hotel
from customer import Customer
from reservation import Reservation
from utils import load_data, HOTELS_FILE, CUSTOMERS_FILE, RESERVATIONS_FILE


class TestHotelReservationSystem(unittest.TestCase):
    """Unit tests for hotel, customer, and reservation operations."""

    def setUp(self):
        """Initialize test attributes."""
        self.hotel_name = "Hotel Test"
        self.customer_name = "John Doe"
        self.hotel_location = "New York"
        self.hotel_rooms = 100
        self.customer_email = "john@example.com"

    def test_hotel_operations(self):
        """Test hotel creation and deletion."""
        Hotel.create_hotel(self.hotel_name,
                           self.hotel_location,
                           self.hotel_rooms)
        hotels = load_data(HOTELS_FILE)
        self.assertIn(self.hotel_name, hotels)
        Hotel.delete_hotel(self.hotel_name)
        hotels = load_data(HOTELS_FILE)
        self.assertNotIn(self.hotel_name, hotels)

    def test_customer_operations(self):
        """Test customer creation and deletion."""
        Customer.create_customer(self.customer_name, self.customer_email)
        customers = load_data(CUSTOMERS_FILE)
        self.assertIn(self.customer_name, customers)
        Customer.delete_customer(self.customer_name)
        customers = load_data(CUSTOMERS_FILE)
        self.assertNotIn(self.customer_name, customers)

    def test_reservation_operations(self):
        """Test reservation creation and cancellation."""
        Reservation.create_reservation(self.customer_name, self.hotel_name)
        reservations = load_data(RESERVATIONS_FILE)
        self.assertIn(f"{self.customer_name}_{self.hotel_name}", reservations)
        Reservation.cancel_reservation(self.customer_name, self.hotel_name)
        reservations = load_data(RESERVATIONS_FILE)
        self.assertNotIn(f"{self.customer_name}_{self.hotel_name}",
                         reservations)


if __name__ == "__main__":
    unittest.main()
