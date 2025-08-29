#double linked list traversal(forword)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def print_list(head):

#iterative approach
    # cur=head
    # while cur:
    #     print(cur.data,end="<->")
    #     cur=cur.next
    # print("None")

#recursive approach
    if head is None:
        print("None")
        return
    
    print(head.data,end="<->")
    
    print_list(head.next)
   

def main():

    first=Node(1)
    sec=Node(2)
    thrid=Node(3)

    first.next=sec
    sec.next=thrid
    sec.prev=first
    thrid.prev=sec

    print_list(first)
main()