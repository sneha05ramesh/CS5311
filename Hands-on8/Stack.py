class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value

    def isempty(self):
        return self.top == -1


# Example:
stack = Stack(6)

stack.push(5)
stack.push(4)
stack.push(3)

print("Is the stack empty?", stack.isempty())

print("Popped element:", stack.pop())
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())
print("Is stack empty?", stack.isempty())
