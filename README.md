# Seat Allocator (SRM)

A flexible and robust seat allocation system for managing seating arrangements in various scenarios such as theaters, classrooms, event venues, and more.

## Features

- **Flexible Seating Arrangements**: Create seating layouts with custom rows and seats per row
- **Seat Allocation**: Allocate specific seats or automatically assign next available seats
- **Occupant Management**: Track which seats are assigned to which occupants
- **Seat Release**: Release individual seats or all seats for a specific occupant
- **Query Operations**: Check availability, get occupancy rates, and view seating charts
- **Visual Display**: Generate ASCII-based seating charts for easy visualization

## Installation

Simply clone this repository or copy the `seat_allocator.py` file to your project:

```bash
git clone https://github.com/srmasc/srm.git
cd srm
```

## Usage

### Basic Example

```python
from seat_allocator import SeatAllocator

# Create a theater with 5 rows and 10 seats per row
theater = SeatAllocator(5, 10)

# Allocate specific seats
theater.allocate_seat(3, 5, "John Doe")

# Allocate next available seats
seats = theater.allocate_next_available("Jane Smith", 2)
print(f"Jane got seats: {seats}")

# Display seating chart
print(theater.display_seating_chart())

# Check availability
available = theater.get_availability_count()
total = theater.get_total_seats()
print(f"Available: {available}/{total}")

# Release seats
theater.release_all_for_occupant("John Doe")
```

### Running the Example

Run the included example script to see the seat allocator in action:

```bash
python example.py
```

## API Reference

### SeatAllocator Class

#### Constructor
```python
SeatAllocator(rows: int, seats_per_row: int)
```
Create a new seat allocator with the specified dimensions.

#### Methods

- **`allocate_seat(row, seat_number, occupant)`**: Allocate a specific seat
- **`allocate_next_available(occupant, count=1)`**: Allocate next available seats
- **`release_seat(row, seat_number)`**: Release a specific seat
- **`release_all_for_occupant(occupant)`**: Release all seats for an occupant
- **`get_available_seats()`**: Get list of all available seats
- **`get_occupied_seats()`**: Get list of all occupied seats with occupants
- **`get_seats_for_occupant(occupant)`**: Get seats allocated to an occupant
- **`is_seat_available(row, seat_number)`**: Check if a seat is available
- **`get_availability_count()`**: Get count of available seats
- **`get_total_seats()`**: Get total number of seats
- **`get_occupancy_rate()`**: Get occupancy rate as percentage
- **`display_seating_chart()`**: Generate visual seating chart

## Testing

Run the comprehensive test suite:

```bash
python -m unittest test_seat_allocator.py -v
```

## CI/CD

This project includes GitHub Actions workflows for:
- **Continuous Integration**: Automated testing across multiple Python versions (3.8-3.12)
- **Linting**: Code quality checks with flake8, pylint, and mypy

## Use Cases

- **Theaters & Cinemas**: Manage ticket bookings and seat assignments
- **Classrooms**: Assign seats to students
- **Event Venues**: Handle seating for conferences and events
- **Airlines**: Seat allocation for flights
- **Restaurants**: Table and seat management

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.