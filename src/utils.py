from collections import namedtuple

BarycentricPoint = namedtuple("Bary", ["alpha", "beta", "gamma"])

class Vector:
    def __init__(self, x: int, y: int) -> None:
          self.x = x
          self.y = y
    
    def add(self, v: "Vector") -> "Vector":
          return Vector(self.x + v.x, self.y + v.y)

    def subtract(self, v: "Vector") -> "Vector":
         return Vector(self.x - v.x, self.y, v.y)  
    
    def scale(self, v: float) -> "Vector":
         return Vector(self.x * v, self.y * v)

class Vertex(Vector):
     def __init__(self, x:int, y:int, r:int, g:int, b:int) -> None:
          super().__init__(x, y)
          self.red = r
          self.blue = b
          self.green = g