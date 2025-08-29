class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

def front(head,new_data):

    new_node=Node(new_data)

    last=head

    while last.next:
        last=last.next

    last.next=new_node
    
    return head


def traverse(head):
   
    while head is not None:

        print(head.data,end=" ")
        head=head.next
    print()


def main():
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    
    new_data=88

    head=front(head,new_data)
    traverse(head)

    

main()        
