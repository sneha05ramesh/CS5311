class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) >> 1

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def heapify(self, i):
        smallest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def build_min_heap(self, array):
        self.heap = array[:]
        n = len(self.heap)
        for i in range((n - 1) >> 1, -1, -1):
            self.heapify(i)

    def pop_root(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return root

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def display(self):
        print("Min Heap:", self.heap)


heap = MinHeap()
heap.build_min_heap([2, 6, 5, 0, 10])
heap.display()  # Output: Min Heap: [0, 2, 5, 6, 10]
heap.insert(3)
heap.display()  # Output: Min Heap: [0, 2, 3, 6, 10, 5]
print("Popped root:", heap.pop_root())  # Output: Popped root: 0
heap.display()  # Output: Min Heap: [2, 5, 3, 6, 10]
