print("\n 1.square \n 2.tiangle\n 3.diamond\n 4.right angle triangle\n 5.reverse 90' traiangle \n 6.hallow square 7.mirror image Traingle")
n=int(input("enter pattern number:"))
size=int(input("enter pattern size:"))

if n==1:
    print("SQUARE")
    for i in range(size):
        for j in range(size):
            print(" * ",end='')
        print()

elif n==2:
  print("TRIANGLE")
  for i in range(size):
      print( (size-i)*"   ",((2*i)-1)*" * ")
 

elif n==3:
  print("DIAMOND")
  for i in range(size):
      print( (size-i)*"   ",((2*i)-1)*" * ")
  for i in range(size-1,0,-1):
      print( (size-i)*"   ",((2*i)-1)*" * ")

elif n==4:
    print("90' TRIANGLE")
    for i in range(size):
        print((2*i-1)*"*")

elif n==5:
    print("REVERSE 90' TRIANGLE")
    for i in range(size-1,0,-1):
        print((2*i-1)*"*")

elif n==6:
   print("HALLOW SQUARE")
   for i in range(size):
       for j in range(size):
          if j==0 or j==size-1 or i==0 or i==size-1:
           print("*",end=' ')
          else:
             print(" ",end=" ")
       print()

elif n==7:
  print("MIRROR IMAGE TRIANGLE")
  for j in range(size-1,0,-1):
        print( (size-j)*"   ",((2*j)-1)*" * ")
  
  for i in range(size):
        print( (size-i)*"   ",((2*i)-1)*" * ")
 