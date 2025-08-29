class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def delete(head):
    
    if head is None:
        return None

    if head.next is None:
        return None  

    new_head=head.next
    new_head.prev=None
    
    return new_head




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
    head=delete(first)
    print("list after delection:")
    print_list(head)
main()