bookings = []

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [x for x in data[1:] if x["amount"] <= pivot["amount"]]
    right = [x for x in data[1:] if x["amount"] > pivot["amount"]]

    return quick_sort(left) + [pivot] + quick_sort(right)


while True:
    print("\n1. Add Booking")
    print("2. Display Bookings")
    print("3. Sort by Amount")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Customer name: ")
        movie = input("Movie name: ")
        tickets = int(input("Number of tickets: "))
        amount = tickets * 150

        bookings.append({
            "name": name,
            "movie": movie,
            "tickets": tickets,
            "amount": amount
        })

        print("Booking added successfully!")

    elif choice == "2":
        for b in bookings:
            print(b)

    elif choice == "3":
        bookings = quick_sort(bookings)
        print("\nBookings sorted by ticket amount:")
        for b in bookings:
            print(b)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")