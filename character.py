from main import slow_print
import random
from item import Item
from typing import Optional, List

class Player:
    def __init__(self, player_name, appearance, ATK = 10, player_health = 100, bag_capacity = 50):
        self.player_name = player_name
        self.appearance = appearance
        self.player_health = player_health
        self.bag_capacity = bag_capacity
        self.bag_items: List[Item] = []
        self.ATK = ATK
        self.gold = 150

    def id_card(self):
        slow_print("\n=== PLAYER STATUS ===")
        slow_print("Name:", self.player_name)
        slow_print("Appearance:", self.appearance)
        slow_print("Health:", self.player_health)
        slow_print("Attack:", self.ATK)
        slow_print("Gold:", self.gold)
        slow_print("=" * 20)

    def bag(self):
        total_weight = sum(item.weight for item in self.bag_items)
        remaining = self.bag_capacity - total_weight
        slow_print(f"Your bag capacity is {self.bag_capacity}.")
        slow_print(f"You have {total_weight} units of weight in your bag.")
        slow_print(f"You have {remaining} capacity left")
        if remaining == 0:
            slow_print("Your bag is FULL!")
        if self.bag_items:
            slow_print("The items in your bag:")
            for item in self.bag_items:
                slow_print(f" - {item.name} (Weight: {item.weight})")
        else:
            slow_print("Your bag is empty, pick something up!")
        
    def pick_up(self, item: Item):
        current_weight = sum(item.weight for item in self.bag_items)
        remaining_capacity = self.bag_capacity - current_weight
        if item.weight <= remaining_capacity:
            self.bag_items.append(item)
            slow_print(f"You picked up: {item.name} (weight: {item.weight})")
            slow_print(f"Bag:{current_weight + item.weight}/{self.bag_capacity}")
            return True
        else:
            slow_print(f"You don't have enough capacity to pick up {item.name}. You need {item.weight - remaining_capacity} more capacity.")
            return False
        
    def drop(self, item_name: str):
        for index, item in enumerate(self.bag_items):
            if item.name.lower() == item_name.lower():
                dropped_item = self.bag_items.pop(index)
                slow_print(f"You dropped: {dropped_item.name} (Weight: {dropped_item.weight})")
                current_weight = sum(i.weight for i in self.bag_items)
                slow_print(f"Bag: {current_weight} / {self.bag_capacity}")
                return dropped_item
        slow_print(f"Item '{item_name}' not found in your bag.")
        return None

    def fight(self, enemy: "Boss", weapon: str):
        weapon_item = None
        for item in self.bag_items:
            if hasattr(item, 'damage') and item.name.lower() == weapon.lower():
                weapon_item = item
                break
        if weapon_item is None:
            slow_print(f"You don't have weapon in your bag!")
            return None
        
        common_damage = weapon_item.damage + self.ATK

        if weapon.lower() == enemy.weakness.lower():
            damage = int(common_damage * 2)
            slow_print(f"Critical hit! {weapon} is effective against {enemy.char_name}")
        else:
            damage = common_damage + random.randint(-5, 10)
            damage = max(1, damage)

        enemy.health -= damage
        slow_print(f"You attack {enemy.char_name} successfully with {weapon} for {damage} damage.")
        slow_print(f"{enemy.char_name} has {enemy.health} health remaining.")

        if enemy.health > 0:
            boss_damage = random.randint(1, enemy.ATK)
            self.player_health -= boss_damage
            slow_print(f"{enemy.char_name} hits you for {boss_damage} damage!")

            if self.player_health <= 0:
                slow_print(f"{self.player_name}, you have been defeated!")
                return False
            elif self.player_health < 30:
                slow_print(f"{self.player_name}, critical health! Be careful!")
            elif self.player_health < 70:
                slow_print(f"{self.player_name}, you will be fine, keep fighting!")
            else:
                slow_print(f"{self.player_name}, you're still very strong!")
            
            slow_print(f"Your health: {self.player_health}")
            return None
         
        else:
            slow_print(f"\n Congraduation! You defeated {enemy.char_name}!")

            if hasattr(enemy, "drop_loot") and enemy.loot:
                loot = enemy.drop_loot()
                if loot:
                    slow_print(f"\n{enemy.char_name} dropped:")
                    for item in loot:
                        slow_print(f" - {item.name}")
                        if self.pick_up(item):
                            continue
                        else:
                            slow_print(f"You don't have enough space!")
            return True

class Character():
    def __init__(self, char_name: str, char_description: str):
        self.char_name: str = char_name
        self.char_description: str = char_description
        self.conversation: Optional[str] = None

    def describe(self):
        slow_print("This is " + self.char_name)
        slow_print(self.char_description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            slow_print("[" + self.char_name + " says]: " + self.conversation)
        else:
            slow_print(self.char_name + " has nothing to say.")

    def fight(self, combat_item):
        slow_print(self.char_name + " is friendly and does not want to fight with you.")
        return True

class Boss(Character):
    def __init__(
            self, 
            char_name: str, 
            char_description: str, 
            health: int = 0, 
            skill: Optional[str] = None, 
            weakness: Optional[str] = None, 
            ATK: Optional[int] = None,
            loot: Optional[list] = None
    ):
        super().__init__(char_name, char_description)
        self.weakness: Optional[str] = weakness
        self.health: int = health
        self.max_health: int = health
        self.skill: Optional[str] = skill
        self.ATK: Optional[int] = ATK
        self.loot = loot if loot else []

    def describe(self):
        super().describe()
        slow_print("Health:", self.health)
        if self.skill:
            slow_print("Special Skill:", self.skill)

    def boss_weakness(self):
        if self.health <= self.max_health / 2:
            slow_print(f"The health of {self.char_name} is lower than 50%!")
            slow_print(f"This is his weakness: {self.weakness}")
        else:
            slow_print(f"{self.char_name} is still strong!")  

    def boss_fight(self, player: Player):
        damage = random.randint(1, self.ATK)
        player.player_health -= damage
        slow_print(f"{self.char_name} attacks you for {damage} damage!")

        if player.player_health <= 0:
            slow_print(f"You have been defeated by {self.char_name}! Don't give up! Try again!")
        
    def drop_loot(self):
        return self.loot
    
