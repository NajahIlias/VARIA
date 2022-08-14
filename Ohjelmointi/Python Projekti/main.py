from argparse import Action
from ast import For
from pprint import pprint
from classes import Player
import random
mark = [">","","","","","","","","",""];
selected = 0;
location = "beach";
def win():
    sClear(5)
    print("You use the boat to escape the island, congratulations, you've beaten the game!")
    input("Press any key to reset.")
    global player
    player.Inventory.wipe();
    del player
    Start();

def Start():
    inp = input("Enter your name: ");
    sClear(5);
    print("Your name is "+inp+", you're an adventurer stranded on a remote island. You find yourself at a beach with a thick forest next to it.");
    input("")
    global player
    player = Player(inp);
    global location
    location = "beach";
    World();
    
def lose():
    sClear(5)
    input("You're dead! Press any key to reset.")
    global player
    player.Inventory.wipe();
    del player
    Start();

def World():
    global location
    while True:
        if player.food <= 0 or player.water <= 0 or player.health <= 0:
            input("Suddenly, you collapse.")
            input("It's no use, You're dying!")
            lose();
        sClear(3)
        print("What do you do?")
        action = Actions();
        if location == "beach":
            if action == "W":
                location = "forest"
                print("You enter the forest");
                print("Press any key to continue.")
                input("")
            elif action == "S":
                print("You need a [BOAT] if you want to escape")
                print("Press any key to continue.")
                input("")
                if player.boat == True:
                    win();
            elif action == "A" or action =="D":
                print("You walk along the shoreline and find nothing of interest.")
                print("Press any key to continue.")
                input("")

            
        elif location == "forest":
            if action == "W":
                location = "river";
                print("You keep walking and find a river");
                print("Press any key to continue.")
                input("")
            elif action == "S":
                location = "beach";
                print("You go back to the beach");
                print("Press any key to continue.")
                input("")
            elif action == "D" or action == "A":
                if random.randint(0,1) == 0:
                    print("You find nothing but trees, cut one down?(Y/N)  [HATCHET] required");
                    if Actions() == True:       
                        if player.hatchet == True:
                            amnt = random.randint(1,3)
                            player.Inventory.wood += amnt
                            print("You cut down the tree and get ",amnt, " logs.")
                            print("+",amnt,"WOOD")
                            print("Press any key to continue.")
                            input("")
                        else:
                            print("You don't have a hatchet!")
                            print("Press any key to continue.")
                            input("")
                else:
                    print("You get attacked by a wild boar!");
                    print("-20HP");
                    player.health -= 20;
                    input("")
        elif location == "river":
            if action == "W":
                print("You stand next to the river, drink the water? Y/N")
                if Actions() == True:
                    print("You drink the water")
                    print("+20 Hydration")
                    print("Press any key to continue.")
                    input("")
                    player.water += 20
                    if player.water > 100:
                        print("You're too full, you throw some water up.")
                        player.water = 100;
                        print("Press any key to continue.")
                        input("")                   
            elif action == "A" or action == "D":
                print("Nothing here.")
                print("Press any key to continue.")
                input("")
            elif action == "S":
                location = "forest"
                print("You go back to the forest.")
                print("Press any key to continue.")
                input("")
            

def sClear(amount):
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    print("Controls: Y = Yes, N = No, W = Up/Forward, A = Left, S = Down/Backwards, D = Right, ACT = Perform an action");
    for x in range(amount):
        print("")
def Actions():
    inp = input();
    sClear(3);
    match inp:
        case "Y":
            return True;
        case "N":
            return False;
        case "W":
            return "W"
        case "A":
            return "A"
        case "S":
            return "S"
        case "D":
            return "D"
        case "ACT":
            GUI();
        case _:
            print("Wrong input, read the controls.")
            print("Press any key to continue.")
            input("");
def Selection(x):
    global mark
    global selected
    pointer = mark.index(">");
    mark = ["","","","","","","","","",""]
    if x == "down":
        mark[pointer+1] = ">"
        selected += 1;
        pointer += 1;
    elif x == "up" and pointer > 0:
        mark[pointer-1] = ">"
        selected -= 1;
        pointer -= 1;
    else:
        mark = [">","","","","","","","","",""];
        selected = 0;
        pointer = 0;        
