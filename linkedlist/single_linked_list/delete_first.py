class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



def delete(head):

    if head is None:
        return None
    
   

    head=head.next
    
    return head


def print_list(head):
    
    cur=head

    while cur is not None:
        print(cur.data,end="->")
        cur=cur.next
    print("None")

def main():


    head = Node(3)
    head.next = Node(12)
    head.next.next = Node(15)
    head.next.next.next = Node(18)

    # values=list(map(int,input().split()))
    # head=Node(values[0])

    # for value in values[1:]:
    #     head.next=Node(value)
    #     head=head.next
    
    head=delete(head)
    print_list(head)

main()

