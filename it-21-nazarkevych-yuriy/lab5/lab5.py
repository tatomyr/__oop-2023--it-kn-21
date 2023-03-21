class vehicle:
    def __init__(self, name, kind, color, price):
        self.name = name
        self.kind = kind
        self.color = color
        self.price = price

    def desc(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.price)
        return desc_str

car1 = vehicle("Lada Priora", "sportcar", "cherry", 666000)
car2 = vehicle("Skoda Fabia", "monstertruck", "black", 99999999)

print(car1.desc())
print(car2.desc())