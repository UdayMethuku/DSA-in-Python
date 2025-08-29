class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def delete(head,pos):
    temp=head
    prev=None

    if temp is None:
        return head

    if pos == 1:
        head=temp.next
        print("linked list after deletion:")
        return head
    
    for _ in range(1,pos):
        prev=temp
        temp=temp.next
        
        if temp is None:
            print("enter vaild position to delete:")
            return head
    
    if temp is not None:
        prev.next=temp.next
    print("linked list after deletion:")
    return head

def print_list(head):
  
  cur=head
  while cur is not None:
      print(cur.data,end="->")
      cur=cur.next
  print("None")



def main():
    

    values=list(map(int,input("enter values in the linked list:").split()))
    head=Node(values[0])
    cur=head
    for value in values[1:]:
        cur.next=Node(value)
        cur=cur.next



    # head.next=Node(2)
    # head.next.next=Node(1)
    # head.next.next.next=Node(1)
    # head.next.next.next.next=Node(1)
    
    print("orginal list:")
    print_list(head)
    
    pos=int(input("enter the position  to delete:"))
    head=delete(head,pos)
  
    print_list(head)

main()