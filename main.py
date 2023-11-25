class BearPrototype:
    def __init__(self, name, color, bag_type):
        self.name = name
        self.color = color
        self.bag_type = bag_type

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.color} ведмідь {self.name} з мішечком для {self.bag_type}"

brown_bear = BearPrototype("Брауні", "Коричневий", "мед")

white_bear = brown_bear.clone()
white_bear.name = "Сніжок"
white_bear.color = "Білий"
white_bear.bag_type = "риба"

polar_bear = brown_bear.clone()
polar_bear.name = "Полярник"
polar_bear.color = "Білий"
polar_bear.bag_type = "сала"

print(brown_bear)
print(white_bear)
print(polar_bear)


# class Prototype:
#     def __init__(self):
#         self._data = {}

#     def set_data(self, key, value):
#         self._data[key] = value

#     def get_data(self, key):
#         return self._data.get(key)

#     def clone(self):
#         # Використовуємо глибоку копію для клонування об'єкта
#         return copy.deepcopy(self)

# # Створення початкового об'єкта-прототипу
# prototype = Prototype()
# prototype.set_data("name", "Прототип")
# prototype.set_data("version", "1.0")

# # Клонування об'єкта
# clone = prototype.clone()
# # Перевірка клонованого об'єкта
# print(clone.get_data("name"))  # Виведе "Прототип"
# print(clone.get_data("version"))  # Виведе "1.0"




