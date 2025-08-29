class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printt_list(cur,head):

# Using Iterative Method
#     if head is None:
#         return
    
#     cur=head
#     while True:
#       print(cur.data,end="<->")
#       cur=cur.next
#       if cur.next ==head:
#           print(head.data)
#           break
    

    if head is None:
        return
    print(cur.data,end=" ")
    
    if cur.next ==head:
        return
    printt_list(cur.next,head)



def main():
    head=Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head
    

    # printt_list(head)
    printt_list(head,head)
    
main()

