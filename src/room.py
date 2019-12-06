class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.hidden_items = None
        self.hidden_rooms = None
        self.is_dark = False
        self.is_locked = False

    def add_item(self, item, player):
        self.items.append(item)
        player.remove_from_inventory(item)

    def remove_item(self, item, player):
        if self.is_dark:
            print("Unable to do anything as you can't see.")
            return
        self.items.remove(item)
        player.add_to_inventory(item)

    def view_items(self):
        if self.is_dark:
            print("Room is too dark - you can't see!")
            return

        if len(self.items) > 0:
            for item in self.items:
                print(item.name)
        else:
            print("Room is too dark to do anything.")