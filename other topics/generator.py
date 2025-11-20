# x = range(1000)
# print(x)
# print(list(x))


#==============================================================================================================

def gen_num(n):
    i=1
    while(i<=n):
          yield i
          i=i+1
    
n=int(input("Enter : "))
var=gen_num(n)
print(var)

ele1 = next(var)
print(ele1)

ele2 = next(var)
print(ele2)





    