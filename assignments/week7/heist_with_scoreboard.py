# Comments spread throughout, with final comments at the bottom.

# SOLUTION | DON'T READ FOR SPOILERS
# You move around and search each room to find loot.
# You drop the fake money to pickup later since you don't have much inventory space.
# You use the battery to power the machine, and gloves to pickup nails, before crafting a key.
# You pickup the fake money again.
# You use a key you craft to get into the safe room, searching the room, replacing the money with fake money.
# You then escape with the money using the key in the southern room.

import time
import os
import csv

DEBUG = True
# Use 'debug' to toggle between modes! Using this command resets all progress.

escaping = False
start_time = 0
end_time = 0
final_time = 0

inventory = [
    {"name": "Fake Money", "type": "Valuable", "description": "Can fool anyone as real money. Should be used."}
]
room_north = [
    {"name": "Money", "type": "Valuable", "description": "Obtained very legally."}
]
room_east = [
    {"name": "Metal Scrap", "type": "Material", "description": "Useless on it's own. Can be used to craft."},
    {"name": "Glove", "type": "Valuable", "description": "Let's you pick up nails."}
]
room_south = [
    {"name": "Nail", "type": "Material", "description": "Useless on it's own. Can be used to craft."},
    {"name": "Battery", "type": "Material", "description": "This could be used to power something."}
]
room_west = [
    {"name": "Nail", "type": "Material", "description": "Useless on it's own. Can be used to craft."}
]
everything = [
    {"name": "Fake Money", "type": "Valuable", "description": "Can fool anyone as real money. Should be used."},
{"name": "Money", "type": "Valuable", "description": "Obtained very legally."},
{"name": "Metal Scrap", "type": "Material", "description": "Useless on it's own. Can be used to craft."},
{"name": "Glove", "type": "Valuable", "description": "Let's you pick up nails."},
{"name": "Nail", "type": "Material", "description": "Useless on it's own. Can be used to craft."},
{"name": "Battery", "type": "Material", "description": "This could be used to power something."},
{"name": "Key", "type": "Valuable", "description": "Used to open doors."},
{"name": "Machine", "type": "Miscellaneous", "description": "Creates keys from metal scraps and nails."}
]

north_top = " "
east_top = " "
east_bottom = " "
south_right = " "
south_left = " "
west_bottom = " "
west_top = " "

player_north = " "
player_north_north = " "
player_east = " "
player_south = " "
player_west = " "
player_middle = "X"

searched_east = False
searched_south = False
searched_west = False
searched_north = False
searched_north_north = False
searched_middle = False

machine_on = False
escaped = False
failed = False

direction = {"north", "east", "south", "west", "up", "right", "down", "left"}
INVENTORY_SIZE = 3

def player_move():
    global player_north, player_north_north, player_east, player_south, player_west, player_middle
    def player_reset():
        global player_north, player_north_north, player_east, player_south, player_west, player_middle
        player_north = " "
        player_north_north = " "
        player_east = " "
        player_south = " "
        player_west = " "
        player_middle = " "
    def valid_move():
        if direction == "north" or direction == "up" or direction == "u" or direction == "n":
            print("You move north.")
        elif direction == "east" or direction == "right" or direction == "r" or direction == "e":
            print("You move east.")
        elif direction == "south" or direction == "down" or direction == "d" or direction == "s":
            print("You move south.")
        elif direction == "west" or direction == "left" or direction == "l" or direction == "w":
            print("You move west.")
        show_map()
    if direction == "north" or direction == "up" or direction == "u" or direction == "n":
        if player_middle == "X":
            player_reset()
            player_north = "X"
            valid_move()
        elif player_south == "X":
            player_reset()
            player_middle = "X"
            valid_move()
        elif player_north == "X":
            print("The door ahead is locked. You need a key to enter.")
        else:
            print("You cannot move any further in this direction.")
    elif direction == "east" or direction == "right" or direction == "r" or direction == "e":
        if player_west == "X":
            player_reset()
            player_middle = "X"
            valid_move()
        elif player_middle == "X":
            player_reset()
            player_east = "X"
            valid_move()
        else:
            print("You cannot move any further in this direction.")
    elif direction == "south" or direction == "down" or direction == "d" or direction == "s":
        if player_north == "X":
            player_reset()
            player_middle = "X"
            valid_move()
        elif player_middle == "X":
            player_reset()
            player_south = "X"
            valid_move()
        elif player_north_north == "X":
            player_reset()
            player_north = "X"
            valid_move()
        else:
            print("You cannot move any further in this direction.")
    elif direction == "west" or direction == "left" or direction == "l" or direction == "w":
        if player_east == "X":
            player_reset()
            player_middle = "X"
            valid_move()
        elif player_middle == "X":
            player_reset()
            player_west = "X"
            valid_move()
        else:
            print("You cannot move any further in this direction.")
    else:
        print("Unknown command. Type 'help' to see available commands.")

