x=10
y='10'
print(id(x), id(y))
print(x is y)

z=[1,2,3,4]
w=[1,2,3,4]
print(id(z), id(w))
print(z is w)

a=['name' , 'alaika']
b=['name' , 'alaika']
print(id(a), id(b))
print(a is b)
