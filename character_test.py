from character import Character

harry = Character("Harry", "tall and strong")

harry.describe()

harry.set_conversation("Come here")

harry.talk()

harry.set_weakness("vegemite")

print("What will you fight with?")
fight_with = input("")
harry.fight(fight_with)