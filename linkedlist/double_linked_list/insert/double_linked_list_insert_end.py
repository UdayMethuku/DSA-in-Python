class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

# def update(third,new_data):

    # new_node=Node(new_data)

    # new_node.prev=third

    # if third is not None:
    #      third.next=new_node
    
def update(head,new_data):
    new_node=Node(new_data)
    if head is None:
        head=new_node
    else:
       
       cur=head
       while cur.next:
           cur=cur.next
       
       cur.next=new_node
       new_node.prev=cur

    return head


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
    
    new_data=int(input("enter the value to insert at last:"))
    head=update(thrid,new_data)
    print_list(first)
main()


