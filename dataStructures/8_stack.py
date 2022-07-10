class Node:
  def __init__(self, value) -> None:
    self.value = value
    self.next = None    

class Stack:
  top = dict
  bottom = dict
  length = 0

  
  def __init__(self, value) -> None:
    node = Node(value)
    self.bottom = node
    self.top = self.bottom
    self.length = 1
    
  def peek(self):
    if (self.top != None):
      return print(self.top.value)
    else:
      return print("Nothing to peek")
  
  def push(self, value):
    node = Node(value)
    if (self.length == 0):
      self.top = node
      self.bottom = node
    else:
      holdingPointer = self.top
      self.top = node
      self.top.next = holdingPointer
    self.length += 1
  
  def pop(self):
    if (self.top != None):
      self.top = self.top.next
      self.length -= 1
    else:
      return print("Nothing to pop")
    # self.top = self.top.
  
  
stack = Stack("9gag")
stack.peek()
stack.push("discort")
stack.peek()
stack.push("Udemy")
stack.peek()
stack.push("google")
stack.peek()

stack.pop()
stack.peek()
stack.pop()
stack.peek()
stack.pop()
stack.peek()
stack.pop()
stack.peek()

stack.pop()
stack.peek()

stack.pop()
stack.peek()
