# n = int(input("Enter value : "))
# for i in range(n):
#     print(i , end=" ")




#IN COMPRIHENSION WE CAN ONLY USE FOR LOOP AND IF WITH FOR LOOP AND ONLY POSSIBLE IN COLLECTION (tuple cannot be used)
#=============================================================================================================================

# n = int(input("Enter value : "))
# print([i for i in range(n)])
# print([i for i in range(1,n+1)])                                   #from 1
# print([2*i for i in range(1,n+1)])                                  #even
# print([2*i-1 for i in range(1,n+1)])                               #odd


# x = [2*i for i in range(1,n+1)]
# print(*x)                                                            #unpacking of list


#=================================================================LIST=========================================================

# n = int(input("Enter value : "))
# print([i for i in range(1,n+1) if i%2==0])
# print([i for i in range(1,n+1) if i%2!=0])
# print([('even' if i%2==0 else 'odd')for i in range(1,n+1)])
# print([(('even',i) if i%2==0 else 'odd')for i in range(1,n+1)])
# print(['even' if n%2==0 else 'odd'])                                            #we dont use this usally

#====================================================================DICT=========================================================

# n = int(input("Enter value : "))
# print({i:i**2 for i in range(1,n)})
# print({i:i**2 for i in range(1,n) if i%2==0})


#=====================================================================SET========================================================

# n = int(input("Enter value : "))
# print({i**2 for i in range(1,n) if i%2==0})

#=======================================TUPLE (BUT WITH TYPECASTING)=============================================================
# n = int(input("Enter value : "))
# print(tuple([i for i in range(n)]))
# print((i for i in range(n)))                   #yeh address bta dega