def show_map():
      print(f"      ┌───────┐      \n"
            f"      │   {player_north_north} {north_top} │      \n"
            f"      ├──┄┄┄──┤      \n"
            f" ┌───┐┕━━┑{player_north}┍━━┙      \n"
            f" │ {west_top} └─┐ │ │ ┌─────┐ \n"
            f" │     ├─┘ └─┤{east_top}    │ \n"
            f" │  {player_west}     {player_middle}     {player_east}  │ \n"
            f" │   {west_bottom} ┝━┑ ┍━┥    {east_bottom}│ \n"
            f" ┕━━━━━┙ │ │ ┕━━━━━┙ \n"
            f"      ┌──┘ └──┐      \n"
            f"      │   {player_south}  {south_right}│      \n"
            f"      │{south_left}      │      \n"
            f"      ┕━━┅┅┅━━┙      \n")

def open_inventory():
    if len(inventory) == 0:
        print(f"You are not carrying anything. You can carry any {INVENTORY_SIZE} items.")
    else:
        print(f"You are carrying {len(inventory)}/{INVENTORY_SIZE} possible items:")
        for item in inventory:
            print(f"   {item['name']} ({item['type']}) - {item['description']}")

def search_room():
    if player_east == "X":
        global searched_east, east_top, east_bottom
        if not searched_east:
            searched_east = True
            print("You search the room and find a piece of METAL SCRAP (S), and a GLOVE (G).")
            east_top = "S"
            east_bottom = "G"
            show_map()
        else:
            print("You already searched this room!")
    if player_south == "X":
        global searched_south, south_left, south_right
        if not searched_south:
            searched_south = True
            print("You search the room and find a NAIL (N), and a BATTERY (B).")
            south_left = "N"
            south_right = "B"
            show_map()
        else:
            print("You already searched this room!")
    if player_west == "X":
        global searched_west, west_top, west_bottom
        if not searched_west:
            searched_west = True
            print("You search the room and find a big MACHINE (H), and a NAIL (N). The machine cannot be picked up.")
            west_top = "H"
            west_bottom = "N"
            show_map()
        else:
            print("You already searched this room!")
    if player_north == "X":
        global searched_north
        if not searched_north:
            searched_north = True
            print("You search the room and find nothing. You might have better luck inside the room ahead.")
        else:
            print("You already searched this room!")
    if player_north_north == "X":
        global searched_north_north, north_top
        if not searched_north_north:
            searched_north_north = True
            print("You search the room and find a big pile of MONEY (M).")
            north_top = "M"
            show_map()
        else:
            print("You already searched this room!")
    if player_middle == "X":
        global searched_middle
        if not searched_middle:
            searched_middle = True
            print("You search the room and find nothing.")
        else:
            print("You already searched this room!")

