class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = [0] * self.capacity

    def resize(self, new_capacity):
        new_arr = [0] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def push_back(self, element):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.arr[self.size] = element
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            return None
        popped_element = self.arr[self.size - 1]
        self.size -= 1
        if self.size < self.capacity // 4:
            self.resize(self.capacity // 2)
        return popped_element

    def get(self, index):
        if 0 <= index < self.size:
            return self.arr[index]
        else:
            return None

    def set(self, index, value):
        if 0 <= index < self.size:
            self.arr[index] = value

    def __len__(self):
        return self.size

    def __str__(self):
        return '[' + ', '.join(map(str, self.arr[:self.size])) + ']'


# Test the implementation
if __name__ == "__main__":
    # Create a dynamic array
    dyn_arr = DynamicArray()

    # Add elements
    for i in range(10):
        dyn_arr.push_back(i)

    # Print the array
    print("Dynamic Array after adding elements:", dyn_arr)

    # Pop an element
    popped_element = dyn_arr.pop_back()
    print("Popped Element:", popped_element)
    print("Dynamic Array after popping:", dyn_arr)

    # Access elements
    print("Element at index 5:", dyn_arr.get(5))

    # Modify elements
    dyn_arr.set(5, 100)
    print("Modified Element at index 5:", dyn_arr.get(5))
