# Клас, що представляє об'єкт, який ми будуємо
class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Вигляд готового об'єкта:")
        for part in self.parts:
            print(part)


# Абстрактний клас будівельника
class Builder:
    def build_part1(self):
        pass

    def build_part2(self):
        pass

    def get_result(self):
        pass


# Конкретний будівельник
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part1(self):
        self.product.add("Частина 1")

    def build_part2(self):
        self.product.add("Частина 2")

    def get_result(self):
        return self.product


# Керівник будівництва
class Director:
    def __init__(self):
        self.builder = None

    def construct(self):
        self.builder.build_part1()
        self.builder.build_part2()

    def set_builder(self, builder):
        self.builder = builder


if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder()

    director.set_builder(builder)
    director.construct()

    product = builder.get_result()
    product.show()
