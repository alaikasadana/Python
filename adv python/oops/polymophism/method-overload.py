class Student:
    def add(self,x,y):
        print(x+y)
    def add(self,x,y,z):
        print(x+y+z)
    def add(self,x,y,z,p):
        print(x+y+z+p)

obj = Student()
# obj.add(10,20)
# obj.add(10,20,30)
obj.add(10,20,30,40)
