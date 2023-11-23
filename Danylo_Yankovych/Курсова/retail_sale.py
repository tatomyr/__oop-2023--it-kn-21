class RetailSale:
    def __init__(self, fertilizer, quantity_sold, sale_date):
        self.fertilizer = fertilizer
        self.quantity_sold = quantity_sold
        self.sale_date = sale_date

    def display_sale_info(self):
        print(f"Дата продажу: {self.sale_date.strftime('%Y-%m-%d')}, {self.quantity_sold} kg продано {self.fertilizer.name}")
