class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self, size):
        self.size = size
        self.nodes = [None] * size
        self.head = None
        self.free_list = list(range(size))

    def allocate_node(self, value):
        if not self.free_list:
            print("Out of memory")
            return None
        index = self.free_list.pop(0)
        self.nodes[index] = Node(value)
        return index

    def free_node(self, index):
        self.nodes[index] = None
        self.free_list.append(index)

    def insert(self, value):
        index = self.allocate_node(value)
        if index is None:
            return
        if self.head is None:
            self.head = index
        else:
            current = self.nodes[self.head]
            while current.next is not None:
                current = self.nodes[current.next]
            current.next = index

    def search(self, value):
        current_index = self.head
        while current_index is not None:
            current = self.nodes[current_index]
            if current.value == value:
                return True
            current_index = current.next
        return False

    def delete(self, value):
        if self.head is None:
            return
        if self.nodes[self.head].value == value:
            self.free_node(self.head)
            self.head = self.nodes[self.head].next
            return
        previous_index = self.head
        current_index = self.nodes[self.head].next
        while current_index is not None:
            current = self.nodes[current_index]
            if current.value == value:
                self.nodes[previous_index].next = current.next
                self.free_node(current_index)
                return
            previous_index = current_index
            current_index = current.next

    def display(self):
        current_index = self.head
        while current_index is not None:
            current = self.nodes[current_index]
            print(current.value, end=" -> ")
            current_index = current.next
        print("None")


# Example:
linked_list = SinglyLinkedList(10)

linked_list.insert(7)
linked_list.insert(8)
linked_list.insert(10)

print("Linked list:")
linked_list.display()

print("Search for 10:", linked_list.search(10))
print("Search for 4:", linked_list.search(6))

linked_list.delete(8)
print("Linked list after deleting 8:")
linked_list.display()
