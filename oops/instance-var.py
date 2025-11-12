# class Student:
#     def __init__(self,name,rollno):
#         self.n=name 
#         self.r=rollno

# obj = Student("alaika",124)
# obj.c='12345'

#======================================================================================================
#declaration ways

# class Student:
#     def __init__(self,name,rollno):
#         self.n=name                               #declaration
#         self.r=rollno
#     def addnew(self,contact):
#         self.c=contact                    #declaration

# obj = Student("alaika",124)
# obj.addnew(12233)

# obj.school='shsss'                 #declaration

#========================================================================================================
#calling

class Student:
    def __init__(self,name,rollno):
        self.n=name 
        self.r=rollno
        print(self.n ,self.r)                 #call
    def addnew(self,contact):
        self.c=contact   
        print(self.n ,self.r,self.c)            #call
    

obj = Student("alaika",124)
obj.addnew(1234455)
obj.school='sshhss'                                 
print(obj.school)                                  
print(obj.school)                                  #call
print(obj.n,obj.r,obj.c)                           #call
