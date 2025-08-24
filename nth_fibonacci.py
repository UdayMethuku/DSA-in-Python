def num(n):
    if  n==0:
        return 0
    elif n==1 :
     return 1
    else:
       
       return num(n-1)+num(n-2)
n=int(input("enter number to find fibonacci series:"))
b=num(n)
print(f"{n}th of fibonacci:{b}")
