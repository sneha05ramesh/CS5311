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
        self.array = [None] * initial_capacity

    def hash_function_multiplication(self, key):
        A = 0.5
        return int(self.capacity * ((key * A) % 1))

    def hash_function_division(self, key):
        return key % self.capacity

    def resize(self, new_capacity):
        old_array = self.array
        self.capacity = new_capacity
        self.array = [None] * new_capacity
        for linked_list in old_array:
            current = linked_list.head if linked_list else None
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def insert(self, key, value):
        index = self.hash_function_multiplication(key)
        # index = self.hash_function_division(key)

        if not self.array[index]:
            self.array[index] = DoublyLinkedList()
        linked_list = self.array[index]

        current = linked_list.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        linked_list.append(key, value)
        self.size += 1

        # Check if resizing is needed
        if self.size > self.capacity * 2:
            self.resize(self.capacity * 2)

    def get(self, key):
        index = self.hash_function_multiplication(key)
        # index = self.hash_function_division(key)
        linked_list = self.array[index]

        current = linked_list.head if linked_list else None
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self.hash_function_multiplication(key)
        # index = self.hash_function_division(key)
        linked_list = self.array[index]

        current = linked_list.head if linked_list else None
        while current:
            if current.key == key:
                linked_list.remove(current)
                self.size -= 1
                # Check if resizing is needed
                if self.size < self.capacity // 4:
                    self.resize(self.capacity // 2)
                return
            current = current.next

    def print_table(self):
        for i, linked_list in enumerate(self.array):
            print(f"Index {i}: ", end="")
            current = linked_list.head if linked_list else None
            while current:
                print(f"({current.key}: {current.value})", end=" -> " if current.next else "")
                current = current.next
            print()

hash_table = HashTable()
hash_table.insert(5, 10)
hash_table.insert(6, 50)
hash_table.insert(8, 3)
hash_table.insert(3, 1000)

print("Hash Table:")
hash_table.print_table()

print("Value for key 3:", hash_table.get(3))
hash_table.remove(3)
print("After removing key 3:")
hash_table.print_table()
