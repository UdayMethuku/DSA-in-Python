a=input("enter string:")
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
c="".join(b)
if c==a:
    print("palindrome")
else:
    print("not palindrome")


# second methond for palindrome
      # a=input("enter string:")
      # b=a[::-1]
      # if b==a:
      #     print("palindrome")
      # else:
      #     print("not palindrome")