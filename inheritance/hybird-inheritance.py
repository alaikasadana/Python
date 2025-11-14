class Parent:
    def home(self):
        print("Home from parent")
    def car(self):
        print("Car from parent")

class Child1(Parent):
    def bank(self):
        print("ICCI")

class Child2(Parent):
    def land(self):
        print("Land from child-2")
    def bank(self):
        print("ICCI")
        Child1.bank(self)
        
class GrandChild(Child2,Child1):
    pass

obj=GrandChild()
obj.home()
obj.land()
obj.car()
obj.bank()

