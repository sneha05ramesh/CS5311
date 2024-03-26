class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

class HashTable:
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [None] * initial_capacity

    def hash_function_multiplication(self, key):
        A = 0.61803398875  # A value close to the golden ratio
        return int(self.capacity * ((key * A) % 1))

    def hash_function_division(self, key):
        return key % self.capacity

    def resize(self, new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [None] * new_capacity
        for bucket in old_buckets:
            current = bucket
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def insert(self, key, value):
        # Choose hash function (multiplication or division)
        index = self.hash_function_multiplication(key)
        # index = self.hash_function_division(key)

        if not self.buckets[index]:
            self.buckets[index] = DoublyLinkedList()
        bucket = self.buckets[index]

        current = bucket.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        bucket.append(key, value)
        self.size += 1

        # Check if resizing is needed
        if self.size > self.capacity * 2:
            self.resize(self.capacity * 2)

    def get(self, key):
        index = self.hash_function_multiplication(key)
        bucket = self.buckets[index]

        current = bucket.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self.hash_function_multiplication(key)
        bucket = self.buckets[index]

        current = bucket.head
        while current:
            if current.key == key:
                bucket.remove(current)
                self.size -= 1
                # Check if resizing is needed
                if self.size < self.capacity // 4:
                    self.resize(self.capacity // 2)
                return
            current = current.next

    def print_table(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: ", end="")
            current = bucket.head if bucket else None
            while current:
                print(f"({current.key}: {current.value})", end=" -> " if current.next else "")
                current = current.next
            print()


# Example usage:
hash_table = HashTable()
hash_table.insert(1, 10)
hash_table.insert(2, 20)
hash_table.insert(3, 30)
hash_table.insert(4, 40)

print("Hash Table:")
hash_table.print_table()

print("Value for key 2:", hash_table.get(2))
hash_table.remove(2)
print("After removing key 2:")
hash_table.print_table()
