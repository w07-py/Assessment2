from main import slow_print
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
        slow_print(self.country_name)
        slow_print("-------------")
        slow_print(self.description)
        for direction in self.linked_countries:
            country = self.linked_countries[direction]
            slow_print("The " + country.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_countries:
            return self.linked_countries[direction]
        else:
            slow_print("You can't go that way")
            return self

class Store:
    def __init__(self):
        self.store_items = []
        self.prices = {}

    def add_item(self, item: Item, price: int = 30):
        self.store_items.append(item)
        self.prices[item.name] = price

    def display_store(self):
        slow_print("\n=== WELCONE TO THE STORE ===")
        slow_print("Here are the items available for purchase:")
        slow_print("-" * 50)
        for idx, item in enumerate(self.store_items, 1):
            price = self.prices.get(item.name, 30)
            slow_print(f"{idx}. {item.name} - {price} gold")
            slow_print(f"{item.description}")
            slow_print(f"Effect: {item.effect} | Weight: {item.weight}")
            slow_print()
        slow_print("Enter item number to buy, or 0 to cancel.")
        slow_print("-" * 50)
