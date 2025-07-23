from item import Item
class Store:
    def __init__(self):
        self.store_items = []

    def add_item(self, item: Item):
        self.store_items.append(item)

    def display_store(self):
        print("Welcome to the Store! Here are the items available:")
        for idx, item in enumerate(self.store_items, 1):
            print(f"{idx}. {item.name} - {item.description} (Effect: {item.effect}, Weight: {item.weight})")