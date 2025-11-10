#wap to check given no is armstrong or not
n=int(input("Enter a number : "))
count=0
digit=x=n
sum=0
while(n>0):
    count=count+1
    n=n//10
    
while(x>0):
    ld=x%10
    sum=sum+ld**count
    x=x//10

if(sum==digit):
    print( digit , " : Yes your number is Armstrong  " )
else:
    print("Not an Armstrong")
