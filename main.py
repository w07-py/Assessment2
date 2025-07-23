#symple Function
import time
import random
from enum import Enum

#Country.py
from country import Country
from country import Store

#Character.py
from character import Player
from character import Character
from character import Boss

#Item.py
from item import Outfit
from item import Key
from item import Weapon
from item import Armor
from item import Potion
from item import Special
from item import ObtainMethod

#Skill.py
from skill import Skill

def slow_print(text, delay = 0.05):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(delay)
    print()
    

time.sleep(1)
slow_print("Dear player, welcome to Empire Assassins!")
time.sleep(1)

slow_print("In this game, you'll venture through different countries,")
time.sleep(1)

slow_print("each with its own unique boss to defeat.")
time.sleep(1)

slow_print("You'll have the freedom to choose your name and appearance,")
time.sleep(1)

slow_print("and pick one skill you like from a range of powerful abilities.")
time.sleep(1)

slow_print("Along the way, there will be many surprises and hidden easter eggs waiting for you.")
time.sleep(1)

slow_print("There are some details you should know before starting your journey:")
time.sleep(1)

slow_print("1. You can move between countries and rooms in different countries.")
time.sleep(1)

slow_print("But you can't move back to the last country. ")
time.sleep(1)

slow_print("Always type the direction you want to go, e.g., 'north', 'south'...)")
time.sleep(1)

slow_print("2. When you get the key from the boss, you can open the door to the next country.")
time.sleep(1)

input("Are you ready to begin your adventure? (TYPE enter to begin)")
time.sleep(1)

name = input("Please create a name:")
time.sleep(1)

guide = Character("Kael", "A hooded figure in a weathered cloak, his face hidden in shadows. Only a faint glimmer of silver hair and piercing eyes can be seen beneath the hood.")
guide.set_conversation(slow_print("Welcome, " + name + ". I am Kael. This is the Empire of Assassins,\n"
                        "The Five Monarchs forged this realm with their own hands. \n"
                        "Legend says that only true warriors and assassins can pass the trials they left behind. \n"
                        "And I... am the one who leads such brave souls on their journey. \n"
                        "Good luck on your journey. But first, I have two gifts for you - a cloak and a crystal. Choose whichever you prefer."))

guide.describe()
time.sleep(1.5)

guide.talk()

cloaks = [
    Outfit(
        name = "Saffron silk Robe",
        description = "A flowing robe dyed in deep saffron, stitched with mandalas. It whispers in the qind like a prayer.",
    ),
    Outfit(
        name = "Royal Thorn Cloak",
        description = "Dark velvet cloak with silver trim and hissen thorns. Once worn by nobles.",
    ),
    Outfit(
        name = "Desert Moon Garb",
        description = "Light garb that shimmers under moonlight. Sand never clings to it.",
    ),
    Outfit(
        name = "Silent Wind Haori",
        description = "Indigo haori that moves without sound, stitched with wind god symbols."
    ),
    Outfit(
        name = "Dragonscale Vest",
        description = "Sleeveless Vest covered with silk scales like a dragon's hide. Feels alive."
    ),
]

print("This is the cloak: ")
for i, cloak in enumerate(cloaks, 1):
    print(f"{i}. {cloak.name}")
choice = int(input("Enter the number of your choice (1-5):"))
while choice < 1 or choice > 5:
    choice = int(input("Please enter the number of your choice:"))

cloak_choice = cloaks[choice - 1]
cloak_choice.outfit_details()

skills = [
    "Surge of Power  Tycoon",
    "Blessing of life ",
    "Gold Tycoon",
]
print("There are three different kinds of crystal, feel free to choose one: ")
for i, skill in enumerate(skills, 1):
    print(f"{i}. {skill}")
skill_choice = int(input("Enter the number of your choice (1-3):"))
while skill_choice < 1 or skill_choice > 3:
    skill_choice = int(input("Please choose again (1-3):"))
chosen_skill = skills[skill_choice - 1]

player = Player(
    player_name = name,
    appearance = cloak_choice.name,
    player_skill = chosen_skill,
    ATK = 10
)

player.id_card()

#Country
india = Country("Ashvara Flame Hall")
india.set_description("A sacred sandstone chamber glowing with eternal fire. Orange tapestries ripple in the heat. Brass bells hang silently from the ceiling, waiting for a ritual that never begins. ")

