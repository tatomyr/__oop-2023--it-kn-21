import copy

class Prototype:
    def clone(self):
        pass

class ConcretePrototype1(Prototype):
    def __init__(self, value):
        self._value = value

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"ConcretePrototype1 with value: {self._value}"

class ConcretePrototype2(Prototype):
    def __init__(self, name):
        self._name = name

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"ConcretePrototype2 with name: {self._name}"

prototype1 = ConcretePrototype1(10)
clone1 = prototype1.clone()
print(clone1)  

prototype2 = ConcretePrototype2("Prototype2")
clone2 = prototype2.clone()
print(clone2)  