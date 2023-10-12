import copy

# Клас, який використовує паттерн прототипу
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def clone(self):
        # Використовуємо бібліотеку copy для створення глибокої копії об'єкта
        return copy.deepcopy(self)

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Major: {self.major}"

# Створення об'єкта-прототипу
prototype_student = Student("John", 20, "Computer Science")

# Створення копії об'єкта на основі прототипу
student1 = prototype_student.clone()
student1.name = "Alice"
student1.age = 22

student2 = prototype_student.clone()
student2.name = "Bob"
student2.major = "Mathematics"

# Виведення результатів
print(student1)
print(student2)