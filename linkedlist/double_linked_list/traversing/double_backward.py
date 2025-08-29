class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def print_list(tail):
#iterative approach 
    # cur=tail
    # while cur:
    #     print(cur.data,end="<->")
    #     cur=cur.prev
    # print("None")

#recursive approach

    if tail is None:
        print("None")
        return
    
    print(tail.data,end="<->")
    print_list(tail.prev)

def main():

    first=Node(1)
    sec=Node(2)
    third=Node(3)

    first.next=sec
    sec.next=third
    sec.prev=first
    third.prev=sec

    print_list(third)
main()