def pickup(item):
    if len(inventory) >= INVENTORY_SIZE:
        print("You cannot carry anything else right now. You must drop something first using 'drop <item>'.")
        return
    if player_east == "X":
        found_item = None
        for item_dict in room_east:
            if item_dict["name"].lower() == item:
                found_item = item_dict
                break
        if found_item is None or searched_east == False:
            print(f"You find no '{item}' in this room to pickup.")
            return
        if item == "nail":
            if not any(item_dict["name"].lower() == "glove" for item_dict in inventory):
                print("You need to wear gloves to pick up any nails.")
                return
        room_east.remove(found_item)
        inventory.append(found_item)
        print(f"You pick up the {found_item['name']}.")
        global east_top
        global east_bottom
        if item == "glove":
            if east_top == "G":
                east_top = "-"
                show_map()
                return
            if east_bottom == "G":
                east_bottom = "-"
                show_map()
                return
        if item == "key":
            if east_top == "K":
                east_top = "-"
                show_map()
                return
            if east_bottom == "K":
                east_bottom = "-"
                show_map()
                return
        if item == "battery":
            if east_top == "B":
                east_top = "-"
                show_map()
                return
            if east_bottom == "B":
                east_bottom = "-"
                show_map()
                return
        if item == "money":
            if east_top == "M":
                east_top = "-"
                show_map()
                return
            if east_bottom == "M":
                east_bottom = "-"
                show_map()
                return
        if item == "nail":
            if east_top == "N":
                east_top = "-"
                show_map()
                return
            if east_bottom == "N":
                east_bottom = "-"
                show_map()
                return
        if item == "metal scrap":
            if east_top == "S":
                east_top = "-"
                show_map()
                return
            if east_bottom == "S":
                east_bottom = "-"
                show_map()
                return
        if item == "fake money":
            if east_top == "F":
                east_top = "-"
                show_map()
                return
            if east_bottom == "F":
                east_bottom = "-"
                show_map()
                return
    if player_south == "X":
        found_item = None
        for item_dict in room_south:
            if item_dict["name"].lower() == item:
                found_item = item_dict
                break
        if found_item is None or searched_south == False:
            print(f"You find no '{item}' in this room to pickup.")
            return
        if item == "nail":
            if not any(item_dict["name"].lower() == "glove" for item_dict in inventory):
                print("You need to wear gloves to pick up any nails.")
                return
        room_south.remove(found_item)
        inventory.append(found_item)
        print(f"You pick up the {found_item['name']}.")
        global south_left
        global south_right
        if item == "glove":
            if south_left == "G":
                south_left = "-"
                show_map()
                return
            if south_right == "G":
                south_right = "-"
                show_map()
                return
        if item == "key":
            if south_left == "K":
                south_left = "-"
                show_map()
                return
            if south_right == "K":
                south_right = "-"
                show_map()
                return
        if item == "battery":
            if south_left == "B":
                south_left = "-"
                show_map()
                return
            if south_right == "B":
                south_right = "-"
                show_map()
                return
        if item == "money":
            if south_left == "M":
                south_left = "-"
                show_map()
                return
            if south_right == "M":
                south_right = "-"
                show_map()
                return
        if item == "nail":
            if south_left == "N":
                south_left = "-"
                show_map()
                return
            if south_right == "N":
                south_right = "-"
                show_map()
                return
        if item == "metal scrap":
            if south_left == "S":
                south_left = "-"
                show_map()
                return
            if south_right == "S":
                south_right = "-"
                show_map()
                return
        if item == "fake money":
            if south_left == "F":
                south_left = "-"
                show_map()
                return
            if south_right == "F":
                south_right = "-"
                show_map()
                return
    if player_west == "X":
        found_item = None
        for item_dict in room_west:
            if item_dict["name"].lower() == item:
                found_item = item_dict
                break
        if found_item is None or searched_west == False:
            print(f"You find no '{item}' in this room to pickup.")
            return
        if item == "nail":
            if not any(item_dict["name"].lower() == "glove" for item_dict in inventory):
                print("You need to wear gloves to pick up any nails.")
                return
        room_west.remove(found_item)
        inventory.append(found_item)
        print(f"You pick up the {found_item['name']}.")
        global west_bottom
        if item == "glove":
            if west_bottom == "G":
                west_bottom = "-"
                show_map()
                return
        if item == "key":
            if west_bottom == "K":
                west_bottom = "-"
                show_map()
                return
        if item == "battery":
            if west_bottom == "B":
                west_bottom = "-"
                show_map()
                return
        if item == "money":
            if west_bottom == "M":
                west_bottom = "-"
                show_map()
                return
        if item == "nail":
            if west_bottom == "N":
                west_bottom = "-"
                show_map()
                return
        if item == "metal scrap":
            if west_bottom == "S":
                west_bottom = "-"
                show_map()
                return
        if item == "fake money":
            if west_bottom == "F":
                west_bottom = "-"
                show_map()
                return
    if player_north_north == "X":
        found_item = None
        for item_dict in room_north:
            if item_dict["name"].lower() == item:
                found_item = item_dict
                break
        if found_item is None or searched_north_north == False:
            print(f"You find no '{item}' in this room to pickup.")
            return
        if item == "nail":
            if not any(item_dict["name"].lower() == "glove" for item_dict in inventory):
                print("You need to wear gloves to pick up any nails.")
                return
        room_north.remove(found_item)
        inventory.append(found_item)
        print(f"You pick up the {found_item['name']}.")
        show_map()
        global north_top
        if item == "glove":
            if north_top == "G":
                north_top = "-"
                show_map()
                return
        if item == "key":
            if north_top == "K":
                north_top = "-"
                show_map()
                return
        if item == "battery":
            if north_top == "B":
                north_top = "-"
                show_map()
                return
        if item == "money":
            if north_top == "M":
                north_top = "-"
                show_map()
                return
        if item == "nail":
            if north_top == "N":
                north_top = "-"
                show_map()
                return
        if item == "metal scrap":
            if north_top == "S":
                north_top = "-"
                show_map()
                return
        if item == "fake money":
            if north_top == "F":
                north_top = "-"
                show_map()
                return