def updown():
    action = Actions()
    if action == "S":
        Selection("down")
    elif action == "W":
        Selection("up")
    elif action == True:
        return True


def GUI():
    sClear(3);
    Selection("reset")
    while(True):
        if player.food <= 0 or player.water <= 0 or player.health <= 0:
            input("Suddenly, you collapse.")
            input("It's no use, You're dying!")
            lose();      
        print("Action list:")
        print("")
        print(mark[0]+"Inventory")
        print(mark[1]+"Player Info")
        print(mark[2]+"Explore")
        print(mark[3]+"Crafting")
        print(mark[4]+"Close action menu")
        if updown() == True:
            match selected:
                case 0:
                    Inventory();
                case 1:
                    PlayerInfo();
                case 2:
                    Explore();
                case 3:
                    Craft();
                case 4:
                    World();
                case _:
                    return "Error."
            

def Inventory():
    while True:
        sClear(3);
        print("Your inventory:")
        print(mark[0]+"Sticks: ",player.Inventory.sticks)
        print(mark[1]+"Rocks: ", player.Inventory.rocks)
        print(mark[2]+"Wood: ", player.Inventory.wood)
        print(mark[3]+"Berries: ", player.Inventory.berries)
        print(mark[4]+"Close")
        print("")
        if updown() == True:
            if selected == 3 and player.Inventory.berries > 0:
                print("You eat a berry.")
                print("-1 BERRY, +7.5 HUNGER")
                print("Press any key to continue.")
                input("")
                player.food += 7.5
                player.Inventory.berries -= 1
                if player.food > 100:
                    print("You're already full, you throw up!")
                    print("Press any key to continue.")
                    input("")
                    player.food = 100
            elif selected == 4:
                GUI();
            else:
                print("Can't use this item.")
                print("Press any key to continue.")
                input("")


        

def PlayerInfo():
    sClear(3);
    print("Player Info:")
    print("")
    print("Health: ", player.health)
    print("Hunger: ", player.food)
    print("Hydration: ", player.water)
    print("")
    print("Press any key to continue.")
    input("")

def Explore():
    sClear(3);
    match location:
        case "beach":
            amnt = random.randint(1,4)
            player.Inventory.rocks += amnt
            print("You find some rocks.")
            print("+ ",amnt,"ROCKS")
            print("")
        case "river":
            print("You find nothing.")
            print("")
        case "forest":
            print("You find some sticks and berries")
            amnt = random.randint(1,3)
            print("+",amnt," STICKS")
            player.Inventory.sticks += amnt;
            amnt = random.randint(1,4)
            print("+",amnt," BERRIES")
            player.Inventory.berries += amnt;
            print("")
    print("After hours of exploring you feel hungrier and thirstier.");
    print("-20 HYDRATION")
    print("-20 HUNGER")
    print("Press any key to continue.")
    input("")
    sClear(3)
    player.food -= 20;
    player.water -= 20;



def Craft():
    Selection("reset")
    while(True):
        sClear(3);
        print("Choose what you want to craft:")
        print(mark[0]+"Basic hatchet                 [2 sticks, 2 rocks]")
        print(mark[1]+"Wooden boat                   [4 logs]")
        print("")
        print(mark[2]+"Go back")
        if updown() == True:
            match selected:
                case 0:
                    if player.Inventory.sticks >= 2 and player.Inventory.rocks >= 2:
                        player.Inventory.sticks -=2
                        player.Inventory.rocks -=2
                        player.hatchet = True;
                        print("You've crafted a [HATCHET], it is now automatically equipped.")
                        print("Press any key to continue.")
                        input("")
                    else:
                        print("You lack the resources.")
                        print("Press any key to continue.")
                        input("")
                case 1:
                    if player.Inventory.wood >= 4:
                        player.Inventory.wood -=4;
                        player.boat = True;
                        print("You've crafted a [BOAT]")
                        print("Press any key to continue.")
                        input("")
                    else:
                        print("You lack the resources.")
                        print("Press any key to continue.")
                        input("");
                case 2:
                    break;
                case _:
                    return "Error."

sClear(6);
print("To start the game, press any button. (Reminder to use CAPSLOCK, and to confirm your ACTION, press ENTER.)")
input("")
Start();