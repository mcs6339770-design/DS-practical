class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print("Inserted:", data)

    def delete(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            print("Deleted:", self.front.data)
            self.front = self.front.next

            if self.front is None:
                self.rear = None

    def display(self):
        temp = self.front

        if temp is None:
            print("Queue is empty")
        else:
            while temp:
                print(temp.data, end=" ")
                temp = temp.next


q = Queue()

while True:
    print("\n\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        q.insert(value)

    elif choice == 2:
        q.delete()

    elif choice == 3:
        q.display()

    elif choice == 4:
        break