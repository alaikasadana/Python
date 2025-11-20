#map with lambda

# l=[1,2,3,4,5]
# print(list(map(lambda n:n*n , l)))

# print(list(map(lambda n : 'even' if n%2==0 else 'odd' , l)))

#==============================================================================

#filter with lambda

# l=[1,2,3,4,5]
# print(list(filter(lambda n : n if n%2==0 else None, l)))

# print(list(filter(lambda n : n if n%2!=0 else None, l)))

#===============================================================================

#reduce with lambda

# from functools import reduce
# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x+y ,l ))
# print(reduce(lambda x,y:x*y ,l ))
# print(reduce(lambda x, y: x if x > y else y, l))
# print(reduce(lambda x, y: x if x < y else y, l))


# largest = reduce(lambda x, y: x if x > y else y, l)
# l.remove(largest)
# print(reduce(lambda x, y: x if x > y else y, l))



# from functools import reduce
# l=[1,2,3,4,5]
# n=int(input("Enter : "))

# if n<=len(l):
#     for _ in range(n):
#         largest = reduce(lambda x, y: x if x < y else y, l)
#         l.remove(largest)

#     print(f'{n} Max digit is {largest}')

# else:
#     print("Enter valid input !!!!")



# from functools import reduce
# l=[1,2,3,4,5]
# n=int(input("Enter : "))

# if n<=len(l):
#     for _ in range(n):
#         minimum = reduce(lambda x, y: x if x < y else y, l)
#         l.remove(minimum)

#     print(f'{n} Min digit is {minimum}')

# else:
#     print("Enter valid input !!!!")
#==================================================================================














