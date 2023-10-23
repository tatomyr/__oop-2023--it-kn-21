class Animal:
    def speak(self):
        print("Тварина говорить")
a = Animal()
a.speak() # виведе "Тварина говорить"
class Cat(Animal):
    def speak(self):
        print("М'яу")
c = Cat()
c.speak() # виведе "М'яу"
