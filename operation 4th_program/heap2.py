class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] <= self.heap[i]:
                break

            self.heap[parent], self.heap[i] = \
                self.heap[i], self.heap[parent]

            i = parent

    def delete(self):
        if not self.heap:
            print("Heap is empty")
            return

        print("Deleted:", self.heap[0])

        self.heap[0] = self.heap[-1]
        self.heap.pop()

        i = 0

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < len(self.heap) and \
               self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < len(self.heap) and \
               self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = \
                self.heap[smallest], self.heap[i]

            i = smallest

    def display(self):
        print("Min Heap:", self.heap)


h = MinHeap()

h.insert(30)
h.insert(10)
h.insert(40)
h.insert(5)
h.insert(20)

h.display()

h.delete()
h.display()