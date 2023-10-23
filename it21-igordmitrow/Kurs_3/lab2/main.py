# Реалізація абстракції
class Shape:
    def __init__(self, color):
        self.color = color

    def apply_color(self):
        pass

# Реалізація конкретної абстракції
class Circle(Shape):
    def apply_color(self):
        return f"Circle colored with {self.color}"

class Square(Shape):
    def apply_color(self):
        return f"Square colored with {self.color}"

# Реалізація інтерфейсу для реалізації
class Color:
    def fill_color(self):
        pass

class RedColor(Color):
    def fill_color(self):
        return "Red"

class GreenColor(Color):
    def fill_color(self):
        return "Green"

# Використання паттерна "Міст"
red_color = RedColor()
green_color = GreenColor()

circle = Circle(red_color)
square = Square(green_color)

print(circle.apply_color())  # Виведе "Circle colored with Red"
print(square.apply_color())  # Виведе "Square colored with Green"
