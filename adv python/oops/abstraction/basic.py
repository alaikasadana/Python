from abc import ABC ,abstractmethod
class Calculator(ABC):
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)

    @abstractmethod
    def div(self,a,b):
        print(a/b)

class Junior(Calculator):
    def div(self,a,b):
        print(a/b)

obj=Junior()
obj.add(20,10)
obj.sub(30,20)
obj.mul(30,90)
obj.div(40,2)