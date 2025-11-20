#Inheritance syntax

#=====================Single-level Inheritance===========================================
# class Parent:
#     city="bhopal"
#     def show(self):
#         print("Car from parent")
# class Child(Parent):
#     pass

# obj=Child()
# print(obj.city)
# obj.show()


#==========single-level (overriding situation)=======================================
# class Parent:
#     car="thar"
#     def home(self):
#         print("home from parent")
# class Child(Parent):
#     car="kia"
#     def home(self):
#         print("home from child")

# obj=Child()
# print(obj.car)
# obj.home()

#==========single-level (overriding solution)=======================================
# class Parent:
#     car="thar"
#     def home(self):
#         print("home from parent")
# class Child(Parent):
#     car="kia"
#     car2=Parent.car   
#     print(car2)                                  #variable override sol
#     def home(self):
#         print(super().car)                       #variable override sol
#         super().home()                           #method override solution
#         print("home from child")

# obj=Child()
# print(obj.car)
# obj.home()


