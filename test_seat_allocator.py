"""
Unit tests for the Seat Allocator system.
"""

import unittest
from seat_allocator import SeatAllocator, Seat, SeatStatus


class TestSeat(unittest.TestCase):
    """Test cases for the Seat class."""
    
    def test_seat_initialization(self):
        """Test that a seat initializes correctly."""
        seat = Seat(1, 5)
        self.assertEqual(seat.row, 1)
        self.assertEqual(seat.number, 5)
        self.assertEqual(seat.status, SeatStatus.AVAILABLE)
        self.assertIsNone(seat.occupant)
    
    def test_seat_allocation(self):
        """Test seat allocation."""
        seat = Seat(1, 1)
        result = seat.allocate("John")
        self.assertTrue(result)
        self.assertEqual(seat.status, SeatStatus.OCCUPIED)
        self.assertEqual(seat.occupant, "John")
    
    def test_seat_allocation_when_occupied(self):
        """Test that allocation fails when seat is already occupied."""
        seat = Seat(1, 1)
        seat.allocate("John")
        result = seat.allocate("Jane")
        self.assertFalse(result)
        self.assertEqual(seat.occupant, "John")
    
    def test_seat_release(self):
        """Test seat release."""
        seat = Seat(1, 1)
        seat.allocate("John")
        result = seat.release()
        self.assertTrue(result)
        self.assertEqual(seat.status, SeatStatus.AVAILABLE)
        self.assertIsNone(seat.occupant)
    
    def test_seat_release_when_available(self):
        """Test that release fails when seat is already available."""
        seat = Seat(1, 1)
        result = seat.release()
        self.assertFalse(result)
    
    def test_is_available(self):
        """Test the is_available method."""
        seat = Seat(1, 1)
        self.assertTrue(seat.is_available())
        seat.allocate("John")
        self.assertFalse(seat.is_available())
        seat.release()
        self.assertTrue(seat.is_available())


