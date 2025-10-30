"""
Seat Allocator - A flexible seat allocation system.

This module provides a SeatAllocator class that can manage seat assignments
for various scenarios like theaters, classrooms, events, etc.
"""

from typing import Optional, List, Tuple, Dict, Set
from enum import Enum


class SeatStatus(Enum):
    """Enum representing the status of a seat."""
    AVAILABLE = "available"
    OCCUPIED = "occupied"


class Seat:
    """Represents a single seat in the allocation system."""
    
    def __init__(self, row: int, number: int):
        """
        Initialize a seat.
        
        Args:
            row: The row number of the seat
            number: The seat number within the row
        """
        self.row = row
        self.number = number
        self.status = SeatStatus.AVAILABLE
        self.occupant: Optional[str] = None
    
    def allocate(self, occupant: str) -> bool:
        """
        Allocate the seat to an occupant.
        
        Args:
            occupant: The identifier of the person/booking
            
        Returns:
            True if allocation was successful, False otherwise
        """
        if self.status == SeatStatus.AVAILABLE:
            self.status = SeatStatus.OCCUPIED
            self.occupant = occupant
            return True
        return False
    
    def release(self) -> bool:
        """
        Release the seat, making it available again.
        
        Returns:
            True if release was successful, False otherwise
        """
        if self.status == SeatStatus.OCCUPIED:
            self.status = SeatStatus.AVAILABLE
            self.occupant = None
            return True
        return False
    
    def is_available(self) -> bool:
        """Check if the seat is available."""
        return self.status == SeatStatus.AVAILABLE
    
    def __repr__(self) -> str:
        """String representation of the seat."""
        status = "O" if self.status == SeatStatus.OCCUPIED else "A"
        return f"Seat({self.row},{self.number},{status})"


