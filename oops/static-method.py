class Book:
    Price=100
    def _init_(self , title , branch):
        self.t = title
        self.b = branch


    @classmethod 
    def update_price(cls,newprice):
        cls.Price = newprice


obj = Book('python' , "IT")
print(obj.Price)

x = float(input("Enter new price :"))
obj.update_price(x)
print(obj.Price)
