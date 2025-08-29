# Count nodes in Circular linked list
class  Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def length(head):
    cur=head
    count=0
    while True:
        count+=1
        if cur.next==head:
            break
       
        cur=cur.next
    return count
def main():
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=head

    result=length(head)

    print("length of linked list=",result)

main()


        