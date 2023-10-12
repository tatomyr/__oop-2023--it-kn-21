class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __repr__(self):
        return f'Rectangle({self.width}, {self.height}) with area {self.calculate_area()}'
    
    def calculate_area(self):
        return self.width * self.height
    
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
rectangle = Rectangle(4, 6)
print(rectangle)  # Виводить: Rectangle(4, 6) with area 24
