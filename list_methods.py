# list methods in python
arr=list(map(int,input("enter numbers  separated by spaces:").split()))
print("array oprations")
print(" insert->1\n pop->2\n append->3\n remove->4\n index->5 \n reverse->6")
operation=int(input("enter number to perfrom operation:"))

try:
     
     if (operation == 1):
         index=int(input("enter index:"))
         value=int(input("enter value:"))
         arr.insert(index,value)
         print("array after insertion:",arr)
     
     elif (operation == 2):
         index=int(input("enter index to delete the value:"))
         print("popped value:",arr.pop(index))
         print("array after pop:",arr)
     
     elif (operation == 3):
         app=int(input("enter value to append:"))
         arr.append(app)
         print("new array with append value:",arr)
     
     elif (operation == 4):
         remove=int(input("enter value to remove from array:"))
         print("removed value:",remove)
         print("new array after deletion:",arr.remove(remove))
     
     elif (operation == 5):
         index=int(input("enter value to find first index occurence:"))
         print(arr.index(index))
     
     
     
     elif (operation == 6):
         print("reversed array:",arr.reverse())
     
     else:
         print("enter vaild operation")

except ValueError as e:
    print("error:",e)
except IndexError as e:
    print("index out of range:",e)
except Exception as e:
    print("An unexpected error occured:",e)
