class Parent:
    def home(self):
        print("Home from parent")
    def car(self):
        print("Car from parent")
class Child1(Parent):
    pass
class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()

obj1.home()
obj1.car()

obj2.home()
obj2.car()