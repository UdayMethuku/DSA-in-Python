class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def delete(last,key):
    if last is None:
        print("empty list")
        return None
    cur=last.next
    prev=last
    if cur == last and cur.data ==key:
        return None
    
    if cur.data==key:
        last.next=cur.next
        return last
    
    while cur!=last and cur.data!=key:
        prev=cur
        cur=cur.next
    if cur.data==key:
        prev.next=cur.next
        if cur==last:
            last=prev
    else:
        print(f"node with {key} not found")
    return last

def print_list(last):
    if last is None:
        print("List is Empty")
        return

    head = last.next
    while True:
        print(head.data, end=" ")
        head = head.next
        if head == last:
            break
    print()

def print_list(last):
    if last ==None:
        print("list is empty")
        return
    
    head=last.next
    cur=head
    while True:
        print(cur.data,end=" ")
        cur=cur.next
        if cur ==head:
            break
    print()
def main():
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    last=head.next.next.next
    last.next=head

    key=3
    res=delete(last,key)
    print_list(res)
main()
