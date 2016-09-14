import math


class Vec(tuple):
    def __new__(cls, x, y):
        obj = tuple.__new__(Vec, (x, y))
        return obj

    def __add__(self, other):
        return Vec(self[0] + other[0], self[1] + other[1])  
    
    def __sub__(self, other):
        x1, y1 = self
        x2, y2 = other
        return Vec(x1 - x2, y1 - y2)  
            
    def __mul__(self, other):
        x, y = self
        return Vec(other * x, other * y)
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        return self * (1 / other)
    
    def magnitude(self):
        x, y = self
        return math.sqrt(x**2 + y**2)
           
 