british = Country("Thornshade Hall")
british.set_description("A shadow-draped Victorian hall lined with thorn-covered pillars. Dusty portraits observe in silence while cold air stirs the candle flames and ancient whispers drift through the gloom.")

bridge_british = Country("Fogveil Bridge")
bridge_british.set_description("An arched stone bridge covered in moss and ivy. Beneath it flows a dark, silent river. The fog lingers, thick and low, swallowing all sound.")

boss_room_british = Country("Chapel of Iron")
boss_room_british.set_description("A gothic chamber with high stained-glass windows. Cold drafts coil through thorn-covered pillars, and the air smells faintly of iron.")

egypt_1 = Country("Hall of Glyphs")
egypt_1.set_description("A sandstone chamber lit by oil torches. Hieroglyphics cover the walls, and a weathered altar sits at the center, untouched for centuries.")

power_store = Country("Vault of Power")
power_store.set_description("A hidden chamber where forgotten strength lingers in the air. Ancient tools and glowing glyphs suggest a place where one's power can be awakened.")

egypt_2 = Country("Anubis Passage")
egypt_2.set_description("A narrow corridor flanked by jackal-headed statues. The silence is thick, broken only by the faint echo of breathing and shifting dust.")

boss_room_egypt = Country("Queen's Rest")
boss_room_egypt.set_description("A golden burial chamber sealed in time. A stone sarcophagus glows faintly at the center, and sacred energy vibrates beneath the sands.")

japan = Country("Sakura Courtyard")
japan.set_description("A moss-covered courtyard where a lone cherry blossom tree blooms out of season. Petals remain suspended mid-air, frozen in a moment of stillness.")

store = Country("Spirit Market")
store.set_description("A modest shrine converted into a market. Blades, charms, and armor lie neatly arranged under fluttering paper lanterns.")

bridge_japan = Country("Crescent Moon Bridge")
bridge_japan.set_description("A delicate wooden bridge arched like a crescent moon. Lanterns sway gently from its beams")

boss_room_japan_1 = Country("Doji of Saku")
boss_room_japan_1.set_description("A moonlit doji lined with polished katanas. A solitary mat lies untouched at the center, radiating tension in the stillness.")

boss_room_japan_2 = Country("Shrine of Aokusa")
boss_room_japan_2.set_description("A mist-shrouded shrine interior filled with the scent of incense. Sacred talismans float weightlessly, and the atmosphere hums with restrained power.")

china = Country("Jade Throne Hall")
china.set_description("A grand hall supported by jade pillars and golden rafters. Massive scrolls hang from the ceiling, and a silent brass gong dominates the center.")

museum = Country("Archive of Echoes")
museum.set_description("A quiet museum chamber filled with ancient artifacts enclosed in glass. Dragon motifs spiral across cracked scrolls, and dust motes float in frozen shafts of light.")

street_1 = Country("Crimson Lion Corridor")
street_1.set_description("A crimson corridor lined with lion statues. Every footstep echoes with unnatural clarity, and shadows seem to shift in the corners of vision.")

street_2 = Country("Silent Water Walk")
street_2.set_description("A narrow hallway with polished stone floors and flowing water along the walls. Lanterns cast wavering reflection like unseen eyes.")

boss_room_china_1 = Country("Skyforge Arena")
boss_room_china_1.set_description("A stone courtyard beneath open sky. Weapon racks line the walls, and a red banner stirs without wind.")

boss_room_china_2 = Country("Forsted Throne")
boss_room_china_2.set_description("A frost-covered throne room where icicles hang from the ceiling. The floor crunches with each step, delicate as glass.")

boss_room_china_3 = Country("Chamber of Stillness")
boss_room_china_3.set_description("A meditation chamber surrounded by still air. A sand garden remains undisturbed, and candles bure with no visible flame.")

boss_room_china_4 = Country("Phonenix Altar")
boss_room_china_4.set_description("A blazing altar chamber filled with dancing embers. Vermilion feathers swirl in the air like echoes of a phoenix reborn.")

#Boss
boss_india = Boss(
    char_name = "Ashvara the Eternal Flame",
    char_description = "A divine warrior wreathed in sacred flame, with eyes that reflect the eternal cycle.",
    health = 45,
    skill = "",
    weakness = "",
    ATK = random.randint(1, 15)
)

