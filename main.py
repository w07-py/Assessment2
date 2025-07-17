from country import Country
import time
from character import Character
from item import Outfit
from character import Player

def slow_print(text, delay = 0.05):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(delay)

time.sleep(1.5)
slow_print("Dear player, welcome to Empire Assassins!")
time.sleep(1.5)

print("")

slow_print("In this game, you'll venture through different countries,")
time.sleep(1.5)

print("")

print("each with its own unique boss to defeat.")
time.sleep(1.5)

print("")

print("You'll have the freedom to choose your name and appearance,")
time.sleep(1.5)

print("")

print("and pick one skill you like from a range of powerful abilities.")
time.sleep(1.5)

print("")

print("Along the way, there will be many surprises and hidden easter eggs waiting for you.")
time.sleep(1.5)

print("")

print("There are some details you should know before starting your journey:")
time.sleep(1.5)

print("")

print("1. You can move between countries and rooms in different countries.")
time.sleep(1.5)

print("")

print("But you can't move back to the last country. ")
time.sleep(1.5)

print("")

print("Always type the direction you want to go, e.g., 'north', 'south'...)")
time.sleep(1.5)

print("")

print("2. When you get the key from the boss, you can open the door to the next country.")
time.sleep(1.5)

print("")

input("Are you ready to begin your adventure? (TYPE enter to begin)")
time.sleep(1.5)

print("")

name = input("Please creating a name:")
time.sleep(1.5)

guide = Character("Kael", "A hooded figure in a weathered cloak, his face hidden in shadows. Only a faint glimmer of silver hair and piercing eyes can be seen beneath the hood.")
guide.set_conversation("Welcome, " + name + ". I am Kael. This is the Empire of Assassins,\n"
                        "The Five Monarchs forged this realm with their own hands. \n"
                        "Legend says that only true warriors and assassins can pass the trials they left behind. \n"
                        "And I... am the one who leads such brave souls on their journey. \n"
                        "Good luck on your journey. But first, I have two gifts for you - a cloak and a crystal. Choose whichever you prefer.")

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
        name = "Drgonscale Vest",
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
print("There are three didderent kinds of crystal, feel free to choose one: ")
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

india = Country("Ashvara Flame Hall")
india.set_description("A sacred sandstone chamber glowing with eternal fire. Orange tapestries ripple in the heat. Brass bells hang silently from the ceiling, waiting for a ritual that never begins. ")

british = Country("Thornshade Hall")
british.set_description("A shadow-draped Victorian hall lined with thorn-covered pillars. Dusty portraits observe in silence while cold air stirs the candle flames and ancient whispers drift through the gloom.")

bridge_british = Country("Fogveil Brdge")
bridge_british.set_description("An arched stone bridge covered in moss and ivy. Beneath it flows a dark, silent river. The fog lingers, thick and low, swallowing all sound.")

boss_british = Country("Chapel of Iron")
boss_british.set_description("A gothic chamber with high stained-glass windows. Cold drafts coil through thorn-covered pillars, and the air smells faintly of iron.")

egypt_1 = Country("Hall of Glyphs")
egypt_1.set_description("A sandstone chamber lit by oil torches. Hieroglyphics cover the walls, and a weathered altar sits at the center, untouched for centuries.")

power_store = Country("Vault of Power")
power_store.set_description("A hidden chamber where forgotten strength lingers in the air. Ancient tools and glowing glyphs suggest a place where one's power can be awakened.")

egypt_2 = Country("Anubis Passage")
egypt_2.set_description("A narrow corridor flanked by jackal-headed statues. The silence is thick, broken only by the faint echo of breathing and shifting dust.")

boss_egypt = Country("Queen's Rest")
boss_egypt.set_description("A golden burial chamber sealed in time. A stone sarcophagus glows faintly at the center, and sacred energy vibrates beneath the sands.")

japan = Country("Sakura Courtyard")
japan.set_description("A moss-covered courtyard where a lone cherry blossom tree blooms out of season. Petals remain suspended mid-air, frozen in a moment of stillness.")

