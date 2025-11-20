# a=int(input("enter"))
# b=int(input("enter"))
# c=a/b
# print(c)

x=int(input("Enter a number: " ))
y=int(input("Enter a number: " ))
try:
    z=x/y
    print(z)

except ZeroDivisionError:
    print("please enter non zero value against y")

    
x = int(in)