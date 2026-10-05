heap = []


def insert(value):
    heap.append(value)
    i = len(heap) - 1

    while i > 0:
        parent = (i - 1) // 2

        if heap[parent] >= heap[i]:
            break

        heap[parent], heap[i] = heap[i], heap[parent]
        i = parent


def delete():
    if len(heap) == 0:
        print("Heap Underflow")
        return

    print("Deleted:", heap[0])

    heap[0] = heap[-1]
    heap.pop()

    i = 0

    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(heap) and heap[left] > heap[largest]:
            largest = left

        if right < len(heap) and heap[right] > heap[largest]:
            largest = right

        if largest == i:
            break

        heap[i], heap[largest] = heap[largest], heap[i]
        i = largest


while True:
    print("\n--- HEAP MENU ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        insert(value)

    elif choice == 2:
        delete()

    elif choice == 3:
        print("Heap:", heap)

    elif choice == 4:
        break

    else:
        print("Invalid choice")