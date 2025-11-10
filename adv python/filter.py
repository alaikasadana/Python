# L=[50,60,70,65,40,30,90]
# def division(n):
#     if n>=60 :
#         return n
# print(list(filter(division,L)))

#==============================================================

# L = eval(input("Enter : "))
# def even (n):
#     if n%2 == 0:
#         return n
    
# print(list(filter(even,L)))

#==============================================================

# L = eval(input("Enter : "))
# def odd(n):
#     if n%2 != 0:
#         return n
    
# print(list(filter(odd,L)))

#==============================================================

# l = input("Enter : ")
# def vowel(n):
#      if n in ('a','e','i','o','u','A','E','I','O','U'):
#           return n
# # res=(list(filter(vowel,l)))
# # print(''.join(res))
# print(''.join(list(filter(vowel,l))))


# without function
# s=input("Enter : ")
# s1=''

# for i in s :
#     if i in ('a','e','i','o','u','A','E','I','O','U'):
#         s1=''.join([s1,i])

# print(s1)
 
#==================================================================
s=input("Enter : ")
v=c=0

for i in s :
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        v=v+1
    elif i==' ':
        pass
    else:
        c=c+1

print(v,c)


