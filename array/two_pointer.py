def  two_pointer(a,target):

    for i in range(len(a)):
      for j in range(i+1,len(a)):
          
          if a[i]+a[j]== target:
              return ("Target found")
          
    return ("Target not found")

a=list(map(int,input("enter values:").split()))
target=int(input("enter target:"))
result=two_pointer(a,target)

print(result)