boss_british = Boss(
    char_name = "Lord Blackthorn of Albion",
    char_description = "A noble draped in shadowed robes and thorns, plotting with an ever-sinister smile.",
    health = 65,
    skill = "",
    weakness = "",
    ATK = random.randint(5, 15)
)

boss_egypt = Boss(
    char_name = "Pharaoh Nefra-Ra",
    char_description = "An ancient pharaoh risen from the sands, radiating death and divine power.",
    health = 85,
    skill = "",
    weakness = "",
    ATK = random.randint(10, 30)
)

boss_japan_1 = Boss(
    char_name = "Shogun Kurokami",
    char_description = "A silent samurai with jet-black hair, blade always half-drawn and gaze never shaken.",
    health = 95,
    skill = "",
    weakness = "",
    ATK = random.randint(5, 40)
)

boss_japan_2 = Boss(
    char_name = "Priestess Aokusa",
    char_description = "A shrine maiden bathed in green light, surrounded by sacred spirits and chants.",
    health = 105,
    skill = "Nature's Invocation",
    weakness = "",
    ATK = random.randint(10, 40)
)

boss_china_1 = Boss(
    char_name = "General Longwei",
    char_description = "A towering general clad in dragon-engraved armor, exuding a fierce aura of loyalty and strength.",
    health = 110,
    skill = "",
    weakness = "",
    ATK = random.randint(25, 50)
)

boss_china_2 = Boss(
    char_name = "Empress Xuelan",
    char_description = "An elegant but distant empress whose steps chill the air, ruling with ice and iron.",
    health = 115,
    skill = "",
    weakness = "",
    ATK = random.randint(30, 50)
)

boss_china_3 = Boss(
    char_name = "Master Wuchen",
    char_description = "A cloaked hermit whose voice echoes with ancient wisdom. Dust never touches his steps.",
    health = 120,
    skill = "",
    weakness = "",
    ATK = random.randint(25, 60)
)

boss_china_4 = Boss(
    char_name = "Zhu Yan the Vermilion Flame",
    char_description = "A blazing figure wrapped in vermilion fire, laughing amidst destruction.",
    health = 160,
    skill = "",
    weakness = "",
    ATK = random.randint(35, 70)
)

#Item
    #KEY
india_key = Key(country="india")
british_key = Key(country="british")
egypt_key = Key(country="egypt")
china_key = Key(country="china")
japan_key_half1 = Key(country="japan", half_key=True) 
japan_key_half2 = Key(country="japan", half_key=True)

    #WEAPON
weapon_india = Weapon(
    name="Scimitar of Eternal Flame",
    damage=18,
    description="A curved blade imbued with sacred fire, said to purify all it touches.",
    effect="Chance to inflict burning (3 damage/turn for 3 turns)",
    obtain_method = ObtainMethod.BOSS_DROP
)

weapon_british = Weapon(
    name="Blackthorn's Rapier",
    damage=20,
    description="An elegant yet deadly blade entwined with living thorns.",
    effect="Critical hits poison the enemy (2 damage/turn for 5 turns)",
    obtain_method=ObtainMethod.BOSS_DROP
)

weapon_egypt = Weapon(
    name="Khopesh of the Sun God",
    damage=25,
    description="An ancient golden blade bearing hieroglyphs of Ra's power.",
    effect="+5 damage against undead enemies",
    obtain_method=ObtainMethod.BOSS_DROP
)

weapon_japan_1 = Weapon(
    name="Kurokami's Shadow Katana",
    damage=28,
    description="A jet-black katana that seems to absorb light around it.",
    effect="20% chance to dodge attacks",
    obtain_method=ObtainMethod.BOSS_DROP
)

weapon_japan_2 = Weapon(
    name="Aokusa's Sakura Staff",
    damage=22,
    description="A wooden staff adorned with eternally blooming cherry blossoms.",
    effect="Heals 5 HP per turn",
    obtain_method=ObtainMethod.BOSS_DROP
)

weapon_china_1 = Weapon(
    name="Longwei's Dragon Glaive",
    damage=32,
    description="A massive polearm with intricate dragon carvings along its blade.",
    effect="+10 damage on first attack each combat",
    obtain_method=ObtainMethod.BOSS_DROP
)

