class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name + "!")
obj = MyClass("John")
obj.say_hello() # Виведе "Hello, John!"
