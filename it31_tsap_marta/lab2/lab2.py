# Базовий клас Coffee
class Coffee:
    def cost(self):
        return 5  # Вартість базової кави

# Декоратор для молока
class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2  # Додаємо вартість молока

# Декоратор для цукру
class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1  # Додаємо вартість цукру

# Приклад використання:
coffee = Coffee()
print("Базова кава:", coffee.cost())

coffee_with_milk = MilkDecorator(coffee)
print("Кава з молоком:", coffee_with_milk.cost())

coffee_with_sugar = SugarDecorator(coffee)
print("Кава з цукром:", coffee_with_sugar.cost())

coffee_with_milk_and_sugar = SugarDecorator(MilkDecorator(coffee))
print("Кава з молоком і цукром:", coffee_with_milk_and_sugar.cost())
