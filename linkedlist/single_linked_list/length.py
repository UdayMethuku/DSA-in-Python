class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

def  length(head):
    sum=0

# iteration approach
    # while head is not None:
    #     sum=sum+1
    #     head=head.next
    # return sum

    
# recursive approach    
    if head is None:         
         return 0
    
    return 1+length(head.next)



def main():

    head=Node(1)
    head.next=Node(1)
    head.next.next=Node(1)
    head.next.next.next=Node(1)
    print("length of the linked list:",length(head))
main()