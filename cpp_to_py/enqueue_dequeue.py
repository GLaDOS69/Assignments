class Queue:
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    return self.items.pop(0)

  def peek(self):
    return self.items[0]

  def is_empty(self):
    return len(self.items) == 0

  def size(self):
    return len(self.items)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())  
print(queue.dequeue())  
print(queue.dequeue())  
print(queue.is_empty())  
print(queue.size())  
