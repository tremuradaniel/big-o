class Node:
  def __init__(self, value) -> None:
    self.value = value
    self.left = None
    self.right = None
    
#             9
#        4        20
#      1   6    15  170
    
class BinarySearchTree:
  def __init__(self):
    self.root = None
    
  def insert(self, value):
    node = Node(value)
    if self.root == None:
      self.root = node
    else:
      self.__attachToParent(node)
      
      
  def __attachToParent(self, node):
    parent = self.__findParent(self.root, node)
    if parent.value > node.value:
      parent.left = node
    else:
      parent.right = node
      
  def __findParent(self, upperNode, node) -> Node:
    if upperNode.value > node.value:
      if upperNode.left == None:
        return upperNode
      return self.__findParent(upperNode.left, node)
    else:
      if upperNode.right == None:
        return upperNode
      return self.__findParent(upperNode.right, node)
 
    
  
  def lookup(self, value):
    currentNode = self.root
    if currentNode == None:
      return 'N/A'
    while True:
      if currentNode.value == value:
        return currentNode

      if currentNode.value > value and currentNode.left != None:
        currentNode = currentNode.left
      elif currentNode.value < value and currentNode.right != None:
        currentNode = currentNode.right
      else:
        return 'N/A'
      
  
  
bST = BinarySearchTree()

bST.insert(9)
bST.insert(4)
bST.insert(20)
bST.insert(15)
bST.insert(170)
bST.insert(6)
bST.insert(1)

print(bST.root)


print(bST.lookup(170).value == 170)
print(bST.lookup(1).value == 1)
print(bST.lookup(171) == 'N/A')