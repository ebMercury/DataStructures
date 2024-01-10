class Node:
  def __init__(self,d):
    self.data = d
    self.next = None
class LinkList:
  def __init__(self):
    self.head = None
  
  def display(self):
    t = self.head
    while t != None:
      print(t.data, end='->')
      t = t.next
    print('Null')

  def Instart(self, d):
    n = Node(d)
    n.next = self.head
    self.head = n
  
  def Inend(self, d):
    n = Node(d)
    if self.head is None:
      self.head = n
      return
    t = self.head
    while(t.next):
      t = t.next
    t.next = n

  def Inafter(self, m, d):

  
  def RemoveNode(self, d):
    t =  self.head
    if (t is not None):
      if (t.data == d):
        self.head = t.next
        t = None
        return
    while (t is not None):
      if t.data == d:
        break
      p = t
      t = t.next
    if (t == None):
      return
    p.next = t.next
    t = None


x = Node(3)
y = Node(4)
z = Node(5)
s = LinkList() 
s.head = x
x.next = y
y.next = z
s.display()