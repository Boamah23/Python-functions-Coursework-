def deleteNode(self):
          n = x = self.head 
          while n!= None:
              while x.next!= None:
                  if x.next.value == n.value: #checks the next value pointed to is the same
                      x.next = x.next.next #pointers skip over node so node is essentially deleted
                  else:
                      x = x.next #if value is not the same move on to the next
              n = x = n.next
