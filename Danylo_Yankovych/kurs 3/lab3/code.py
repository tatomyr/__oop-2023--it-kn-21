
class Shape:
    def accept(self, visitor):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def accept(self, visitor):
        visitor.visit_square(self)

class Visitor:
    def visit_circle(self, circle):
        pass

    def visit_square(self, square):
        pass

class AreaPerimeterVisitor(Visitor):
    def visit_circle(self, circle):
        area = 3.14 * circle.radius**2
        perimeter = 2 * 3.14 * circle.radius
        print(f"Circle - Area: {area}, Perimeter: {perimeter}")

    def visit_square(self, square):
        area = square.side_length ** 2
        perimeter = 4 * square.side_length
        print(f"Square - Area: {area}, Perimeter: {perimeter}")

if __name__ == "__main__":
    circle = Circle(5)
    square = Square(4)

    visitor = AreaPerimeterVisitor()

    circle.accept(visitor)
    square.accept(visitor)