def drop(item):
    if player_east == "X":
        held_item = None
        for item_dict in inventory:
            if item_dict["name"].lower() == item:
                held_item = item_dict
                break
        if held_item is None:
            print(f"You don't have a '{item}'.")
            return
        if not searched_east:
            print(f"You find nowhere to drop the {held_item['name']}.")
            return
        global east_top
        global east_bottom
        if east_top == "-":
            room_east.append(held_item)
            inventory.remove(held_item)
            print(f"You dropped up the {held_item['name']}.")
            if item == "glove":
                east_top = "G"
                show_map()
                return
            if item == "key":
                east_top = "K"
                show_map()
                return
            if item == "battery":
                east_top = "B"
                show_map()
                return
            if item == "money":
                east_top = "M"
                show_map()
                return
            if item == "nail":
                east_top = "N"
                show_map()
                return
            if item == "metal scrap":
                east_top = "S"
                show_map()
                return
            if item == "fake money":
                east_top = "F"
                show_map()
                return
        elif east_bottom == "-":
            room_east.append(held_item)
            inventory.remove(held_item)
            print(f"You dropped up the {held_item['name']}.")
            if item == "glove":
                east_bottom = "G"
                show_map()
                return
            if item == "key":
                east_bottom = "K"
                show_map()
                return
            if item == "battery":
                east_bottom = "B"
                show_map()
                return
            if item == "money":
                east_bottom = "M"
                show_map()
                return
            if item == "nail":
                east_bottom = "N"
                show_map()
                return
            if item == "metal scrap":
                east_bottom = "S"
                show_map()
                return
            if item == "fake money":
                east_bottom = "F"
                show_map()
                return
        else:
            print(f"You find nowhere to drop the {held_item['name']}.")
    if player_south == "X":
        held_item = None
        for item_dict in inventory:
            if item_dict["name"].lower() == item:
                held_item = item_dict
                break
        if held_item is None:
            print(f"You don't have a '{item}'.")
            return
        if not searched_south:
            print(f"You find nowhere to drop the {held_item['name']}.")
            return
        global south_left
        global south_right
        if south_left == "-":
            room_south.append(held_item)
            inventory.remove(held_item)
            print(f"You dropped up the {held_item['name']}.")
            if item == "glove":
                south_left = "G"
                show_map()
                return
            if item == "key":
                south_left = "K"
                show_map()
                return
            if item == "battery":
                south_left = "B"
                show_map()
                return
            if item == "money":
                south_left = "M"
                show_map()
                return
            if item == "nail":
                south_left = "N"
                show_map()
                return
            if item == "metal scrap":
                south_left = "S"
                show_map()
                return
            if item == "fake money":
                south_left = "F"
                show_map()
                return
        elif south_right == "-":
            room_south.append(held_item)
            inventory.remove(held_item)
            print(f"You dropped up the {held_item['name']}.")
            if item == "glove":
                south_right = "G"
                show_map()
                return
            if item == "key":
                south_right = "K"
                show_map()
                return
            if item == "battery":
                south_right = "B"
                show_map()
                return
            if item == "money":
                south_right = "M"
                show_map()
                return
            if item == "nail":
                south_right = "N"
                show_map()
                return
            if item == "metal scrap":
                south_right = "S"
                show_map()
                return
            if item == "fake money":
                south_right = "F"
                show_map()
                return
        else:
            print(f"You find nowhere to drop the {held_item['name']}.")
    if player_west == "X":
        held_item = None
        for item_dict in inventory:
            if item_dict["name"].lower() == item:
                held_item = item_dict
                break
        if held_item is None:
            print(f"You don't have a '{item}'.")
            return
        if not searched_west:
            print(f"You find nowhere to drop the {held_item['name']}.")
            return
        global west_top
        global west_bottom
        if west_bottom == "-":
            room_west.append(held_item)
            inventory.remove(held_item)
            print(f"You dropped up the {held_item['name']}.")
            if item == "glove":
                west_bottom = "G"
                show_map()
                return
            if item == "key":
                west_bottom = "K"
                show_map()
                return
            if item == "battery":
                west_bottom = "B"
                show_map()
                return
            if item == "money":
                west_bottom = "M"
                show_map()
                return
            if item == "nail":
                west_bottom = "N"
                show_map()
                return
            if item == "metal scrap":
                west_bottom = "S"
                show_map()
                return
            if item == "fake money":
                west_bottom = "F"
                show_map()
                return
        else:
            print(f"You find nowhere to drop the {held_item['name']}.")
    if player_north == "X":
        held_item = None
        for item_dict in inventory:
            if item_dict["name"].lower() == item:
                held_item = item_dict
                break
        if held_item is None:
            print(f"You find nowhere to drop the '{item}'.")
        else:
            print(f"You find nowhere to drop the {held_item['name']}.")
        return
    if player_north_north == "X":
        held_item = None
        for item_dict in inventory:
            if item_dict["name"].lower() == item:
                held_item = item_dict
                break
        if held_item is None:
            print(f"You don't have a '{item}'.")
            return
        if not searched_north_north:
            print(f"You find nowhere to drop the {held_item['name']}.")
            return
        global north_top
        if north_top == "-":
            room_north.append(held_item)
            inventory.remove(held_item)
            print(f"You dropped up the {held_item['name']}.")
            if item == "glove":
                north_top = "G"
                show_map()
                return
            if item == "key":
                north_top = "K"
                show_map()
                return
            if item == "battery":
                north_top = "B"
                show_map()
                return
            if item == "money":
                north_top = "M"
                show_map()
                return
            if item == "nail":
                north_top = "N"
                show_map()
                return
            if item == "metal scrap":
                north_top = "S"
                show_map()
                return
            if item == "fake money":
                north_top = "F"
                show_map()
                return
        else:
            held_item = None
            for item_dict in inventory:
                if item_dict["name"].lower() == item:
                    held_item = item_dict
                    break
            if held_item is None:
                print(f"You find nowhere to drop the '{item}'.")
            else:
                print(f"You find nowhere to drop the {held_item['name']}.")

