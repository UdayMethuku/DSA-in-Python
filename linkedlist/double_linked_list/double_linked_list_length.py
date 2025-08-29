#double linked list traversal(forword)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None



#iterative approach
    # cur=head
    # while cur:
    #     print(cur.data,end="<->")
    #     cur=cur.next
    # print("None")
#double linked list traversal(forword)


def count_list(head):

#iterative approach
    # cur=head
    # count=0
    # while cur:
    #     count=count+1
    #     cur=cur.next
    # return count

#recursive approach
    if head is None:
        return 0
    
    
    
    return 1+count_list(head.next)
   

def main():

    first=Node(1)
    sec=Node(2)
    thrid=Node(3)

    first.next=sec
    sec.next=thrid
    sec.prev=first
    thrid.prev=sec

    print(f"length of double linked list={count_list(first)}")
main()