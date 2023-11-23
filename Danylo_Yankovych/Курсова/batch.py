from datetime import datetime


class MineralFertilizer:
    def __init__(self, name, expiration_date, quantity):
        self.name = name
        self.expiration_date = expiration_date
        self.quantity = quantity

    def is_expired(self):
        return datetime.now() > self.expiration_date

    def display_info(self):
        print(f"{self.name}: {self.quantity} kg, Використати до: {self.expiration_date.strftime('%Y-%m-%d')}, Номер партії: {self.batch_number}")

class Batch(MineralFertilizer):
    def __init__(self, name, expiration_date, quantity, batch_number):
        super().__init__(name, expiration_date, quantity)
        self.batch_number = batch_number
