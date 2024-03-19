class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, value):
        if self.count == self.size:
            print("Queue Overflow")
            return
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            print("Queue Underflow")
            return None
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return value

    def isempty(self):
        return self.count == 0


# Example:
queue = Queue(6)

queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

print("Is queue empty?", queue.isempty())

print("Dequeued element:", queue.dequeue())
print("Dequeued element::", queue.dequeue())
print("Dequeued element::", queue.dequeue())
print("Is queue empty?", queue.isempty())
