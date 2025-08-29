def arr(a,target):

    n=len(a)
    if target in a:
       return ("single", a.index(target))

    else:
      for i in range(n):
          for j in range(i+1,n):
              if a[i]+a[j]==target:
                  return ("pair",i,j)
      return False

a= [0, -1, 2, -3, 1]
target =int(input("enter the value to find two sum:"))
result=arr(a,target) 

if result ==False:
    print("Not found")
elif result[0] == "single":
    print(f"Single element found at index {result[1]} → {a[result[1]]}")
else:
   i, j = result[1], result[2]
   print("Indices:", i, j)
   print(f"{a[i]} + {a[j]} = {a[i] + a[j]}")
  