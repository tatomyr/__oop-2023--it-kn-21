class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.init_singleton()
        return cls._instance

    def init_singleton(self):
        self.some_data = None  # Поля ініціалізуються при створенні єдиного екземпляра
        self.counter = 0

    def increment_counter(self):
        self.counter += 1

    def get_counter(self):
        return self.counter

# Приклад використання Singleton
s1 = Singleton()
s2 = Singleton()

s1.increment_counter()
s1.some_data = "Some data for s1"

s2.increment_counter()
s2.some_data = "Some data for s2"

print(s1 is s2)  # Виведе True, оскільки це один і той же екземпляр

print("Counter for s1:", s1.get_counter())  # Виведе 2, оскільки counter збільшили на 1 в обох екземплярах
print("Counter for s2:", s2.get_counter())  # Виведе 2

print("Data for s1:", s1.some_data)  # Виведе "Some data for s2", оскільки s1.some_data було перезаписано
print("Data for s2:", s2.some_data)  # Виведе "Some data for s2"
