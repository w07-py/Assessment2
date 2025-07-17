class Outfit:
    def __init__(self, name, description, surprise = None):
        self.name = name 
        self.description = description
        self.surprise = surprise

    def outfit_details(self):
        print("Your Cloak: " + self.name)
        print("Have a look " + self.description)

class Item:
    def __init__(self, name, description, effect = None, weight = 0):
        self.name = name
        self.description = description
        self.effect = effect
        self.weight = weight

