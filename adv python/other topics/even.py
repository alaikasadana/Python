def outer(even):
    def inner(x):
        even(x)
        value=range(1,x+1,2)
        return list(value)
    return inner

@outer
def operation(n):
    x=range(2,n+1,2)
    return list(x)

n=int(input("Enter value : "))
res=operation(n)
print(res)
