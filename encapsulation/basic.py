#=============================Public==================================================
# class Parent:
#     bank="HDFC"
#     def add(self):
#         print("HEllow")
# class Child(Parent):
#     pass

# obj=Child()
# print(obj.bank)
# obj.add()


#========================PROTECTED (python not supported)============================
# class Parent:
#     _bank="HDFC"
#     def _add(self):
#         print("HEllow")
# class Child(Parent):
#     pass

# obj=Child()
# print(obj._bank)
# obj._add()


#=======================================Private====================================
class Parent:
    __bank="HDFC"
    def __add(self):
        print("HEllow")
class Child(Parent):
    pass

obj=Child()
print(dir(Parent))
obj._Parent__add()
print(obj._Parent__bank)

