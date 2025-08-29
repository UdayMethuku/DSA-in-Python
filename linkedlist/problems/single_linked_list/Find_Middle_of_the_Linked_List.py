# Find Middle of the Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def length(head):
  
    if head.next == None:
     return 1
    else:
      cur=head
      count=0
      while cur:
          count=count+1
          cur=cur.next
      return count
 
def node(head,a):
    

    mid=a//2
    
      
    for _ in range(mid):
        head=head.next
    return head.data




def main():
    head=Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
   
    
    len=length(head)
    result=node(head,len)
    print("mid of the linked list=",result)
    
        
main()