class Node:

  def __init__(self,data):
    self.data=data
    self.next=None



def insert(head,new_data,pos):
  
  new_node=Node(new_data)

  if pos==1:
    new_node.next=head
    return new_node
  
  cur=head

  for _ in range(1,pos-1):
    if cur == None:
      break
    cur=cur.next

  if cur is None:
        print("Enter vaild position:")
        return head

  new_node.next=cur.next

  cur.next=new_node

  return head
    
  


def print_list(head):
  
  cur=head

  while cur is not None:
    print(cur.data,end="->")
    cur=cur.next
  print("None")

def main():

  values=list(map(int,input("enter values:").split()))

  head=Node(values[0])

  cur=head

  for value in values[1:]:

    cur.next=Node(value)
    cur=cur.next

  new_data=int(input("enter new value to insert:"))
  pos=int(input("enter position of new values to insert:"))

  head=insert(head,new_data,pos)

  print_list(head)
main()


