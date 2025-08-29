class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def delete(last):
    if last==None:
        return None
    head=last.next
    if head==last:
        last=None
    else:
        last.next=head.next
    return last
def print_list(last):
    head=last.next
    
    while True:
        print(head.data,end=" ")
        head=head.next
        if head ==last.next:
            break
        
        


def main():
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)

    last=head.next.next.next
    last.next=head
    
    re=delete(last)
    print_list(re)
main()
    
    