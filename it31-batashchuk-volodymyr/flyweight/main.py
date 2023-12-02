class SoldierType:
    """ Flyweight class representing soldier types. """
    def __init__(self, unit_type, weapon, armor):
        self.unit_type = unit_type
        self.weapon = weapon
        self.armor = armor

    def display_info(self):
        return f"{self.unit_type} equipped with {self.weapon} and {self.armor} armor"

class SoldierTypeFactory:
    """ Factory to manage SoldierType flyweights. """
    _types = {}

    @staticmethod
    def get_soldier_type(unit_type, weapon, armor):
        key = (unit_type, weapon, armor)
        if key not in SoldierTypeFactory._types:
            SoldierTypeFactory._types[key] = SoldierType(unit_type, weapon, armor)
        return SoldierTypeFactory._types[key]

class Soldier:
    """ Represents an individual soldier. """
    def __init__(self, x, y, health, soldier_type):
        self.x = x
        self.y = y
        self.health = health
        self.soldier_type = soldier_type

    def display(self):
        return f"Soldier at ({self.x}, {self.y}), Health: {self.health}, Type: {self.soldier_type.display_info()}"

# Client code
if __name__ == "__main__":
    infantry_type = SoldierTypeFactory.get_soldier_type("Infantry", "Rifle", "Light")
    sniper_type = SoldierTypeFactory.get_soldier_type("Sniper", "Sniper Rifle", "Stealth")

    soldier1 = Soldier(10, 10, 100, infantry_type)
    soldier2 = Soldier(20, 15, 100, sniper_type)
    soldier3 = Soldier(11, 12, 100, infantry_type)  # Reuses the same Infantry SoldierType instance

    print(soldier1.display())
    print(soldier2.display())
    print(soldier3.display())
