# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, curr_room):
        self.name = name
        self.curr_room = curr_room
        self.inventory = []

    def move_n(self):
        if self.curr_room.n_to == None:
            print("You hit a wall.")
            return
        if self.curr_room.n_to.is_locked == True:
          # check if user has key
            print("This room is locked. Unless you have a key.")
            return
        self.curr_room = self.curr_room.n_to

    def move_s(self):
        if self.curr_room.s_to == None:
            print("You hit a wall.")
            return
        self.curr_room = self.curr_room.s_to

    def move_e(self):
        if self.curr_room.e_to == None:
            print("You hit a wall.")
            return
        self.curr_room = self.curr_room.e_to

    def move_w(self):
        if self.curr_room.w_to == None:
            print("You hit a wall.")
            return
        self.curr_room = self.curr_room.w_to

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def take_item(self, item, room):

        print(len(room.items))
        print(len(self.inventory))

        if len(room.items) == 0:
            print(f"This room has no items.")
            return

        e = False
        for i in room.items:
            if i.name == item:
                room.remove_item(i, self)
                e = True
                break

        if not e:
            print(f"{item} is not here!")

        print(len(room.items))
        print(len(self.inventory))

    def drop_item(self, item, room):

        print(len(room.items))
        print(len(self.inventory))

        if len(self.inventory) == 0:
            print("Inventory is empty.")
            return

        e = False
        for i in self.inventory:
            if i.name == item:
                room.add_item(i, self)
                e = True
                break

        if not e:
            print(f"{item} can't be found in inventory")

        print(len(room.items))
        print(len(self.inventory))

    def view_inventory(self):
        if len(self.inventory) > 0:
            for i in self.inventory:
                print(i.name)
        else:
            print("Inventory is empty.")