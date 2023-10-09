from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def create(self):
        pass

class ConcreteProductA(Product):
    def create(self):
        print("Product A created.") 

class ConcreteProductB(Product):
    def create(self):
        print("Product B created.")

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def create_product(self):
        product = self.factory_method()
        product.create()
        return product

class CreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class CreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

creator_a = CreatorA()
product_a = creator_a.create_product()

creator_b = CreatorB()
product_b = creator_b.create_product()
