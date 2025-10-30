"""
Example usage of the Seat Allocator system.

This script demonstrates how to use the SeatAllocator class
for various scenarios.
"""

from seat_allocator import SeatAllocator


def main():
    """Run example scenarios."""
    
    print("=" * 60)
    print("SEAT ALLOCATOR DEMO")
    print("=" * 60)
    print()
    
    # Example 1: Theater Booking
    print("Example 1: Small Theater Booking")
    print("-" * 60)
    theater = SeatAllocator(5, 8)
    print(f"Created theater: {theater}")
    print()
    
    # Book some seats
    print("Booking 2 seats for Alice...")
    alice_seats = theater.allocate_next_available("Alice", 2)
    print(f"Alice got seats: {alice_seats}")
    print()
    
    print("Booking specific seats for Bob (Row 3, Seats 4-5)...")
    theater.allocate_seat(3, 4, "Bob")
    theater.allocate_seat(3, 5, "Bob")
    bob_seats = theater.get_seats_for_occupant("Bob")
    print(f"Bob got seats: {bob_seats}")
    print()
    
    print("Booking 3 seats for Charlie...")
    charlie_seats = theater.allocate_next_available("Charlie", 3)
    print(f"Charlie got seats: {charlie_seats}")
    print()
    
    # Display current status
    print("Current Theater Status:")
    print(theater.display_seating_chart())
    print()
    print(f"Occupancy Rate: {theater.get_occupancy_rate():.1f}%")
    print()
    
    # Release seats
    print("Alice cancels their booking...")
    released = theater.release_all_for_occupant("Alice")
    print(f"Released {released} seats")
    print(f"New availability: {theater.get_availability_count()}/{theater.get_total_seats()}")
    print()
    
    # Example 2: Classroom Seating
    print("\n" + "=" * 60)
    print("Example 2: Classroom Seating")
    print("-" * 60)
    classroom = SeatAllocator(4, 6)
    print(f"Created classroom: {classroom}")
    print()
    
    students = ["Emma", "Liam", "Olivia", "Noah", "Ava"]
    print(f"Assigning seats to {len(students)} students...")
    for student in students:
        seats = classroom.allocate_next_available(student, 1)
        print(f"  {student}: Seat {seats[0]}")
    print()
    
    print("Classroom Layout:")
    print(classroom.display_seating_chart())
    print()
    
    # Example 3: Query Operations
    print("\n" + "=" * 60)
    print("Example 3: Query Operations")
    print("-" * 60)
    venue = SeatAllocator(3, 5)
    
    venue.allocate_seat(1, 1, "David")
    venue.allocate_seat(1, 2, "David")
    venue.allocate_seat(2, 3, "Eve")
    
    print("Available seats:")
    available = venue.get_available_seats()
    print(f"  {len(available)} seats available: {available[:5]}...")
    print()
    
    print("Occupied seats:")
    occupied = venue.get_occupied_seats()
    for row, seat, occupant in occupied:
        print(f"  Row {row}, Seat {seat}: {occupant}")
    print()
    
    print("David's seats:")
    david_seats = venue.get_seats_for_occupant("David")
    print(f"  {david_seats}")
    print()
    
    print("Checking specific seat availability:")
    print(f"  Row 1, Seat 1: {'Available' if venue.is_seat_available(1, 1) else 'Occupied'}")
    print(f"  Row 2, Seat 1: {'Available' if venue.is_seat_available(2, 1) else 'Occupied'}")
    print()
    
    print("=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
