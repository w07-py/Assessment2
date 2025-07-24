from main import slow_print
from enum import Enum

class Outfit:
    def __init__(self, name: str, description: str, surprise = None):
        self.name = name 
        self.description = description
        self.surprise = surprise

    def outfit_details(self):
        slow_print("Your Cloak: " + self.name)
        slow_print("Have a look " + self.description)

class ObtainMethod(Enum):
    STORE = "Store"
    BOSS_DROP = "Boss Drop"
    QUEST = "Quest"
    
class Item:
    def __init__(self, name: str, weight: int, description: str, effect = None ):
        self.name = name
        self.weight = weight
        self.description = description
        self.effect = effect

    def display_info(self):
        slow_print(f"Name: {self.name}")
        slow_print(f"Weight: {self.weight}")
        slow_print(f"Description: {self.description}")
        slow_print(f"Effect: {self.effect}")
    
    def describe(self):
        slow_print(f"{self.name} - {self.description}")
        if self.effect:
            slow_print(f"Effect: {self.effect}")

class Key(Item):
    COUNTRIES = ['india', 'british', 'egypt', 'japan', 'china']

    def __init__(self, country: str, half_key: bool = False):
        self.country = country
        self.half = half_key

        super().__init__(
            name = self._get_name(),
            weight = 1,
            description = self._get_description(),
            effect = "Can open corresponding locks"
    )

    def _get_name(self):
        if self.half:
            return "Half " + self.country.capitalize() + " Key"
        else:
            return self.country.capitalize() + "Key"
        
    def _get_description(self):
        return "Dropped from " + self.country.capitalize() + " boss"
    
class Weapon(Item):
    def __init__(self, name: str, damage: int, description: str, effect: str, weight: float = 2):
        self.damage = damage
        super().__init__(name, weight, description, effect)

class Armor(Item):
    def __init__(self, name: str, defense: int, description: str, effect: str, weight: float = 3):
        self.defense = defense
        super().__init__(name, weight, description, effect)

class Potion(Item):
    def __init__(self, name: str, potion_type: str, amount: int, description: str, effect: str, weight: float = 1):
        self.potion_type = potion_type
        self.amount = amount
        super().__init__(name, weight, description, effect)

class Special(Item):
    def __init__(self, name: str, description: str, effect: str, weight: float = 1):
        super().__init__(name, weight, description, effect)
