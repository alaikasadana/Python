#Q.2 Create a class Circle with attribute radius and methods:
# area() → calculate circle area
# circumference() → calculate circle circumference

import math
class Circle:
    def __init__(self , radius):
        self.r = radius
    
    def area(self):
        return math.pi * self.r *self.r
    
    def circumfrence(self):
        return 2* math.pi * self.r
    
obj = Circle(5)
print(f' AREA: {obj.area()}')
print(f'CIRCUMFRENCE : {obj.circumfrence()}')
