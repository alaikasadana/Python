#method resolution order :MRO (depth first)

# class Father:
#     def home(self):
#         print("home from Father")
# class Mother:
#     def car(self):
#         print("thar")
#     def home(self):
#         print("home from Mother")
       
# class Child(Mother,Father):
#     pass

# obj=Child()
# obj.car()
# obj.home()

#=========================================================================================

# class Father:
#     def home(self):
#         print("home from Father")
# class Mother:
#     def car(self):
#         print("thar")
#     def home(self):
#         print("home from Mother")
#         Father.home(self)
# class Child(Mother,Father):
#     pass

# obj=Child()
# obj.car()
# obj.home()

#==============================================================================================

class Father:
    def home(self):
        print("home from Father")
        Mother.home(self)
class Mother:
    def car(self):
        print("thar")
    def home(self):
        print("home from Mother")
        
class Child(Father,Mother):
    pass

obj=Child()
obj.car()
obj.home()

 