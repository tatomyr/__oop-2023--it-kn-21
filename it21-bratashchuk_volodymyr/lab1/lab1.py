class Car:
    def __init__(self, model, power):
        self.model = model
        self.power = power
    def get_model(self):
        return self.model
    def get_power(self):
        return self.power
    def set_power(self, power):
        self.power = power
    def __str__(self):
        return "Car's model is " + self.model + ", power is " + str(self.power)
    def human_age(self):
        return self.age * 7
    
car1 = Car("Jaguar", 500)
print(car1)