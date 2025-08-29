class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None




def insert_position(head,pos,new_data):
    new_node=Node(new_data)
    
    if pos ==0:
        new_node.next=head

    
        if head is not None:
            head.prev = new_node
        return new_node
    
    cur=head
    for _ in range(pos-1):
        if cur is None:
            return head
        cur=cur.next
        
    if cur is None:
            return head
    new_node.prev=cur
    new_node.next=cur.next
    if cur.next is not None:
        cur.next.prev=new_node
    cur.next=new_node
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
    
    new_data=100
    pos=2
    head=insert_position(first,pos,new_data)
    print_list(head)
main()



        