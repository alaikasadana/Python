#Q.3 Create a class Student with a class variable school_name and instance variables name and roll.
# Initialize them in constructor and create a method show() that displays details.

class Student:
    school_name="SHSS"
    def __init__(self , name , rollno):
        self.name = name 
        self.rollno = rollno
    
    def show(self):
        print( f"Name : {self.name}")
        print( f"Roll.No : {self.rollno}")
        print(f"School_name : {Student.school_name}")

obj = Student("alaika" , 101)
obj.show()

