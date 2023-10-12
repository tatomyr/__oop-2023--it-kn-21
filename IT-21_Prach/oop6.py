class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.calculate_area()
        
    def calculate_area(self):
        return self.width * self.height
    
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        self.area = self.calculate_area()
rectangle = Rectangle(4, 6)
print(rectangle.width)   # Виводить: 4
print(rectangle.height)  # Виводить: 6
print(rectangle.area)    # Виводить: 24

rectangle.resize(8, 10)
print(rectangle.width)   # Виводить: 8
print(rectangle.height)  # Виводить: 10
print(rectangle.area)    # Виводить: 80