def use(item): # This has been updated, the last version accidentally searched in 'everything' and not in 'inventory',
               # so players could use items without having them in their inventory.
    held_item = None
    global player_south, player_west, player_north, player_north_north
    if item == "machine":
        held_item = {"name": "Machine"} # Because the item is now looked for in the inventory, using the machine won't work.
                                        # This temporarily tricks the function into thinking you have the machine in your inventory.
    for item_dict in inventory:
        if item_dict["name"].lower() == item:
            held_item = item_dict
            break
    if held_item is None:
        print(f"You don't have a '{item}' to use.")
        return
    if player_west == "X":
        global machine_on
        if item == "machine":
            if machine_on:
                if (sum(1 for d in inventory if d["name"].lower() == "nail") >= 2 and
                    any(d["name"].lower() == "metal scrap" for d in inventory)):
                        print("You successfully crafted a KEY. You grab the key.")
                        inventory.append({"name": "Key", "type": "Valuable", "description": "Used to open doors."})
                        inventory.remove({"name": "Metal Scrap", "type": "Material", "description": "Useless on it's own. Can be used to craft."})
                        inventory.remove({"name": "Nail", "type": "Material", "description": "Useless on it's own. Can be used to craft."})
                        inventory.remove({"name": "Nail", "type": "Material", "description": "Useless on it's own. Can be used to craft."})
                        return
                else:
                    print("To use the big (mysterious) machine, you need a NAIL, a METAL SCRAP, and another NAIL.")
                    return
            else:
                print("You need to power the machine with a battery before using it.")
                return
        elif item == "battery":
            if not machine_on:
                print("You power the machine with the battery. You no longer have a battery.")
                machine_on = True
                inventory.remove(held_item)
                return
        else:
            held_item = None
            for item_dict in inventory:
                if item_dict["name"].lower() == item:
                    held_item = item_dict
                    break
            if held_item is None:
                print(f"You find no use for the '{item}'.")
            else:
                print(f"You find no use for the {held_item['name']}.")
            return
    if player_south == "X":
        global escaped, failed, escaping, start_time, end_time, final_time
        if item == "key":
            if any(d["name"].lower() == "key" for d in inventory):
                if any(d["name"].lower() == "money" for d in inventory):
                    if north_top == "F":
                        escaped = True
                        escaping = False
                        end_time = time.time()
                        final_time = end_time - start_time
                        final_time = int(final_time)
                        print(f"You escape with the money in {final_time} seconds, and no one suspects a thing!")
                        print("\n"
                              "┌─────────┐ \n"
                              "│ YOU WIN │ \n"
                              "┕━━━━━━━━━┙ \n"
                              "\n"
                              "Thank you for playing! \n"
                              "Save your score to the local leaderboard by typing 'save score'! \n"
                              "Play again by typing 'restart'.")
                        return
                    else:
                        failed = True
                        print("You forgot to replace the money with the fake money. You were caught!")
                        print("\n"
                              "┌────────────┐ \n"
                              "│ YOU FAILED │ \n"
                              "┕━━━━━━━━━━━━┙ \n"
                              "\n"
                              "Play again by typing 'restart'.")
                        return
                print("You have no reason to leave yet. You still don't have the money!")
                return
    if player_north == "X":
        if item == "key":
            if any(d["name"].lower() == "key" for d in inventory):
                print("You use the key to get through the door.")
                player_north = " "
                player_north_north = "X"
                show_map()
                return
    if player_north_north == "X":
        if item == "key":
            if any(d["name"].lower() == "key" for d in inventory):
                print("You use the key to get through the door.")
                player_north_north = " "
                player_north = "X"
                show_map()
                return
    else:
        held_item = None
        for item_dict in inventory:
            if item_dict["name"].lower() == item:
                held_item = item_dict
                break
        if held_item is None:
            print(f"You find no use for the '{item}'.")
        else:
            print(f"You find no use for the {held_item['name']}.")
        return

