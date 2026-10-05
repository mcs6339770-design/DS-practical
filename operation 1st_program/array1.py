stack = []

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        stack.append(item)
        print("Element pushed successfully.")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped element:", stack.pop())

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", stack[-1])

    elif choice == 4:
        print("Stack:", stack)

    elif choice == 5:
        break

    else:
        print("Invalid choice")