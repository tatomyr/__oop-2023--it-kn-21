class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def from_square(cls, side):
        return cls(side, side)

    @classmethod
    def max_area(cls, rectangles):
        max_area = 0
        max_rectangle = None
        for rectangle in rectangles:
            area = rectangle.width * rectangle.height
            if area > max_area:
                max_area = area
                max_rectangle = rectangle
        return max_rectangle
rect1 = Rectangle(10, 5)
rect2 = Rectangle.from_square(7)
rect3 = Rectangle(8, 12)
rectangles = [rect1, rect2, rect3]

max_rectangle = Rectangle.max_area(rectangles)
print("Rectangle with max area: ", max_rectangle.width, "x", max_rectangle.height)
