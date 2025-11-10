# 1)Positional argument :=

# def display(x,y,z):
#     return x+y+z

# display(12)        ##wrong


# def display(x,y,z):
#     return x+y+z

# display(12,13)        ##wrong


# def display(x,y,z):
#     return x+y+z

# display(12,13,15,14)        ##wrong


# def display(x,y,z):
#     return x+y+z

# print(display(12,13,14))      ###correct


# def display(x,y,z):
#     print(y,x,z)

# display(12,13,14)         ##correct


#===============================================================================================
# 2)Default Positional argument

# def display(x=0,y=0,z=0):
#    print(x+y+z)

# display(12)        ##correct


# def display(x=0,y=0,z=0):
#    print(x+y+z)

# display(12,13)      ##correct


# def display(x=0,y=0,z=0):
#    print(x+y+z)

# display(12,13,14,15)      ##wrong 


# def display(x=0,y=0,z=0):
#    print(x+y+z)

# display(12,13,14)       ##correct

#===============================================================================================
# 3)Variable length Positional argument (*args)

# def display(*n):
#    print(n)
#    print(type(n))

# display(12)  
# display(10,20,13,'python',[1,2,3]) 
# display("al")



# def display(*n):
#    sum=0
#    for i in n:
#       for j in i:
#         sum=sum+j
#    print("sum=" , sum)

# x=eval(input("Enter : "))
# display(x)  


# def display(*n):
#    sum=0
#    for i in n:
#       sum=sum+i
#    print("Sum =" , sum)

# x=eval(input("Enter : "))
# display(*x)  

#===============================================================================================
def display(x,y=0,*z):
    print(x)
    print(y)
    print(z)

display(1,2,3,4,5,6,7,8,9,20,11,23)