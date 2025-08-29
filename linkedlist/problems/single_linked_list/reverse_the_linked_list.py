class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

def traverse(head):

# iteration approach
    stack=[]
    while head is not None:
         stack.append(head.data)
         head=head.next
    while stack:
        print(stack.pop(),end=" ")

    

# recursive approach
    # if  head is None:
    #     print()
    #     return
    # print(head.data,end="->")
    # traverse(head.next)






def main():

    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)

    traverse(head)
main()
