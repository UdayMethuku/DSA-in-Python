class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def delete_end(head,pos):
    
    
    if head is None:
        return None
    
    if pos==1:
        new_head=head.next
        new_head.prev=None

        return new_head
    cur=head
    for _ in range(pos-1):
        if cur is None:
            return head
        cur=cur.next
    if cur is None:
            return head
    
    
    if cur.next is None:
         cur.prev.next=None
         return head

    if cur.next is not None:
        cur.prev.next=cur.next
        cur.next.prev=cur.prev
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
    third=Node(3)
    fourth=Node(4)
    fifth=Node(5)

    first.next=sec
    sec.next=third
    third.next=fourth
    fourth.next=fifth

    fifth.prev=fourth
    fourth.prev=third
    third.prev=sec
    sec.prev=first

    print("orginal list:")
    print_list(first)

    pos=2
    head=delete_end(first,pos)
    print("list after delection:")
    print_list(head)
main()