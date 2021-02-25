import math

class Point:
    def __init__(self, x, y): # this is the initializer
        self.x = x # these are member variables
        self.y = y
    
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    
p1 = Point(5, 2) # call the initializer, instantiate the class
p2 = Point(8, 4)
print(p1.x) # 5
print(p1.y) # 2
print(p2.x)
print(p2.y)
# print(type(p1)) # Point
print(p1.distance(p2))
print(p2.distance(p1))