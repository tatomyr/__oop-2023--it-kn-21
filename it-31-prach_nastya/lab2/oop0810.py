# Клас, який має метод, який ми хочемо використовувати
class OldSystem:
    def do_old_operation(self):
        print("Виконуємо операцію старої системи")

# Клас, який має інший метод, який також потрібно використовувати
class NewSystem:
    def do_new_operation(self):
        print("Виконуємо операцію нової системи")

# Адаптер для старої системи
class OldSystemAdapter:
    def __init__(self, old_system):
        self.old_system = old_system
    
    def do_operation(self):
        self.old_system.do_old_operation()

# Адаптер для нової системи
class NewSystemAdapter:
    def __init__(self, new_system):
        self.new_system = new_system
    
    def do_operation(self):
        self.new_system.do_new_operation()

# Функція для виконання операції через інтерфейс
def execute_operation(system_adapter):
    system_adapter.do_operation()

# Використання адаптерів для обох систем
old_system = OldSystem()
new_system = NewSystem()

old_adapter = OldSystemAdapter(old_system)
new_adapter = NewSystemAdapter(new_system)

# Виконуємо операцію через адаптери
execute_operation(old_adapter)  # Виконуємо операцію старої системи
execute_operation(new_adapter)  # Виконуємо операцію нової системи
