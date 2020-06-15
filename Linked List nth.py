class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head= None
    self.size = 0

  def push(self,new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
    self.size += 1

  def getNth(self, index):

    current = self.head
    count = 0
    while current is not None:
      if index == count:
        print(current.data)
      count += 1
      current = current.next

  def printNthFromLast(self, index):
    temp = self.head
    if index > self.size:
      print("the index in llist does not exist")
    else:
      for i in range(0,self.size-index):
        temp = temp.next
      print(temp.data)

  def getSize(self):
    print(self.size)

  def printList(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next    
    # assert(False)
    # return 0

if __name__ == '__main__':
  llist = LinkedList()
  llist.push(5)
  llist.push(3)
  llist.push(7)
  llist.getSize()

  llist.printNthFromLast(654)
  # llist.getNth(0)
  # llist.printList()