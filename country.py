from item import Item
class Country:
    def __init__(self, country_name):
        self.country_name = country_name
        self.description = None
        self.linked_countries = {}
        self.character = None

    def set_description(self, country_description):
        self.description = country_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def set_name(self, country_name):
        self.country_name = country_name

    def get_name(self):
        return self.country_name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character 

    def link_country(self, country_to_link, direction):
        self.linked_countries[direction] = country_to_link

    def get_details(self):
        print(self.country_name)
        print("-------------")
        print(self.description)
        for direction in self.linked_countries:
            country = self.linked_countries[direction]
            print("The " + self.country_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_countries:
            return self.linked_countries[direction]
        else:
            print("You can't go that way")
            return self

class Store:
    def __init__(self):
        self.store_items = []

    def add_item(self, item: Item):
        self.store_items.append(item)

    def display_store(self):
        print("Welcome to the Store! Here are the items available:")
        for idx, item in enumerate(self.store_items, 1):
            print(f"{idx}. {item.name} - {item.description} (Effect: {item.effect}, Weight: {item.weight})")
