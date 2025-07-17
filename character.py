from item import Item

class Player:
    def __init__(self, player_name, appearance, player_skill, ATK = None, player_health = 100, bag_capacity = 50):
        self.player_name = player_name
        self.appearance = appearance
        self.player_skill = player_skill
        self.player_health = player_health
        self.bag_capacity = bag_capacity
        self.bag_items = []
        self.experience = 0
        self.ATK = ATK

    def id_card(self):
        print("Name:", self.player_name)
        print("Appearance:", self.appearance)
        print("Skill:", self.player_skill)
        print("Health:", self.player_health)

    def bag(self):
        total_weight = sum(item.weight for item in self.bag_items)
        remaining = self.bag_capacity - total_weight
        print(f"Your bag capacity is {self.bag_capacity}.")
        print(f"You have {total_weight} units of weight in your bag.")
        print(f"you have {remaining} capacity left")
        if remaining == 0:
            print("Your bag is FULL!")
        if self.bag_items:
            print("The items in your bag:")
            for item in self.bag_items:
                print(f" - {item.name} (Weight: {item.weight})")
        else:
            print("Your bag is empty, pick someting up!")
        
    def pick_up(self, item):
        total_weight = sum(i.weight for i in self.bag_items)
        remaining_capacity = self.bag_capacity - total_weight
        if item.weight <= remaining_capacity:
            self.bag_items.append(item)
            print(f"You picked up: {item.name} (weight: {item.weight})")
        else:
            print(f"You don't have enough capacity to pick it up, try to drop something.")
        
    def amount_health(self, amount):
        self.player_health += amount
        if self.player_health < 0:
            print(f"{self.player_name}, you are killed by the enemy. Game over!")
        elif self.player_health > 0 and amount <30:
            print(f"{self.player_name}, be careful, your health is lower than 30%!")
        elif self.player_health > 30 and amount < 70:
            print(f"{self.player_name}, you are doing well, but be cautious! ")
        else:
            print(f"{self.player_name}, you are in great shape! Keep fighting with them!")

    def fight(self, amount):
        self.player_health -= amount
        print(f"{self.player_name}")

class Character():
    def __init__(self, char_name, char_description):
        self.char_name = char_name
        self.char_description = char_description
        self.conversation = None

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
    
class Enemy(Character):
    def __init__(self, char_name, char_description, ATK = None):
        super().__init__(char_name, char_description)
        self.ATK = ATK

    def fight(self, combat_item):
        if combat_item:
            print("You fend " + self.name + "off with the " + combat_item)
        else:
            print(self.name + "swallows you, little wimp")
            return False


class Boss(Character):
    def __init__(self, char_name, char_description, health = 0, skill = None, weakness = None, ATK = None):
        super().__init__(char_name, char_description)
        self.weakness = weakness
        self.health = health
        self.max_health = health
        self.skill = skill
        self.ATK = ATK

    def describe(self):
        super().describe()
        print("Health:", self.health)
        print("Special Skill:", self.skill)

    def boss_weakness(self):
        if self.health <= self.max_health / 2:
            print(f"The health of {self.char_name} is lower than 50%!")
            print(f"This is his weakness: {self.weakness}")
        else:
          print(f"{self.char_name} is still srong!")  

    def boss_fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You cauch the weakness! Critical strike!")
        else:
            print(f"You attracked {self.char_name}")
        