weapon_china_2 = Weapon(
    name="Xuelan's Frost Fan",
    damage=26,
    description="An ornate fan that chills the air with each graceful movement.",
    effect="Chance to freeze enemies (skip their next turn)",
    obtain_method=ObtainMethod.BOSS_DROP
)

weapon_china_3 = Weapon(
    name="Wuchen's Taoist Sword",
    damage=30,
    description="A simple yet deadly jian sword imbued with ancient wisdom.",
    effect="+5% critical hit chance for each turn in combat (max 25%)",
    obtain_method=ObtainMethod.BOSS_DROP
)

weapon_china_4 = Weapon(
    name="Zhu Yan's Vermillion Blade",
    damage=40,
    description="A sword forged in celestial fire, radiating intense heat.",
    effect="Burning effect deals double damage",
    obtain_method=ObtainMethod.BOSS_DROP
)

    #ARMOR
pharaohs_crown = Armor(
    name="Pharaoh's Golden Crown",
    defense=15,
    description="An ornate golden crown said to grant divine protection.",
    effect="+5 resistance to magic attacks",
    weight=2.5,
    obtain_method=ObtainMethod.STORE
)

samurai_helmet = Armor(
    name="Kabuto of the Shogun",
    defense=20,
    description="A traditional samurai helmet adorned with a fearsome mempo mask.",
    effect="Reduces critical hit damage by 50%",
    weight=3,
    obtain_method=ObtainMethod.STORE
)

dragon_armor = Armor(
    name="Imperial Dragon Armor",
    defense=35,
    description="Heavy armor with intricate dragon scales that seem to shimmer.",
    effect="Reduces all damage by 10%",
    weight=5,
    obtain_method=ObtainMethod.STORE
)

flame_cloak = Armor(
    name="Cloak of Eternal Flame",
    defense=25,
    description="A flowing cloak that radiates comforting warmth.",
    effect="Immunity to fire damage",
    weight=2,
    obtain_method=ObtainMethod.STORE
)

hermits_sandals = Armor(
    name="Wuchen's Traveling Sandals",
    defense=10,
    description="Simple sandals that leave no trace in dust or snow.",
    effect="+10% evasion chance",
    weight=1,
    obtain_method=ObtainMethod.QUEST
)

    #POTION
health_potion_small = Potion(
    name="Small Health Potion",
    potion_type="health",
    amount=20,
    description="A red potion that restores vitality.",
    effect="Restores 20 HP",
    weight=0.5,
    obtain_method=ObtainMethod.STORE
)

health_potion_large = Potion(
    name="Large Health Potion",
    potion_type="health",
    amount=50,
    description="A potent red potion that mends serious wounds.",
    effect="Restores 50 HP",
    weight=1,
    obtain_method=ObtainMethod.STORE
)

strength_potion = Potion(
    name="Potion of Strength",
    potion_type="strength",
    amount=10,
    description="A bubbling orange liquid that temporarily enhances muscle power.",
    effect="+10 ATK for 3 turns",
    weight=0.5,
    obtain_method=ObtainMethod.STORE
)

    #SPECIAL
revival_coin = Special(
    name="Coin of Rebirth",
    description="An ancient coin bearing symbols of life and death.",
    effect="Revives with 50% HP when defeated (consumed on use)",
    weight=0.1,
    obtain_method=ObtainMethod.QUEST
)

#Method
india.link_country(british, "south")

british.link_country(bridge_british, "east")
bridge_british.link_country(british, "west")
bridge_british.link_country(boss_room_british, "east")
boss_room_british.link_country(british, "west")

british.link_country(egypt_1, "south")

egypt_1.link_country(power_store, "east")
power_store.link_country(egypt_1, "west")
egypt_1.link_country(egypt_2, "south")
egypt_2.link_country(egypt_1, "north")
egypt_2.link_country(boss_room_egypt, "east")
boss_room_egypt.link_country(egypt_2, "west")

egypt_2.link_country(japan, "south")


japan.link_country(store, "east")
store.link_country(japan, "west")
japan.link_country(bridge_japan, "south")
bridge_japan.link_country(japan, "north")
bridge_japan.link_country(boss_room_japan_1, "south")
boss_room_japan_1.link_country(bridge_japan, "north")
boss_room_japan_1.link_country(boss_room_japan_2, "east")
boss_room_japan_2.link_country(boss_room_japan_1, "west")

