#Q.1 Create a class Person with attributes name and age. Add a method show_details() that prints both.

class Person:
    def __init__(self,name,age):
        self.n = name
        self.g= age
    def show_details(self):
        print(f'Name : {self.n} ')
        print(f'Age  : {self.g} ')

obj = Person("Alaika Sadana" , 20)
obj.show_details()
        
