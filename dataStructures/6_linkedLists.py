class Node:
  def __init__(self, value) -> None:
    self.value = value
    self.next = None      

class LinkedList:
  head = dict
  tail = dict
  
  length = 0

  def __str__(self):
        return "From str method of Test: a is %s, b is %s" % (self.head, self.tail)

  def __init__(self, value):
    node = Node(value)

    self.head = node
    self.tail = self.head
    self.length = 1

  def append(self, value):
    node = Node(value)  
    self.tail.next = node
    self.tail = node
    self.length+=1

  def prepend(self, value):
    node = Node(value)

    node.next = self.head
    self.head = node
    self.length += 1

  def printList(self):
    currNode = self.head
    myList = []

    while (True):
      if(not hasattr(currNode, "value")):
        break
      myList.append(currNode.value)
      currNode = currNode.next
    print(myList)


  def insert(self, index, value) -> None:
    currIndex = 0
    currNode = self.head
    previousNode = None
    if (index < 0):
      print("ERROR: incorrect index! Index {}, max index {}".format(index, self.length-1))
      return
    if (index >= self.length):
      self.append(value)
      return
    while(currIndex+1 < self.length):
      if (currIndex == index):
        newNode = Node(value)

        if (currIndex == 0):
          newNode.next = currNode
          self.head = newNode
          break

        newNode.next = currNode
        previousNode.next = newNode
        break
      previousNode = currNode
      currNode = currNode.next
      currIndex+=1

    self.length+=1

  def remove(self, index):

    if (index < 0 or index >= self.length):
      print("ERROR: incorrect index! Index {}, max index {}".format(index, self.length-1))
      return

    currIndex = 0
    currNode = self.head
    previousNode = None

    while(currIndex+1 < self.length):
      if (currIndex == index):
        if(index == 0):
          self.head = currNode.next
          break
        previousNode.next = currNode.next
      previousNode = currNode
      currNode = currNode.next
      currIndex+=1

    self.length-=1
      





ls1 = LinkedList(10)

ls1.append(6)
ls1.append(16)


ls1.append(100)

ls1.prepend(99)
ls1.prepend(69)

print(ls1.head)
print(ls1.tail)
print(ls1)

ls1.insert(2, 404)
ls1.insert(0, 1000)
ls1.insert(0, 1001)
ls1.insert(-1, 44)
ls1.insert(8, 44)
ls1.insert(7, 666)
ls1.insert(100, 77)
ls1.remove(1)
ls1.remove(0)
ls1.printList()