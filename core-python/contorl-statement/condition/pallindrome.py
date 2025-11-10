#wap program to check the value is pallidrome or not

n=input("Enter any value:")

if(n==n[::-1]):
    print("yes")
else:
    print("no")