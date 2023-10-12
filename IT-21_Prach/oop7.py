class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    @classmethod
    def square(cls, side):
        return cls(side, side)
    
    @staticmethod
    def is_large(rect, limit):
        return rect.area() > limit
r1 = Rectangle(5, 10)
r2 = Rectangle(3, 6)
r3 = Rectangle.square(7)

print(Rectangle.is_large(r1, 40))  # True
print(Rectangle.is_large(r2, 10))  # True
print(Rectangle.is_large(r3, 40))  # True
