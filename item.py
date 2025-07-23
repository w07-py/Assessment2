from enum import Enum

class Outfit:
    def __init__(self, name: str, description: str, surprise = None):
        self.name = name 
        self.description = description
        self.surprise = surprise

    def outfit_details(self):
        print("Your Cloak: " + self.name)
        print("Have a look " + self.description)

class ObtainMethod(Enum):
    STORE = "Store"
    BOSS_DROP = "Boss Drop"
    QUEST = "Quest"
    
class Item:
    def __init__(self, name: str, weight: int, description: str, obtain_method: ObtainMethod, effect = None ):
        self.name = name
        self.weight = weight
        self.description = description
        self.obtain_method = obtain_method
        self.effect = effect

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Weight: {self.weight}")
        print(f"Description: {self.description}")
        print(f"Effect: {self.effect}")
    
    def describe(self):
        print(f"{self.name} - {self.description}")
        if self.effect:
            print(f"Effect: {self.effect}")

class Key(Item):
    COUNTRIES = ['india', 'british', 'egypt', 'japan', 'china']

    def __init__(self, country: str, half_key: bool = False):
        self.country = country
        self.half = half_key

        super().__init__(
            name = self._get_name(),
            weight = 1,
            description = self._get_description(),
            obtain_method = ObtainMethod.BOSS_DROP,
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
    def __init__(self, name: str, damage: int, description: str, effect: str, weight: float = 2, obtain_method: ObtainMethod = ObtainMethod.BOSS_DROP):
        self.damage = damage
        super().__init__(name, weight, description, obtain_method, effect)

class Armor(Item):
    def __init__(self, name: str, defense: int, description: str, effect: str, weight: float = 3, obtain_method: ObtainMethod = ObtainMethod.STORE):
        self.defense = defense
        super().__init__(name, weight, description, obtain_method, effect)

class Potion(Item):
    def __init__(self, name: str, potion_type: str, amount: int, description: str, effect: str, weight: float = 1, obtain_method: ObtainMethod = ObtainMethod.STORE):
        self.potion_type = potion_type
        self.amount = amount
        super().__init__(name, weight, description, obtain_method, effect)

class Special(Item):
    def __init__(self, name: str, description: str, effect: str, weight: float = 1, obtain_method: ObtainMethod = ObtainMethod.QUEST):
        super().__init__(name, weight, description, obtain_method, effect)
