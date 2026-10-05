MAX = 5
queue = [None] * MAX
front = -1
rear = -1

def insert(value):
    global front, rear

    if (rear + 1) % MAX == front:
        print("Circular Queue Overflow")
        return

    if front == -1:
        front = 0

    rear = (rear + 1) % MAX
    queue[rear] = value
    print("Inserted:", value)


def delete():
    global front, rear

    if front == -1:
        print("Circular Queue Underflow")
        return

    print("Deleted:", queue[front])

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % MAX


def display():
    if front == -1:
        print("Queue is empty")
        return

    i = front
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % MAX


while True:
    print("\n\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        insert(value)

    elif choice == 2:
        delete()

    elif choice == 3:
        display()

    elif choice == 4:
        break