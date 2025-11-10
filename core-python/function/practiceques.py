# wap to print factorial of any number through function

def factorial(num):
    fac = 1
    for i in range(1,num+1):
        fac = fac * i
    
    return fac
    

n = int(input("Enter : "))
print(f"Factorial of {n} is " , factorial(n))


#===============================================================================================
#wap to print upto n even number

# def even(n):
#     for i in range (2,n+1,2):
#         print(i)

# num=int(input("Enter : "))
# even(num)


#===============================================================================================
#wap to print upto n odd number

# def even(n):
#     for i in range (1,n+1,2):
#         print(i)

# num=int(input("Enter : "))
# even(num)
