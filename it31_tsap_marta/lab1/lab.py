class Singleton:
    _instance = None  # Приватне статичне поле, що містить одинака

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("This class is a singleton. Use get_instance() method to obtain an instance.")
        self.some_data = None

# Приклад використання
singleton1 = Singleton.get_instance()
singleton1.some_data = "Data from singleton1"

singleton2 = Singleton.get_instance()
print(singleton2.some_data)  # Виведе "Data from singleton1"

# Спроба створити новий екземпляр через конструктор призведе до помилки
# singleton3 = Singleton()  # Помилка: This class is a singleton...