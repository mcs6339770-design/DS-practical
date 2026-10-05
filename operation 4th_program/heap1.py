class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] >= self.heap[i]:
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
            largest = i

            if left < len(self.heap) and \
               self.heap[left] > self.heap[largest]:
                largest = left

            if right < len(self.heap) and \
               self.heap[right] > self.heap[largest]:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = \
                self.heap[largest], self.heap[i]

            i = largest

    def display(self):
        print("Max Heap:", self.heap)


h = MaxHeap()

h.insert(40)
h.insert(20)
h.insert(50)
h.insert(10)
h.insert(30)

h.display()

h.delete()
h.display()