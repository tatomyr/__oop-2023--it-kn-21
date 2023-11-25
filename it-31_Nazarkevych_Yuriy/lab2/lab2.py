# Базовий клас компоненту
class Coffee:
    def cost(self):
        return 5

# Конкретний компонент
class SimpleCoffee(Coffee):
    pass

# Декоратор
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._decorated_coffee = coffee

    def cost(self):
        return self._decorated_coffee.cost()

# Конкретні декоратори
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._decorated_coffee.cost() + 2

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._decorated_coffee.cost() + 1

# Приклад використання
coffee = SimpleCoffee()
print("Cost of Simple Coffee:", coffee.cost())

milk_coffee = MilkDecorator(coffee)
print("Cost of Coffee with Milk:", milk_coffee.cost())

sugar_milk_coffee = SugarDecorator(milk_coffee)
print("Cost of Coffee with Milk and Sugar:", sugar_milk_coffee.cost())
