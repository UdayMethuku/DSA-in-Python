a=list(map(int,input("enter number:").split()))
w=int(input("enter window size:"))
if len(a)<w:
    print("Invalid")
else:
   b=sum(a[:w])
   max_value=b
   
   for i in range(len(a)-w):
       b=b-a[i]+a[i+w]
       c=max(b,max_value)
   print(c)