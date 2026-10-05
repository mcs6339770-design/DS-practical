def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [x for x in data[1:] if x["name"].lower() <= pivot["name"].lower()]
    right = [x for x in data[1:] if x["name"].lower() > pivot["name"].lower()]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = [
    {"name": "Ravi", "movie": "Leo", "seat": "A1"},
    {"name": "Anu", "movie": "Jailer", "seat": "A2"},
    {"name": "Meena", "movie": "GOAT", "seat": "B1"},
    {"name": "Kavi", "movie": "Vikram", "seat": "B2"}
]

print("Bookings sorted by customer name:")

for b in quick_sort(bookings):
    print(b["name"], b["movie"], b["seat"])