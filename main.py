from country import Country
from character import Enemy

india = Country("India")
india.set_description("A sacred sandstone chamber glowing with eternal fire. Orange tapestries ripple in the heat. Brass bells hang silently from the ceiling, waiting for a ritual that never begins. ")

british = Country("British")
british.set_description("A shadow-draped Victorian hall lined with thorn-covered pillars. Dusty portraits observe in silence while cold air stirs the candle flames and ancient whispers drift through the gloom.")

bridge_british = Country("Old Bridge")
bridge_british.set_description("An arched stone bridge covered in moss and ivy. Beneath it flows a dark, silent river. The fog lingers, thick and low, swallowing all sound.")

boss_british_room = Country("Blackthorn")
boss_british_room.set_description("A gothic chamber with high stained-glass windows. Cold drafts coil through thorn-covered pillars, and the air smells faintly of iron.")

india.link_room(british, "south")
british.link_room(bridge_british, "east")
bridge_british.link_room(boss_british_room, "east")

egypt_1 = Country("Egypt 1")
egypt_1.set_description("A sandstone chamber lit by oil torches. Hieroglyphics cover the walls, and a weathered altar sits at the center, untouched for centuries.")

egypt_2 = Country("Egypt 2")
egypt_2.set_description("A narrow corridor flanked by jackal-headed statues. The silence is thick, broken only by the faint echo of breathing and shifting dust.")

power_store = Country("Power store")
power_store.set_description("It's a place to gain power!")

boss_egypt_room = Country("Boss Queen")
boss_egypt_room.set_description("A golden burial chamber sealed in time. A stone sarcophagus glows faintly at the center, and sacred energy vibrates beneath the sands.")

british.link_room(egypt_1, "south")
egypt_1.link_room(power_store, "east")
egypt_1.link_room(egypt_2, "south")
egypt_2.link_room(boss_egypt_room, "east")

japan = Country("Japan")
japan.set_description("A moss-covered courtyard where a lone cherry blossom tree blooms out of season. Petals remain suspended mid-air, frozen in a moment of stillness.")

store = Country("Store")
store.set_description("A place to buy weapon.")

bridge_japan = Country("Moon Bridge")
bridge_japan.set_description("A delicate wodden brodge arched like a cresvent moon. Lanterns sway gently from its beams")

boss_japan_1_room = Country("Saku")
boss_japan_1_room.set_description("A moonlit doji lined with polished katanas. A solitary mat lies untouched at the center, radiating tension in the stillness.")

boss_japan_2_room = Country("afhau")
boss_japan_2_room.set_description("A msit-shrouded shrine interior filled with the scent of incense. Sacred talismans float weightlessly, and the atmosphere hums with restrained power.")

door_1 = Country("Door")
door_1.set_description("good")

egypt_2.link_room(japan, "south")
japan.link_room(store, "east")
japan.link_room(bridge_japan, "south")
bridge_japan.link_room(boss_japan_1_room, "south")
boss_japan_1_room.link_room(boss_japan_2_room, "east")

china = Country("China")
china.set_description("A grand hall supported by jade pillars and gloden rafters. Massive scrolls hang from the ceiling, and a silent brass gong dominates the center.")

museum = Country("Museum")
museum.set_description("A quiet museum chamber filled with ancient artifacts enclosed in galss. Dragon motifs spiral across cracked scrolls, and dust motes float in frozen shafts of light.")

street_1 = Country("Street 1")
street_1.set_description("A crimson corridor lined with lion statues. Enery footstep echoes with unnatural clarity, and shadows seem to shift in the corners of viison.")

street_2 = Country("Street 2")
street_2.set_description("A narrow hallway with polished stone floors and flowing water along the walls. Lanterns cast wavering reflection like unseen eyes.")

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
    command = input(">")
    current_rooms = current_room.move(command)
    
    

