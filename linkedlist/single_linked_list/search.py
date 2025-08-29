class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

def search(head,key):

# iteration approach
    # while head is not None:

    #     if head.data==key:
    #       return True
    #     head=head.next
    
    # return False


# recursive approach
     if  head is None:
        return False
     if head.data==key:
         return True
     return search(head.next,key)
  

    



def main():
    head=Node(1)
    head.next=Node(10)
    head.next.next=Node(7)
    head.next.next.next=Node(8)
    
    key=7

    if  search(head,key):
        print("yes")
    else:
        print("No")
main()
