def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[0]
    left = [x for x in bookings[1:] if x["tickets"] <= pivot["tickets"]]
    right = [x for x in bookings[1:] if x["tickets"] > pivot["tickets"]]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = [
    {"id": 101, "movie": "Leo", "tickets": 4},
    {"id": 102, "movie": "Jailer", "tickets": 2},
    {"id": 103, "movie": "GOAT", "tickets": 5},
    {"id": 104, "movie": "Vikram", "tickets": 1}
]

print("Bookings sorted by number of tickets:")

for b in quick_sort(bookings):
    print("Booking ID:", b["id"],
          "Movie:", b["movie"],
          "Tickets:", b["tickets"])