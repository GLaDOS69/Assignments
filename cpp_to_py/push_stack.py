class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def peek(self):
    return self.items[-1]

  def is_empty(self):
    return len(self.items) == 0

  def size(self):
    return len(self.items)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())  
print(stack.is_empty())  
print(stack.size())  
