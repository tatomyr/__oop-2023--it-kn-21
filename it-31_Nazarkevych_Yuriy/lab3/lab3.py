# Абстрактний клас стратегії
class PaymentStrategy:
    def pay(self, amount):
        pass

# Конкретні класи стратегій
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'Paid {amount} using a credit card.')

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'Paid {amount} using PayPal.')

# Клас, що використовує стратегію
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.cart = {}
        self.payment_strategy = payment_strategy

    def add_item(self, item, price):
        if item in self.cart:
            self.cart[item] += price
        else:
            self.cart[item] = price

    def calculate_total(self):
        return sum(self.cart.values())

    def checkout(self):
        total = self.calculate_total()
        self.payment_strategy.pay(total)

# Приклад використання
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

cart1 = ShoppingCart(credit_card_payment)
cart1.add_item("Item 1", 50)
cart1.add_item("Item 2", 30)
cart1.checkout()  # Виведе "Paid 80 using a credit card."

cart2 = ShoppingCart(paypal_payment)
cart2.add_item("Item 1", 50)
cart2.add_item("Item 2", 30)
cart2.checkout()  # Виведе "Paid 80 using PayPal."
