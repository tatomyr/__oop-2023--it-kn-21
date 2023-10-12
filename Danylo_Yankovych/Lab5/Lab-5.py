class Car:
    def __init__(self, name, kind, color, price):
        self.name = name
        self.kind = kind
        self.color = color
        self.price = price

    def desc(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.price)
        return desc_str

car1 = Car("Formula 1", "sportcar", "red", 12000000)
car2 = Car("Tesla model S", "electrocar", "white", 89000)

print(car1.desc())
print(car2.desc())