def restart():
    global room_north, room_east, room_south, room_west
    global north_top, east_top, east_bottom, south_right, south_left, west_bottom, west_top
    global player_north, player_north_north, player_east, player_south, player_west, player_middle
    global searched_east, searched_south, searched_west, searched_north, searched_north_north, searched_middle
    global machine_on, escaped, failed, inventory, everything

    global escaping
    escaping = False

    inventory = [
        {"name": "Fake Money", "type": "Valuable", "description": "Can fool anyone as real money. Should be used."}
    ]
    room_north = [
        {"name": "Money", "type": "Valuable", "description": "Obtained very legally."}
    ]
    room_east = [
        {"name": "Metal Scrap", "type": "Material", "description": "Useless on it's own. Can be used to craft."},
        {"name": "Glove", "type": "Valuable", "description": "Let's you pick up nails."}
    ]
    room_south = [
        {"name": "Nail", "type": "Material", "description": "Useless on it's own. Can be used to craft."},
        {"name": "Battery", "type": "Material", "description": "This could be used to power something."}
    ]
    room_west = [
        {"name": "Nail", "type": "Material", "description": "Useless on it's own. Can be used to craft."}
    ]
    everything = [
        {"name": "Fake Money", "type": "Valuable", "description": "Can fool anyone as real money. Should be used."},
        {"name": "Money", "type": "Valuable", "description": "Obtained very legally."},
        {"name": "Metal Scrap", "type": "Material", "description": "Useless on it's own. Can be used to craft."},
        {"name": "Glove", "type": "Valuable", "description": "Let's you pick up nails."},
        {"name": "Nail", "type": "Material", "description": "Useless on it's own. Can be used to craft."},
        {"name": "Battery", "type": "Material", "description": "This could be used to power something."},
        {"name": "Key", "type": "Valuable", "description": "Used to open doors."},
        {"name": "Machine", "type": "Miscellaneous", "description": "Creates keys from metal scraps and nails."}
    ]
    north_top = " "
    east_top = " "
    east_bottom = " "
    south_right = " "
    south_left = " "
    west_bottom = " "
    west_top = " "
    player_north = " "
    player_north_north = " "
    player_east = " "
    player_south = " "
    player_west = " "
    player_middle = "X"
    searched_east = False
    searched_south = False
    searched_west = False
    searched_north = False
    searched_north_north = False
    searched_middle = False
    machine_on = False
    escaped = False
    failed = False
    game_loop()

def shortcut_names(typed_name):
    shortcuts = {
        "g": "glove",
        "n": "nail",
        "f": "fake money",
        "scrap": "metal scrap",
        "s": "metal scrap",
        "b": "battery",
        "k": "key",
        "m": "money",
        "h": "machine"
    }
    return shortcuts.get(typed_name.lower(), typed_name)

