from abc import ABC, abstractmethod

# Інтерфейс спостерігача
class Observer(ABC):
    @abstractmethod
    def update(self, sport):
        pass

# Інтерфейс суб'єкта
class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, sport):
        for observer in self._observers:
            observer.update(sport)

# Конкретний суб'єкт (спортивний журнал)
class SportMagazine(Subject):
    def add_sport(self, sport):
        print(f"Додано новий вид спорту: {sport}")
        self.notify(sport)

# Конкретний спостерігач (підписник)
class Subscriber(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, sport):
        print(f"{self._name} отримав оновлення про новий вид спорту: {sport}")

# Створюємо об'єкти
magazine = SportMagazine()
subscriber1 = Subscriber("Петро")
subscriber2 = Subscriber("Марія")

# Підписуємо підписників на журнал
magazine.attach(subscriber1)
magazine.attach(subscriber2)

# Додаємо новий вид спорту до журналу
magazine.add_sport("Футбол")
