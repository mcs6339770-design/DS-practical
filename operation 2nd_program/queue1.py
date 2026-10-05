queue = []
MAX = 5

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        if len(queue) == MAX:
            print("Queue Overflow")
        else:
            value = int(input("Enter element: "))
            queue.append(value)
            print("Inserted:", value)

    elif choice == 2:
        if len(queue) == 0:
            print("Queue Underflow")
        else:
            print("Deleted:", queue.pop(0))

    elif choice == 3:
        print("Queue:", queue)

    elif choice == 4:
        break

    else:
        print("Invalid choice")