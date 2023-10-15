class Hero:
    _hero_instance = None

    def __new__(cls):
        if cls._hero_instance is None:
            cls._hero_instance = super(Hero, cls).__new__(cls)
            cls._hero_instance.initialize_hero()
        return cls._hero_instance

    def initialize_hero(self):
        self.name = None
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1
        self.health += 10

    def set_name(self, name):
        self.name = name

    def get_status(self):
        return f"{self.name} (Level {self.level}) - Health: {self.health}"

# Приклад використання Singleton
hero1 = Hero()
hero2 = Hero()

hero1.set_name("Warrior")
hero1.level_up()

hero2.set_name("Mage")
hero2.level_up()
hero2.level_up()

print(hero1 is hero2)  # Виведе True, оскільки це один і той же герой

print("Hero 1:", hero1.get_status())  # Виведе "Warrior (Level 2) - Health: 110"
print("Hero 2:", hero2.get_status())  # Виведе "Mage (Level 3) - Health: 120"
