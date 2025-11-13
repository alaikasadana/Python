# class Student:
#     x=10
#     def __init__(self,name):
#         self.n=name 
    
#     @staticmethod
#     def showdata():
#         print(Student.x)

# obj =Student("alaika")
# obj.showdata()

#============================================================================================================         

class Student:
    x=10
    def __init__(self,name):
        self.n=name 
    
    @staticmethod
    def greet(name):
        print(f'Welcome {name}')

obj =Student("alaika")
x=obj.n
obj.greet(x)