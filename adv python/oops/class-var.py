#class variable
# class Student:
#     clg='RGC'
#     def __init__(self,name,roll):
#         self.n=name
#         self.r=roll

# obj= Student("alaika",101)
# obj1= Student("shaktiman",102)
# obj2= Student("vikkuu",103)
# print(obj.clg,obj1.clg,obj2.clg)

#====================================================================================================
#declaration
# class Student:
#     clg='RGC'                             #class var declaration
#     def __init__(self,name,roll):
#         self.n=name
#         self.r=roll
#         Student.sub="python"                     #class var declaration
#     def addnew(self):
#         Student.course="BCA"                              #class var declaration
#     @classmethod
#     def update_or_create(cls):
#         cls.clg_city="bhopal"                                   #class var declaration

# obj=Student("ALAIKA",121)
# obj.addnew()
# obj.update_or_create()


#===============================================================================================================
#calling


# class Student:
#     school = 'OIS'

#     def __init__(self , name , rollno):
#         self.n = name
#         self.r = rollno
#         print(Student.school)
#         Student.principle = 'Python'

#     def addnew(self):
#         Student.school_code = 1212


#     def show(self):
#         print(Student.school, Student.principle , Student.school_code)


#     @classmethod 
#     def create_or_update(cls):
#         print(Student.school, Student.principle)

# obj = Student('alaika',101)
# obj.addnew()
# obj.show()
# obj.create_or_update()

#=============================================================================================================================
#calling


class Student:
    school = 'OIS'

    def __init__(self , name , rollno):
        self.n = name
        self.r = rollno
        print(Student.school)
        Student.principle = 'Python'

    def addnew(self):
        Student.school_code = 1212


    def show(self):
        print(Student.school, Student.principle , Student.school_code)


    @classmethod 
    def create_or_update(cls):
        cls.course="BCA"
        print(Student.school, Student.principle , Student.school_city)

#call
obj = Student('alaika',101)
obj.addnew()
obj.show()
Student.school_city="bhopal"
obj.create_or_update()
print(Student.school , Student.principle , Student.school_city , Student.course)