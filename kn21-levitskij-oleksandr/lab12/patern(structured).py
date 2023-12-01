# Клас, який представляє мобільний телефон
class Phone:
    def charge(self, charger):
        charger.charge_phone(self)

# Клас, який представляє зарядний пристрій для мобільного телефону
class Charger:
    def charge_phone(self, phone):
        print("Заряджаємо телефон")

# Клас, який представляє USB-кабель
class USBCable:
    def connect_to_usb_port(self):
        print("Підключено до USB-порту")

# Адаптер, який дозволяє використовувати USB-кабель як зарядний пристрій
class Adapter(Charger):
    def __init__(self, usb_cable):
        self.usb_cable = usb_cable

    def charge_phone(self, phone):
        self.usb_cable.connect_to_usb_port()
        print("Заряджаємо телефон через USB-кабель")

# Створення об'єктів
phone = Phone()
usb_cable = USBCable()
adapter = Adapter(usb_cable)

# Заряджаємо телефон за допомогою адаптера
phone.charge(adapter)