class TestSeatAllocator(unittest.TestCase):
    """Test cases for the SeatAllocator class."""
    
    def test_allocator_initialization(self):
        """Test that allocator initializes correctly."""
        allocator = SeatAllocator(5, 10)
        self.assertEqual(allocator.rows, 5)
        self.assertEqual(allocator.seats_per_row, 10)
        self.assertEqual(allocator.get_total_seats(), 50)
        self.assertEqual(allocator.get_availability_count(), 50)
    
    def test_allocator_invalid_dimensions(self):
        """Test that allocator raises error for invalid dimensions."""
        with self.assertRaises(ValueError):
            SeatAllocator(0, 10)
        with self.assertRaises(ValueError):
            SeatAllocator(5, 0)
        with self.assertRaises(ValueError):
            SeatAllocator(-1, 10)
    
    def test_allocate_specific_seat(self):
        """Test allocating a specific seat."""
        allocator = SeatAllocator(3, 5)
        result = allocator.allocate_seat(2, 3, "Alice")
        self.assertTrue(result)
        self.assertEqual(allocator.get_availability_count(), 14)
    
    def test_allocate_occupied_seat(self):
        """Test that allocating an occupied seat fails."""
        allocator = SeatAllocator(3, 5)
        allocator.allocate_seat(2, 3, "Alice")
        result = allocator.allocate_seat(2, 3, "Bob")
        self.assertFalse(result)
    
    def test_allocate_invalid_seat(self):
        """Test that allocating an invalid seat fails."""
        allocator = SeatAllocator(3, 5)
        result = allocator.allocate_seat(10, 10, "Alice")
        self.assertFalse(result)
    
    def test_allocate_next_available(self):
        """Test allocating next available seats."""
        allocator = SeatAllocator(2, 3)
        allocated = allocator.allocate_next_available("Bob", 3)
        self.assertEqual(len(allocated), 3)
        self.assertEqual(allocated[0], (1, 1))
        self.assertEqual(allocated[1], (1, 2))
        self.assertEqual(allocated[2], (1, 3))
        self.assertEqual(allocator.get_availability_count(), 3)
    
    def test_allocate_next_available_insufficient_seats(self):
        """Test allocating when not enough seats are available."""
        allocator = SeatAllocator(1, 2)
        allocator.allocate_seat(1, 1, "Alice")
        allocated = allocator.allocate_next_available("Bob", 5)
        self.assertEqual(len(allocated), 1)  # Only 1 seat was available
    
    def test_release_seat(self):
        """Test releasing a specific seat."""
        allocator = SeatAllocator(3, 5)
        allocator.allocate_seat(2, 3, "Alice")
        result = allocator.release_seat(2, 3)
        self.assertTrue(result)
        self.assertEqual(allocator.get_availability_count(), 15)
    
    def test_release_available_seat(self):
        """Test that releasing an available seat fails."""
        allocator = SeatAllocator(3, 5)
        result = allocator.release_seat(2, 3)
        self.assertFalse(result)
    
    def test_release_invalid_seat(self):
        """Test that releasing an invalid seat fails."""
        allocator = SeatAllocator(3, 5)
        result = allocator.release_seat(10, 10)
        self.assertFalse(result)
    
    def test_release_all_for_occupant(self):
        """Test releasing all seats for a specific occupant."""
        allocator = SeatAllocator(3, 5)
        allocator.allocate_seat(1, 1, "Charlie")
        allocator.allocate_seat(2, 2, "Charlie")
        allocator.allocate_seat(3, 3, "Charlie")
        
        count = allocator.release_all_for_occupant("Charlie")
        self.assertEqual(count, 3)
        self.assertEqual(allocator.get_availability_count(), 15)
    
    def test_release_all_for_nonexistent_occupant(self):
        """Test releasing seats for a non-existent occupant."""
        allocator = SeatAllocator(3, 5)
        count = allocator.release_all_for_occupant("Nobody")
        self.assertEqual(count, 0)
    
    def test_get_available_seats(self):
        """Test getting all available seats."""
        allocator = SeatAllocator(2, 3)
        allocator.allocate_seat(1, 2, "Alice")
        available = allocator.get_available_seats()
        self.assertEqual(len(available), 5)
        self.assertIn((1, 1), available)
        self.assertNotIn((1, 2), available)
    
    def test_get_occupied_seats(self):
        """Test getting all occupied seats."""
        allocator = SeatAllocator(2, 3)
        allocator.allocate_seat(1, 2, "Alice")
        allocator.allocate_seat(2, 1, "Bob")
        occupied = allocator.get_occupied_seats()
        self.assertEqual(len(occupied), 2)
        self.assertIn((1, 2, "Alice"), occupied)
        self.assertIn((2, 1, "Bob"), occupied)
    
    def test_get_seats_for_occupant(self):
        """Test getting seats for a specific occupant."""
        allocator = SeatAllocator(3, 5)
        allocator.allocate_seat(1, 1, "Dave")
        allocator.allocate_seat(2, 3, "Dave")
        allocator.allocate_seat(3, 5, "Eve")
        
        dave_seats = allocator.get_seats_for_occupant("Dave")
        self.assertEqual(len(dave_seats), 2)
        self.assertIn((1, 1), dave_seats)
        self.assertIn((2, 3), dave_seats)
        
        eve_seats = allocator.get_seats_for_occupant("Eve")
        self.assertEqual(len(eve_seats), 1)
        self.assertIn((3, 5), eve_seats)
    
    def test_get_seats_for_nonexistent_occupant(self):
        """Test getting seats for a non-existent occupant."""
        allocator = SeatAllocator(3, 5)
        seats = allocator.get_seats_for_occupant("Nobody")
        self.assertEqual(len(seats), 0)
    
    def test_is_seat_available(self):
        """Test checking if a specific seat is available."""
        allocator = SeatAllocator(3, 5)
        self.assertTrue(allocator.is_seat_available(2, 3))
        allocator.allocate_seat(2, 3, "Alice")
        self.assertFalse(allocator.is_seat_available(2, 3))
        self.assertFalse(allocator.is_seat_available(10, 10))  # Invalid seat
    
    def test_get_occupancy_rate(self):
        """Test calculating occupancy rate."""
        allocator = SeatAllocator(2, 5)
        self.assertEqual(allocator.get_occupancy_rate(), 0.0)
        
        allocator.allocate_seat(1, 1, "Alice")
        self.assertEqual(allocator.get_occupancy_rate(), 10.0)
        
        allocator.allocate_next_available("Bob", 4)
        self.assertEqual(allocator.get_occupancy_rate(), 50.0)
    
    def test_display_seating_chart(self):
        """Test displaying the seating chart."""
        allocator = SeatAllocator(2, 3)
        allocator.allocate_seat(1, 2, "Alice")
        chart = allocator.display_seating_chart()
        self.assertIn("Seating Chart", chart)
        self.assertIn("Available: 5/6", chart)
        self.assertIn("Legend", chart)
    
    def test_multiple_occupants(self):
        """Test allocating seats to multiple occupants."""
        allocator = SeatAllocator(3, 4)
        
        allocator.allocate_next_available("Alice", 2)
        allocator.allocate_next_available("Bob", 3)
        allocator.allocate_seat(3, 4, "Charlie")
        
        alice_seats = allocator.get_seats_for_occupant("Alice")
        bob_seats = allocator.get_seats_for_occupant("Bob")
        charlie_seats = allocator.get_seats_for_occupant("Charlie")
        
        self.assertEqual(len(alice_seats), 2)
        self.assertEqual(len(bob_seats), 3)
        self.assertEqual(len(charlie_seats), 1)
        self.assertEqual(allocator.get_availability_count(), 6)
    
    def test_repr(self):
        """Test string representation of allocator."""
        allocator = SeatAllocator(5, 10)
        repr_str = repr(allocator)
        self.assertIn("SeatAllocator", repr_str)
        self.assertIn("rows=5", repr_str)
        self.assertIn("seats_per_row=10", repr_str)


