class Animal:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Animal.count += 1
    
    def get_name(self):
        return self.name
    
    @staticmethod
    def get_count():
        return Animal.count
cat = Animal('Кіт')
dog = Animal('Собака')
bird = Animal('Птах')

print(cat.get_name())  # виведе "Кіт"
print(Animal.get_count())  # виведе 3
