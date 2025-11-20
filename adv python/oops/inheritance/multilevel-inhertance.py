
#========================================================================================
#=====================multi-level Inheritance============================================
class GrandParent:
    car="thar"
    def home(self):
        print("home from grandparent")
class Parent(GrandParent):
    bank="ICIC"
    def land(self):
        print("land from parent")
class Child(Parent):
    pass

obj=Child()
print(obj.car,obj.bank)
obj.home()
obj.land()