# class Book:
#     price=100
#     def _init_(self,title , branch):
#         self.t = title
#         self.b = branch



# obj = Book('python book' , 'IT' )
# print(obj.price)

# obj2 = Book("Python Book" , 'IT')
# print(obj2.price)

#=========================================================================
class Book:
    price=100
    def __init__ (self, title, branch):
        self.t=title
        self.b=branch

    @classmethod
    def update_price (cls, newprice):
        cls.price=newprice

Obj= Book ('python', 'IT')
print(Obj.price)

x = float(input("Enter new price:"))

Obj.update_price(x)
print(Obj.price)