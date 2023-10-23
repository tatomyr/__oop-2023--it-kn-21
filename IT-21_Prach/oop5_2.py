class MyClass:
    class_variable = "I am a class variable"

MyClass.class_variable = "New value"
class MyClass:
    class_variable = "I am a class variable"

print(MyClass.class_variable) # Виведе "I am a class variable"
