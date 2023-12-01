from abc import ABC, abstractmethod 
 
# Payment Strategy Interface 
class PaymentStrategy(ABC): 
    @abstractmethod 
    def make_payment(self, amount): 
        pass 
 
# Concrete Payment Strategy Classes 
class CreditCardPayment(PaymentStrategy): 
    def make_payment(self, amount): 
        print(f"Paid {amount} dollars by credit card") 
 
class PayPalPayment(PaymentStrategy): 
    def make_payment(self, amount): 
        print(f"Paid {amount} dollars via PayPal") 
 
class CashOnDeliveryPayment(PaymentStrategy): 
    def make_payment(self, amount): 
        print(f"Paid {amount} dollars in cash on delivery") 
 
# Order class with payment strategy selection 
class Order: 
    def __init__(self, payment_strategy): 
        self.payment_strategy = payment_strategy 
 
    def finalize_order(self, amount): 
        self.payment_strategy.make_payment(amount) 
 
# Creating payment strategy objects 
credit_card = CreditCardPayment() 
paypal = PayPalPayment() 
cash_on_delivery = CashOnDeliveryPayment() 
 
# Creating orders and using different payment strategies 
order1 = Order(credit_card) 
order1.finalize_order(1000) 
 
order2 = Order(paypal) 
order2.finalize_order(2000) 
 
order3 = Order(cash_on_delivery) 
order3.finalize_order(1500)
