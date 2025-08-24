a=list(map(int,input("enter number:").split()))
b=[]
cur=0

for num in a:
   cur+=num
   b.append(cur)
print(b)

