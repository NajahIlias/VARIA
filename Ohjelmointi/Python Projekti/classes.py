import this


class Player:
    water = 100;
    food = 100;
    health = 100;
    hatchet = False;
    boat = False;
    class Inventory:
        sticks = 0;
        rocks = 0;
        wood = 0;
        berries = 0;

        def wipe():
            Player.Inventory.sticks = 0;
            Player.Inventory.rocks = 0;
            Player.Inventory.wood = 0;
            Player.Inventory.berries = 0;
    
    def __init__(self, name):       
        self.name = name
    
    

