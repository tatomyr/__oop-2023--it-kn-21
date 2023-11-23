from batch import *
from inventory import Inventory


class UI():
    def __init__(self) -> None:
        self.inventory = Inventory()


    # Функція для виводу меню і отримання вибору користувача
    def display_menu(self):
        print("\nМеню:")
        print("1. Добавити партію")
        print("2. Показати інвентар")
        print("3. Продати добриво")
        print("4. Вийти")
        return input("Виберіть варіант (1-4): ")
    
    def run(self):
        while True:
            choice = self.display_menu()

            if choice == "1":
                name = input("Введіть назву мінерального добрива: ")
                expiration_date = datetime.strptime(input("Введіть кінцеву дату зберігання (DD-MM-YYYY): "), '%d-%m-%Y')
                quantity = float(input("Введіть кількість (kg): "))
                batch_number = input("Введіть номер партії: ")

                batch = Batch(name, expiration_date, quantity, batch_number)
                self.inventory.add_batch(batch)
                print("Партія успішно додано.")

            elif choice == "2":
                self.inventory.display_inventory()

            elif choice == "3":
                batch_number = input("Введіть номер партії для продажу: ")
                quantity_sold = float(input("Введіть кількість, яку плануєте продати (kg): "))
                sale_date = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")

                for batch in self.inventory.batches:
                    if batch.batch_number == batch_number:
                        self.inventory.sell_fertilizer(batch, quantity_sold, sale_date)
                        break
                else:
                    print("Партія не знайдена.")

            elif choice == "4":
                print("Завершення програми.")
                break

            else:
                print("Неправильний вибір. Виберіть між 1-4.")