class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
 
class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
     
      def deleteNode(self):
          n = x = self.head
          while n!= None:
              while x.next!= None:
                  if x.next.value == n.value:
                      x.next = x.next.next
                  else:
                      x = x.next
              n = x = n.next
              
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))
         

l=List()
l.insert(None, Node(4))
l.insert(l.head,Node(6))
l.insert(l.head,Node(6))
l.insert(l.head,Node(6))
l.insert(l.head,Node(8))
l.insert(l.head,Node(8))
l.insert(l.head,Node(5))
l.insert(l.head,Node(7))
l.deleteNode()
l.display()
