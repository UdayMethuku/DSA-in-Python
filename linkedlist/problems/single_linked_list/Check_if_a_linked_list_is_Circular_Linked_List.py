class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printt_list(head):

    if head is None:
        return
    
    cur=head
    while True:
     
      cur=cur.next
      if cur.next ==head:
          return True
          
    



def main():
    head=Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = head
    

    result=printt_list(head)
    print("True -> cuircular list\nFalse -> cuircular list")
    print("cuircular list=",result)
    
main()