class SeatAllocator:
    """
    Main seat allocation system that manages multiple seats.
    
    This class provides functionality to create, allocate, release,
    and query seats in a flexible seating arrangement.
    """
    
    def __init__(self, rows: int, seats_per_row: int):
        """
        Initialize the seat allocator.
        
        Args:
            rows: Number of rows in the seating arrangement
            seats_per_row: Number of seats in each row
            
        Raises:
            ValueError: If rows or seats_per_row are less than 1
        """
        if rows < 1 or seats_per_row < 1:
            raise ValueError("Rows and seats_per_row must be at least 1")
        
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats: Dict[Tuple[int, int], Seat] = {}
        self._allocations: Dict[str, Set[Tuple[int, int]]] = {}
        
        # Initialize all seats
        for row in range(1, rows + 1):
            for seat_num in range(1, seats_per_row + 1):
                self.seats[(row, seat_num)] = Seat(row, seat_num)
    
    def allocate_seat(self, row: int, seat_number: int, occupant: str) -> bool:
        """
        Allocate a specific seat to an occupant.
        
        Args:
            row: The row number
            seat_number: The seat number within the row
            occupant: The identifier of the person/booking
            
        Returns:
            True if allocation was successful, False otherwise
        """
        key = (row, seat_number)
        if key not in self.seats:
            return False
        
        seat = self.seats[key]
        if seat.allocate(occupant):
            if occupant not in self._allocations:
                self._allocations[occupant] = set()
            self._allocations[occupant].add(key)
            return True
        return False
    
    def allocate_next_available(self, occupant: str, count: int = 1) -> List[Tuple[int, int]]:
        """
        Allocate the next available seats to an occupant.
        
        Args:
            occupant: The identifier of the person/booking
            count: Number of seats to allocate
            
        Returns:
            List of (row, seat_number) tuples that were allocated
        """
        allocated = []
        for row in range(1, self.rows + 1):
            for seat_num in range(1, self.seats_per_row + 1):
                if len(allocated) >= count:
                    return allocated
                
                if self.allocate_seat(row, seat_num, occupant):
                    allocated.append((row, seat_num))
        
        return allocated
    
    def release_seat(self, row: int, seat_number: int) -> bool:
        """
        Release a specific seat.
        
        Args:
            row: The row number
            seat_number: The seat number within the row
            
        Returns:
            True if release was successful, False otherwise
        """
        key = (row, seat_number)
        if key not in self.seats:
            return False
        
        seat = self.seats[key]
        occupant = seat.occupant
        
        if seat.release():
            if occupant and occupant in self._allocations:
                self._allocations[occupant].discard(key)
                if not self._allocations[occupant]:
                    del self._allocations[occupant]
            return True
        return False
    
    def release_all_for_occupant(self, occupant: str) -> int:
        """
        Release all seats allocated to a specific occupant.
        
        Args:
            occupant: The identifier of the person/booking
            
        Returns:
            Number of seats released
        """
        if occupant not in self._allocations:
            return 0
        
        seats_to_release = list(self._allocations[occupant])
        count = 0
        
        for row, seat_num in seats_to_release:
            if self.release_seat(row, seat_num):
                count += 1
        
        return count
    
    def get_available_seats(self) -> List[Tuple[int, int]]:
        """
        Get a list of all available seats.
        
        Returns:
            List of (row, seat_number) tuples for available seats
        """
        available = []
        for row in range(1, self.rows + 1):
            for seat_num in range(1, self.seats_per_row + 1):
                seat = self.seats[(row, seat_num)]
                if seat.is_available():
                    available.append((row, seat_num))
        return available
    
    def get_occupied_seats(self) -> List[Tuple[int, int, str]]:
        """
        Get a list of all occupied seats with their occupants.
        
        Returns:
            List of (row, seat_number, occupant) tuples for occupied seats
        """
        occupied = []
        for row in range(1, self.rows + 1):
            for seat_num in range(1, self.seats_per_row + 1):
                seat = self.seats[(row, seat_num)]
                if not seat.is_available():
                    occupied.append((row, seat_num, seat.occupant))
        return occupied
    
    def get_seats_for_occupant(self, occupant: str) -> List[Tuple[int, int]]:
        """
        Get all seats allocated to a specific occupant.
        
        Args:
            occupant: The identifier of the person/booking
            
        Returns:
            List of (row, seat_number) tuples
        """
        if occupant not in self._allocations:
            return []
        return sorted(list(self._allocations[occupant]))
    
    def is_seat_available(self, row: int, seat_number: int) -> bool:
        """
        Check if a specific seat is available.
        
        Args:
            row: The row number
            seat_number: The seat number within the row
            
        Returns:
            True if seat is available, False otherwise
        """
        key = (row, seat_number)
        if key not in self.seats:
            return False
        return self.seats[key].is_available()
    
    def get_availability_count(self) -> int:
        """Get the count of available seats."""
        return len(self.get_available_seats())
    
    def get_total_seats(self) -> int:
        """Get the total number of seats."""
        return self.rows * self.seats_per_row
    
    def get_occupancy_rate(self) -> float:
        """
        Get the occupancy rate as a percentage.
        
        Returns:
            Occupancy rate (0.0 to 100.0)
        """
        total = self.get_total_seats()
        if total == 0:
            return 0.0
        occupied = total - self.get_availability_count()
        return (occupied / total) * 100.0
    
    def display_seating_chart(self) -> str:
        """
        Generate a visual representation of the seating chart.
        
        Returns:
            String representation of the seating chart
        """
        lines = []
        lines.append(f"Seating Chart ({self.rows} rows x {self.seats_per_row} seats)")
        lines.append(f"Available: {self.get_availability_count()}/{self.get_total_seats()}")
        lines.append("")
        
        # Header with seat numbers
        header = "Row | " + " ".join(f"{i:2}" for i in range(1, self.seats_per_row + 1))
        lines.append(header)
        lines.append("-" * len(header))
        
        # Rows with seats
        for row in range(1, self.rows + 1):
            row_str = f"{row:3} | "
            for seat_num in range(1, self.seats_per_row + 1):
                seat = self.seats[(row, seat_num)]
                symbol = "X" if not seat.is_available() else "O"
                row_str += f"{symbol:2} "
            lines.append(row_str)
        
        lines.append("")
        lines.append("Legend: O = Available, X = Occupied")
        
        return "\n".join(lines)
    
    def __repr__(self) -> str:
        """String representation of the allocator."""
        return (f"SeatAllocator(rows={self.rows}, seats_per_row={self.seats_per_row}, "
                f"available={self.get_availability_count()}/{self.get_total_seats()})")