store = Country("Spirit Market")
store.set_description("A modesr shrine converted into a market. Blades, charms, and armor lie neatly arranged under fluttering paper lanterns.")

bridge_japan = Country("Crescent Moon Bridge")
bridge_japan.set_description("A delicate wodden brodge arched like a cresvent moon. Lanterns sway gently from its beams")

boss_japan_1 = Country("Doji of Saku")
boss_japan_1.set_description("A moonlit doji lined with polished katanas. A solitary mat lies untouched at the center, radiating tension in the stillness.")

boss_japan_2 = Country("Shrine of Aokusa")
boss_japan_2.set_description("A msit-shrouded shrine interior filled with the scent of incense. Sacred talismans float weightlessly, and the atmosphere hums with restrained power.")

china = Country("Jade Throne Hall")
china.set_description("A grand hall supported by jade pillars and gloden rafters. Massive scrolls hang from the ceiling, and a silent brass gong dominates the center.")

museum = Country("Archive of Echoes")
museum.set_description("A quiet museum chamber filled with ancient artifacts enclosed in galss. Dragon motifs spiral across cracked scrolls, and dust motes float in frozen shafts of light.")

street_1 = Country("Crimson Lion Corridor")
street_1.set_description("A crimson corridor lined with lion statues. Enery footstep echoes with unnatural clarity, and shadows seem to shift in the corners of viison.")

street_2 = Country("Silent Water Walk")
street_2.set_description("A narrow hallway with polished stone floors and flowing water along the walls. Lanterns cast wavering reflection like unseen eyes.")

boss_china_1 = Country("Skyforge Arena")
boss_china_1.set_description("A stone courtyard beneath open sky. Weapon racks line the walls, and a red banner stirs without wind.")

boss_china_2 = Country("Forsted Throne")
boss_china_2.set_description("A frost-covered throne room where icicles hang from the ceiling. The floor crunches with each step, delicate as glass.")

boss_china_3 = Country("Chamber of Stillness")
boss_china_3.set_description("A meditation chamber surrounded by still air. A sand garden remains undisturbed, and candles bure with no visible flame.")

boss_china_4 = Country("Phonenix Altar")
boss_china_4.set_description("A blazing altar chamber filled with dancing embers. Vermilion feathers swirl in the air like echoes of a phoenix reborn.")


india.link_country(british, "south")

british.link_country(bridge_british, "east")
bridge_british.link_country(british, "west")
bridge_british.link_country(boss_british, "east")
boss_british.link_country(british, "west")

british.link_country(egypt_1, "south")

egypt_1.link_country(power_store, "east")
power_store.link_country(egypt_1, "west")
egypt_1.link_country(egypt_2, "south")
egypt_2.link_country(egypt_1, "noeth")
egypt_2.link_country(boss_egypt, "east")
boss_egypt.link_country(boss_egypt, "west")

egypt_2.link_country(japan, "south")

japan.link_country(store, "east")
store.link_country(japan, "west")
japan.link_country(bridge_japan, "south")
bridge_japan.link_country(japan, "north")
bridge_japan.link_country(boss_japan_1, "south")
boss_japan_1.link_country(bridge_japan, "north")
boss_japan_1.link_country(boss_japan_2, "east")
boss_japan_2.link_country(boss_japan_1, "west")

boss_china_2.link_country(china, "east")

china.link_country(museum, "east")
museum.link_country(china, "west")
museum.link_country(street_1, "east")
street_1.link_country(museum, "west")
street_1.link_country(street_2, "north")
street_2.link_country(street_1, "south")
street_2.link_country(boss_british, "west")
boss_china_1.link_country(boss_china_2, "west")
boss_china_2.link_country(boss_china_1, "east")
boss_china_2.link_country(boss_china_3, "north")
boss_china_3.link_country(boss_china_2, "south")
boss_china_3.link_country(boss_china_4, "east")
boss_china_4.link_country(boss_china_3, "west")
boss_china_4.link_country(boss_china_1, "south")
boss_china_1.link_country(boss_china_4, "north")

current_country = india
while True:
    print("\n")
    current_country.get_details()
    command = input(">")
    current_country = current_country.move(command)
    
    

