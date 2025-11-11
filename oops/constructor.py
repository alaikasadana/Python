# class Student:
#     pass

# print(id(Student))

# obj1 = Student
# print(id(obj1))

# obj2 = Student()
# print(id(obj2))

#=================================================================
#External Constructor 
#kisi object ka initial value ko provide krne ke liye 
#self refrence variable 

class Student:
    school='SHS'
    def __init__(self):
        print("Constructor called")
        print(id(self))
print(id(Student))
obj = Student()
print(id(obj))
obj1 = Student()
print(id(obj1))