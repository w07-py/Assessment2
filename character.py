import random
from item import Item
from typing import Optional, List

class Player:
    def __init__(self, player_name, appearance, player_skill, ATK = 10, player_health = 100, bag_capacity = 50):
        self.player_name = player_name
        self.appearance = appearance
        self.player_skill = player_skill
        self.player_health = player_health
        self.bag_capacity = bag_capacity
        self.bag_items: List[Item] = []
        self.experience = 0
        self.ATK = ATK

    def id_card(self):
        print("Name:", self.player_name)
        print("Appearance:", self.appearance)
        print("Skill:", self.player_skill)
        print("Health:", self.player_health)
        print("Experience:", self.experience)

    def bag(self):
        total_weight = sum(item.weight for item in self.bag_items)
        remaining = self.bag_capacity - total_weight
        print(f"Your bag capacity is {self.bag_capacity}.")
        print(f"You have {total_weight} units of weight in your bag.")
        print(f"You have {remaining} capacity left")
        if remaining == 0:
            print("Your bag is FULL!")
        if self.bag_items:
            print("The items in your bag:")
            for item in self.bag_items:
                print(f" - {item.name} (Weight: {item.weight})")
        else:
            print("Your bag is empty, pick something up!")
        
    def pick_up(self, item: Item):
        current_weight = sum(item.weight for item in self.bag_items)
        remaining_capacity = self.bag_capacity - current_weight
        if item.weight <= remaining_capacity:
            self.bag_items.append(item)
            print(f"You picked up: {item.name} (weight: {item.weight})")
            print(f"Bag:{current_weight + item.weight}/{self.bag_capacity}")
            return True
        else:
            print(f"You don't have enough capacity to pick up {item.name}. You need {item.weight - remaining_capacity} more capacity.")
            return False
        
    def drop(self, item_name: str):
        for index, item in enumerate(self.bag_items):
            if item.name.lower() == item_name.lower():
                dropped_item = self.bag_items.pop(index)
                print(f"You dropped: {dropped_item.name} (Weight: {dropped_item.weight})")
                current_weight = sum(i.weight for i in self.bag_items)
                print(f"Bag: {current_weight} / {self.bag_capacity}")
                return dropped_item
        print(f"Item '{item_name}' not found in your bag.")
        return None

        
    def amount_health(self, amount):
        self.player_health += amount
        if self.player_health < 0:
            print(f"{self.player_name}, you are killed by the enemy. Game over!")
        elif self.player_health > 0 and self.player_health <30:
            print(f"{self.player_name}, be careful, your health is lower than 30%!")
        elif self.player_health > 30 and self.player_health < 70:
            print(f"{self.player_name}, you are doing well, but be cautious! ")
        else:
            print(f"{self.player_name}, you are in great shape! Keep fighting with them!")

    def fight(self, enemy: "Boss", weapon: str):
        if weapon.lower() == enemy.weakness.lower():
            damage = self.ATK * 2
            print(f"Critical hit! {weapon} is effective against {enemy.char_name}")
        else:
            damage = max(1, self.ATK - random.randint(1, 5))

        enemy.health -= damage
        print(f"You against {enemy.char_name} successfully for {damage} units of health.")

        if enemy.health > 0:
            boss_damage = random.randint(1, enemy.ATK)
            self.player_health -= boss_damage
            print(f"{enemy.char_name} hits you for {boss_damage} damage!")
            self.amount_health(0)

        if enemy.health <= 0:
            print(f"You defeated {enemy.char_name}!")
            if hasattr(enemy, "drop_loot"):
                loot = enemy.drop_loot()
                if loot:
                    print(f"{enemy.char_name} dropped:")
                    for item in loot:
                        print(f" - {item.name}")
                        self.pick_up(item)
            return True
        elif self.player_health <= 0:
            print("You have been defeated." \
                "Don't give up. Try again!")
            return False
        return None

class Character():
    def __init__(self, char_name: str, char_description: str):
        self.char_name: str = char_name
        self.char_description: str = char_description
        self.conversation: Optional[str] = None

    def describe(self):
        print("This is " + self.char_name)
        print(self.char_description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print("[" + self.char_name + " says]: " + self.conversation)
        else:
            print(self.char_name + " has nothing to say.")

    def fight(self, combat_item):
        print(self.char_name + " is friendly and does not want to fight with you.")
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
        print("Health:", self.health)
        if self.skill:
            print("Special Skill:", self.skill)

    def boss_weakness(self):
        if self.health <= self.max_health / 2:
            print(f"The health of {self.char_name} is lower than 50%!")
            print(f"This is his weakness: {self.weakness}")
        else:
            print(f"{self.char_name} is still strong!")  

    def boss_fight(self, player: Player):
        damage = random.randint(1, self.ATK)
        player.player_health -= damage
        print(f"{self.char_name} attacks you for {damage} damage!")

        if player.player_health <= 0:
            print(f"You have been defeated by {self.char_name}! Don't give up! Try again!")
        
    def drop_loot(self):
        return self.loot
    