boss_room_japan_2.link_country(china, "east")

china.link_country(museum, "east")
museum.link_country(china, "west")
museum.link_country(street_1, "east")
street_1.link_country(museum, "west")
street_1.link_country(street_2, "north")
street_2.link_country(street_1, "south")
street_2.link_country(boss_room_china_1, "west")
boss_room_china_1.link_country(boss_room_china_2, "west")
boss_room_china_2.link_country(boss_room_china_1, "east")
boss_room_china_2.link_country(boss_room_china_3, "north")
boss_room_china_3.link_country(boss_room_china_2, "south")
boss_room_china_3.link_country(boss_room_china_4, "east")
boss_room_china_4.link_country(boss_room_china_3, "west")
boss_room_china_4.link_country(boss_room_china_1, "south")
boss_room_china_1.link_country(boss_room_china_4, "north")

#Boss
india.set_character(boss_india)
british.set_character(boss_british)
boss_room_egypt.set_character(boss_egypt)
boss_room_japan_1.set_character(boss_japan_1)
boss_room_japan_2.set_character(boss_japan_2)
boss_room_china_1.set_character(boss_china_1)
boss_room_china_2.set_character(boss_china_2)
boss_room_china_3.set_character(boss_china_3)
boss_room_china_4.set_character(boss_china_4)

#Boss_Item
boss_india.loot.append(weapon_india)
boss_british.loot.append(weapon_british)
boss_egypt.loot.append(weapon_egypt)
boss_japan_1.loot.append(weapon_japan_1)
boss_japan_2.loot.append(weapon_japan_2)
boss_china_1.loot.append(weapon_china_1)
boss_china_2.loot.append(weapon_china_2)
boss_china_3.loot.append(weapon_china_3)
boss_china_4.loot.append(weapon_china_4)

#Store_Item
def add_item_to_store():
    game_store = Store()
    game_store.add_item(Armor(
        name="Guardian Helmet",
        defense=10,
        description="A sturdy helmet to protect your head.",
        effect="Increase defense by 10",
        weight=2,
        obtain_method=ObtainMethod.STORE
    ))

    game_store.add_item(Armor(
        name="Iron Chestplate",
        defense=15,
        description="Solid chest armor.",
        effect="Blocks 20% damage",
        weight=4,
        obtain_method=ObtainMethod.STORE
    ))

    game_store.add_item(Armor(
        name="Phoenix Cloak",
        defense=12,
        description="A cloak woven with fire-resistant feathers.",
        effect="Immunity to fire damage",
        weight=2,
        obtain_method=ObtainMethod.STORE
    ))

    game_store.add_item(Armor(
        name="Hermit's Sandals",
        defense=5,
        description="Lightweight sandals that enhance mobility.",
        effect="+10% evasion chance",
        weight=1,
        obtain_method=ObtainMethod.STORE
    ))

    game_store.add_item(Potion(
        name="Health Potion",
        potion_type="Health",
        amount=50,
        description="Restores 50 HP.",
        effect="Restore 50 health",
        weight=1,
        obtain_method=ObtainMethod.STORE
    ))

    game_store.add_item(Potion(
        name="Strength Potion",
        potion_type="Strength",
        amount=20,
        description="Boosts your attack power.",
        effect="Increase ATK by 20 for 3 turns",
        weight=1,
        obtain_method=ObtainMethod.STORE
    ))

    game_store.add_item(Potion(
        name="Elixir of Defense",
        potion_type="Defense",
        amount=15,
        description="Temporarily hardens your skin.",
        effect="+15 DEF for 3 turns",
        weight=1,
        obtain_method=ObtainMethod.STORE
    ))
    
    game_store.display_store()


current_country = india
dead = False

current_country.get_details()
while dead == False:
    print("\n")
    inhabitant = current_country.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input(">")
    if command in ["north", "south", "east", "west"]:
        current_country = current_country.move(command)
        if current_country == store:
            add_item_to_store()

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if inhabitant is not None:
            fight_with= input("What will you fight with?\n")
            if isinstance(inhabitant, Boss):
                result = player.fight(inhabitant, fight_with)
                #boss_ATK = inhabitant.boss_fight(player)
                if result is True:
                    print("Bravo, hero you won the fight!")
                    current_country.set_character(None)
                elif result is False:
                    dead = True
    
