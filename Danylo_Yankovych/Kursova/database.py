import sqlite3
from batch import Batch
from retail_sale import RetailSale
from datetime import datetime

class Database:
    def __init__(self):
        self.create_tables()        

    
    def create_tables(self):
        connection = sqlite3.connect('inventory.db')
        c = connection.cursor()
        c.execute('''
                CREATE TABLE IF NOT EXISTS batches 
                (id INTEGER PRIMARY KEY, name TEXT, expiration_date TEXT, 
                quantity REAL, batch_number TEXT)
                ''')

        c.execute('''
                CREATE TABLE IF NOT EXISTS sales
                (id INTEGER PRIMARY KEY, batch_id INTEGER, quantity_sold REAL, 
                sale_date TEXT, FOREIGN KEY(batch_id) REFERENCES batches(id))
                ''')

        connection.commit()

    def post_sql_query(func):
        def wrapper(*args, **kwargs):
            with sqlite3.connect('inventory.db') as connection:
                cursor = connection.cursor()
            
                try:
                    res = func(*(args + (cursor,)), **kwargs)
                    return res  
                except Exception as ex:
                    print(ex)
                result = cursor.fetchall()
                return result
        return wrapper
          
    @post_sql_query
    def add_batch(self, batch, c):
        c.execute("INSERT INTO batches (name, expiration_date, quantity, batch_number) VALUES (?, ?, ?, ?)", (batch.name, batch.expiration_date, batch.quantity, batch.batch_number))
        
    @post_sql_query
    def register_sale(self, batch, quantity_sold, sale_date, c):  
        c.execute("INSERT INTO sales (batch_id, quantity_sold, sale_date) VALUES (?, ?, ?)", (batch.batch_number, quantity_sold, sale_date))
          
        c.execute("UPDATE batches SET quantity= quantity - ? WHERE batch_number=?", (quantity_sold, batch.batch_number))
    
    @post_sql_query
    def load_batches(self, c):
        c.execute("SELECT * FROM batches")
        
        batches = []
        for row in c:
            batch = Batch(row[1], datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S"), row[3], row[4]) 
            batches.append(batch)
        return batches

    @post_sql_query
    def get_batch_by_id(self, bid, c):
        c.execute("SELECT * FROM batches WHERE batch_number=?", (bid,))
        row = c.fetchone()
        batch = Batch(row[1], datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S"), row[3], row[4]) 

        return batch
    
    @post_sql_query
    def load_sales(self, c):
        c.execute("SELECT * FROM sales")
        
        sales = [] 
        for row in c:
            batch = self.get_batch_by_id(row[1])
            sale = RetailSale(batch, row[2], datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S"))
            sales.append(sale)
        return sales