class Country:
    def __init__(self, country_name):
        self.name = country_name
        self.description = None
        self.linked_rooms = {}
        self.character = None

    def set_description(self, country_description):
        self.description = country_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def set_name(self, country_name):
        self.name = country_name

    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character 

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self


