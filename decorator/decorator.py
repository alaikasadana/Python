#syntax
# def decor (funname):
#     _____________
#     _____________
#     _____________

#     return function

# def outer_func(fun_name):
#     def inner_func(x,y):
#         x=x+5
#         y=y+10
#         return fun_name(x,y)
#     return inner_func

# @outer_func
# def add(x,y):
#     print(x+y)

# add(10,20)  


def outer(fun):
    def inner(x,y):
        x=x+10
        y=y+20
        return fun(x,y)
    return inner

@outer
def sub(x,y):
    print(y-x)

sub(10,5)