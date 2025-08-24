a=int(input("enter number:"))
if a<0:
    print("enter poistive numbers")
else:
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count=count+1
    if count==2:
        print(a,"is prime")
        
    else:
        print(a,"is not prime")
      
    
    
