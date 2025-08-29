class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def occurance(head,key):
    count=0
    cur=head
    while cur:
        if cur.data==key:
            count+=1
        cur=cur.next
    return count
def main():
    head=Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(6)
    
    key=1
    result=occurance(head,key)
    print("count=",result)
main()