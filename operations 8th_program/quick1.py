def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[0]
    left = [x for x in bookings[1:] if x["price"] <= pivot["price"]]
    right = [x for x in bookings[1:] if x["price"] > pivot["price"]]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = [
    {"name": "Anu", "movie": "Leo", "price": 200},
    {"name": "Ravi", "movie": "Jailer", "price": 150},
    {"name": "Kavi", "movie": "Vikram", "price": 250},
    {"name": "Meena", "movie": "GOAT", "price": 180}
]

print("Bookings sorted by ticket price:")
for b in quick_sort(bookings):
    print(b["name"], b["movie"], b["price"])