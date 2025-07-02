from country import Country
from character import Enemy

india = Country("India")
india.set_description("A sacred sandstone chamber glowing with eternal fire. Orange tapestries ripple in the heat. Brass bells hang silently from the ceiling, waiting for a ritual that never begins. ")

british = Country("British")
british.set_description("A sandstone chamber lit by oil torches. Hieroglyphics cover the walls, and a weathered altar sits at the center, untouched for centuries.")

bridge_british = Country("Bridge")
bridge_british.set_description("Wodden")

boss_1_room = Country("Boss Tant")
boss_1_room.set_description("Dark")

india.link_room(british, "south")
british.link_room(bridge_british, "east")
bridge_british.link_room(boss_1_room, "east")

egypt_1 = Country("Egypt 1")
egypt_1.set_description("solid")

egypt_2 = Country("Egypt 2")
egypt_2.set_description("Golden")

power_store = Country("Power store")
power_store.set_description("It's a place to gain power!")

boss_2_room = Country("Boss Queen")
boss_2_room.set_description("Bright")

british.link_room(egypt_1, "south")
egypt_1.link_room(power_store, "east")
egypt_1.link_room(egypt_2, "south")
egypt_2.link_room(boss_2_room, "east")

japan = Country("Japan")
japan.set_description("green")

store = Country("Store")
store.set_description("A place to buy weapon.")

bridge_japan = Country("Japanes Bridge")
bridge_japan.set_description("Banmboo")

Boss_3_room = Country("Saku")
Boss_3_room.set_description("Wodden and broght")

door_1 = Country("Door 1")
door_1.set_description("huge bright")

egypt_2.link_room(japan, "south")
japan.link_room(store, "east")
japan.link_room(bridge_japan, "south")
bridge_japan.link_room(Boss_3_room, "south")
bridge_japan.link_room(door_1, "east")

china = Country("China")
china.set_description("red")

museum = Country("Museum")
museum.set_description("All the bosses before were here.")

street_1 = Country("Street 1")
street_1.set_description("res and dark")

street_2 = Country("Street 2")
street_2.set_description("Golden and red")

big_bosses_room = Country("Final bosses")
big_bosses_room.set_description("Hunge and a lot.")

door_1.link_room(china, "north")
china.link_room(museum, "east")
museum.link_room(street_1, "east")
street_1.link_room(street_2, "north")
street_2.link_room(big_bosses_room, "west")


current_room = british
while True:
    print("\n")
    current_room.get_details()
    command=input(">")
    current_rooms = current_room.move(command)
    


