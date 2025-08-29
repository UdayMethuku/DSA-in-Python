class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def update(head,new_data):

    new_node=Node(new_data)

    new_node.next=head
    if head is not None:
        
     head.prev=new_node
    return new_node

def print_list(head):

    cur=head
    while cur:
        print(cur.data,end="<->")
        cur=cur.next
    print("None")

def main():
  
    first=Node(1)
    sec=Node(2)
    thrid=Node(3)

    first.next=sec
    sec.next=thrid
    sec.prev=first
    thrid.prev=sec
    
    new_data=int(input("enter the value to insert at front:"))
    head=update(first,new_data)
    print_list(head)
main()


