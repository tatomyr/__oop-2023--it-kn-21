from retail_sale import RetailSale
from database import Database

class Inventory:
    def __init__(self):
        self.db = Database()
        self.batches = self.db.load_batches()
        self.sales = self.db.load_sales()
        

    def add_batch(self, batch):
        self.batches.append(batch)
        self.db.add_batch(batch)

    def sell_fertilizer(self, batch, quantity_sold, sale_date):
        if batch.quantity >= quantity_sold:
            batch.quantity -= quantity_sold
            sale = RetailSale(batch, quantity_sold, sale_date)
            self.db.register_sale(batch, quantity_sold, sale_date)
            self.sales.append(sale)
            print(f"{quantity_sold} kg {batch.name} успішно продано.")
        else:
            print("Не достатньо добрива для продажі.")

    def display_inventory(self):
        print("Теперешній інвентар:")
        for batch in self.batches:
            batch.display_info()

        print("\nПродажі:")
        for sale in self.sales:
            sale.display_sale_info()