class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def delete(last):
    if last is None:
        print("empty list")
        return None
    head=last.next
    if head == last:
        last=None
    else:
        last.next = head.next
    return last
def print_list(last):
    if last is None:
        return
    head=last.next
    
    while True:
        print(head.data,end=" ")
        if head==last.next:
            break
        head=head.next


def main():
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)

    last=head.next.next.next
    last.next=head
    re=delete(last)
    print_list(re)
main()
    
    