class TestIntegrationScenarios(unittest.TestCase):
    """Integration tests for realistic scenarios."""
    
    def test_theater_booking_scenario(self):
        """Test a realistic theater booking scenario."""
        # Create a small theater with 5 rows and 8 seats per row
        theater = SeatAllocator(5, 8)
        
        # First customer books 2 seats
        seats1 = theater.allocate_next_available("Customer1", 2)
        self.assertEqual(len(seats1), 2)
        
        # Second customer books specific seats
        result = theater.allocate_seat(3, 4, "Customer2")
        self.assertTrue(result)
        result = theater.allocate_seat(3, 5, "Customer2")
        self.assertTrue(result)
        
        # Third customer books 4 seats
        seats3 = theater.allocate_next_available("Customer3", 4)
        self.assertEqual(len(seats3), 4)
        
        # Check total bookings
        self.assertEqual(theater.get_availability_count(), 32)
        
        # Customer1 cancels their booking
        released = theater.release_all_for_occupant("Customer1")
        self.assertEqual(released, 2)
        self.assertEqual(theater.get_availability_count(), 34)
    
    def test_classroom_seating(self):
        """Test a classroom seating scenario."""
        # Create a classroom with 4 rows and 6 seats per row
        classroom = SeatAllocator(4, 6)
        
        # Assign specific seats to students
        students = ["Alice", "Bob", "Charlie", "David", "Eve"]
        for i, student in enumerate(students):
            row = (i // 6) + 1
            seat = (i % 6) + 1
            classroom.allocate_seat(row, seat, student)
        
        # Check that all students have seats
        for student in students:
            seats = classroom.get_seats_for_occupant(student)
            self.assertEqual(len(seats), 1)
        
        # Display the chart
        chart = classroom.display_seating_chart()
        self.assertIsNotNone(chart)


if __name__ == '__main__':
    unittest.main()