def are_you_escaping():
    global escaping, start_time
    if not escaping:
        escaping = True
        if DEBUG:
            start_time = time.time() - 8000
        else:
            start_time = time.time()

def load_scores():
    rows = []
    fieldnames = ["Time", "Name"]
    if not os.path.exists("heist_scoreboard.csv"): # This was made with help from Gemini, using the logic we used in class, but using OS to check if the file exists.
                                                   # I worked with Gemini for this whole section, but tried to keep the code simple enough for me to understand.
        with open("heist_scoreboard.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(5):
                writer.writerow({"Time": "9999", "Name": "N/A"})
            return [{"Time": "9999", "Name": "Empty"} for _ in range(5)] # This returns the scoreboard values if no scoreboard exists yet.
    with open("heist_scoreboard.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def save_score():
    global final_time
    save_name = ""
    while save_name == "" or len(save_name) > 8: # This system was taken and adapted from my week 2 exercise.
        save_name = input("Please enter your name: ")
        if save_name == "":
            print("You must enter a name to continue!")
        if len(save_name) > 8:
            print("Your name cannot be longer than 8 characters!")
    final_time = int(final_time)
    rows = load_scores()
    if final_time < int(rows[4]["Time"]): # Originally I used a long if-statement if you made it onto the scoreboard,
                                          # Gemini helped create this idea, adding your score regardless of what you got,
                                          # then sorting by the time, and finally cutting the rows off at 5. If your
                                          # score was high enough, it automatically sorts into the scoreboard.
        new_row = {"Time": str(final_time), "Name": save_name}
        rows.append(new_row)
        rows.sort(key=lambda row: int(row["Time"])) # I can't take any credit here; this was all Gemini.
        rows = rows[:5]
        fieldnames = ["Time", "Name"]
        with open("heist_scoreboard.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        scoreboard()
    else:
        print(f"Your time of {final_time} seconds was not fast enough to get on the leaderboard! Type 'scoreboard' to see all scores.")

def scoreboard(): # Here I think I could use load_scores(), but wanted to try using the except error.
    try:
        with open("heist_scoreboard.csv", "r") as f:
            reader = csv.DictReader(f)
            rows = []
            for row in reader:
                rows.append(row)
            print("SCOREBOARD:") # Printing the scoreboard could probably be simpler using loops, but this is
                                 # already complicated enough for me. This does however lock the scoreboard
                                 # to always be 5 rows long.
            print(f"1. {rows[0]['Time']}s | {rows[0]['Name']}")
            print(f"2. {rows[1]['Time']}s | {rows[1]['Name']}")
            print(f"3. {rows[2]['Time']}s | {rows[2]['Name']}")
            print(f"4. {rows[3]['Time']}s | {rows[3]['Name']}")
            print(f"5. {rows[4]['Time']}s | {rows[4]['Name']}")
    except FileNotFoundError:
        print("The scoreboard file has not been found. Submit a score to create the heist_scoreboard.csv file.")

# GAME LOOP

def game_loop():
    global DEBUG
    if DEBUG:
        global north_top, start_time, inventory
        north_top = "F"
        start_time = time.time() - 8000
        inventory.append({"name": "Money", "type": "Valuable", "description": "Obtained very legally."})
        inventory.remove({"name": "Fake Money", "type": "Valuable", "description": "Can fool anyone as real money. Should be used."})
        inventory.append({"name": "Key", "type": "Valuable", "description": "Used to open doors."})
        print("Welcome player! You have been contracted to steal money from an unmarked building. \n"
              "You have limited inventory space, so you need to play smart! \n"
              "You have been given the following: \n"
              "\n"
              "┌─────────────────────────────────────────────────────────────────────┐ \n"
              "│ INFORMATION:                                                        │ \n"
              "│ Type 'help' to open a list of commands.                             │ \n"
              "│ You already have something in your inventory. Check it out!         │ \n"
              "│ Doors are represented with a ┄┄. There might be a way to open them. │ \n"
              "┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙ \n"
              "\n"
              "Type 'help' and 'map' to get started. \n"
              "Good luck! \n"
              "The timer begins the second you enter your first command. \n"
              "\n"
              "┌──────────────────────────────────────────────────────────────────────────────────────────────┐ \n"
              "│ WARNING! DEBUG MODE IS ENABLED!                                                              │ \n"
              "│ To complete the game in DEBUG MODE, simply leave the building (you already have the money).  │ \n"
              "│ To do this, type 'go south' and then 'use key'.                                              │ \n"
              "│ Debug mode automatically adds 8000 seconds to any run, to prevent faked runs.                │ \n"
              "│ To toggle DEBUG MODE on and off, type 'debug'. This resets all progress and acts as 'reset'. │ \n"
              "┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙")

    if not DEBUG:
        print("Welcome player! You have been contracted to steal money from an unmarked building. \n"
              "You have limited inventory space, so you need to play smart! \n"
              "You have been given the following: \n"
              "\n"
              "┌─────────────────────────────────────────────────────────────────────┐ \n"
              "│ INFORMATION:                                                        │ \n"
              "│ Type 'help' to open a list of commands.                             │ \n"
              "│ You already have something in your inventory. Check it out!         │ \n"
              "│ Doors are represented with a ┄┄. There might be a way to open them. │ \n"
              "┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙ \n"
              "\n"
              "Type 'help' and 'map' to get started. \n"
              "Good luck! \n"
              "The timer begins the second you enter your first command. \n")

    while True:
        if escaped == False and failed == False:
            command = input("\n> ").strip().lower()
            global direction
            match command.split():
                case ["help"]:
                    are_you_escaping()
                    print("Here is a list of all commands: \n"
                          "\n"
                          "┌───────────────────────────────────────────────────────────┐ \n"
                          "│ help           |                   Displays this message. │ \n"
                          "│ inventory      |                 Displays your inventory. │ \n"
                          "│ go <direction> |             Move in any given direction. │ \n"
                          "│ map            |                        Displays the map. │ \n"
                          "│ search         |     Searches the current room for items. │ \n"
                          "│ pickup <item>  |              Picks up an item in a room. │ \n"
                          "│ drop <item>    | Drops selected item from your inventory. │ \n"
                          "│ use <item>     |                Uses an item if possible. │ \n"
                          "│ restart        |                       Restarts the game. │ \n"
                          "│ scoreboard     |            Displays the game scoreboard. │ \n"
                          "┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙ \n"
                          "\n"
                          "Keep in mind, abbreviations for directions can be used (north → n, right → r). \n"
                          "This also works for items and their letter on the map (nail → n, machine → h).")
                case ["map"]:
                    are_you_escaping()
                    show_map()
                case ["go", direction]:
                    are_you_escaping()
                    player_move()
                case ["inv"]:
                    are_you_escaping()
                    open_inventory()
                case ["inventory"]:
                    are_you_escaping()
                    open_inventory()
                case ["search"]:
                    are_you_escaping()
                    search_room()
                case ["pickup", *item_words]:
                    are_you_escaping()
                    typed_item = " ".join(item_words)
                    item = shortcut_names(typed_item)
                    pickup(item)
                case ["drop", *item_words]:
                    are_you_escaping()
                    typed_item = " ".join(item_words)
                    item = shortcut_names(typed_item)
                    drop(item)
                case ["use", *item_words]:
                    are_you_escaping()
                    typed_item = " ".join(item_words)
                    item = shortcut_names(typed_item)
                    use(item)
                case ["restart"]:
                    restart()
                case ["scoreboard"]:
                    scoreboard()
                case ["debug"]:
                    if DEBUG:
                        DEBUG = False
                        print("DEBUG: Debug mode disabled.")
                        restart()
                        return
                    if not DEBUG:
                        DEBUG = True
                        print("DEBUG: Debug mode enabled.")
                        restart()
                        return
                case _:
                    print("Unknown command. Type 'help' to see available commands.")
        else:
            command = input("\n> ").strip().lower()
            match command.split():
                case ["restart"]:
                    restart()
                case ["scoreboard"]:
                    scoreboard()
                case ["debug"]:
                    if DEBUG:
                        DEBUG = False
                        restart()
                        return
                    if not DEBUG:
                        DEBUG = True
                        restart()
                        return
                case ["save", "score"]: # Split this with Gemini, so a multiple word command is accepted.
                    if escaped:
                        save_score()
                    else:
                        print("Unknown command. Type 'help' to see available commands.")
                case _:
                    print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()

# For this weeks task I did need to consult with Gemini a lot, and needed help coming up with the logic for the scoreboard.
# But everything should work properly, and I am happy with how the scoreboard works.
# There shouldn't be any bugs, and saving a score should only work when you successfully escaped.
# My best time is 40 seconds.
# ദ്ദി◝ ⩊ ◜.ᐟ
