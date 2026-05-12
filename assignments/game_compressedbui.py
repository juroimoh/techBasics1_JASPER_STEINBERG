import time
import random
import sys

# This is a very basic dungeon escape.

# For the week 5 task, I put a lot of repetitive code segments into functions (see below), and reworked the choice options.
# The entire logic behind main(), along with defining variables as global was done with help from Gemini, since I had no idea how to implement a main() function.
# I feel like this project is still small enough to benefit from global variables, and would be a lot of work to change, especially if I have no plans of expanding this.
# Additionally, made small tweaks and improvements since the last release.

# What can be modularized as a function?
#   All the functions below!
# What makes sense to be defined as local/global variables?
#   Mentioned above, currently no local functions used (except num1 and num2 for the gremlin riddle).
# Which data type fits your variable better?
#   For the choices, I could use int(input()) but, that would require swapping everything, which feels unnecessary because it works just fine how it is and isn't any more complicated.
# How can you structure your code so that it is easier/faster for someone to grasp what is going on? (for example, break down your code into multiple scenes)
#   Easiest would be for someone to read through, since I think everything is easy to follow, with decision = X and then the story for X playing out underneath.
# Is it easier to test and debug your code now?
#   Not sure. Might be more difficult because some things are moved around (such as items in functions), and since global variables are used they have to be called in the functions too which might complicate things.

health = 75
decision = 0
chance = 0
candy = 0
rock = 0
gremlin_fight = 0
skipgrem = 0
sword = 0
gremlin_encounter = "No"
sword_encounter = "No"
candy_encounter = "No"
swings = 0
orc_slip = 0
name = ""
orc_health = 70
choice = 0

# FUNCTIONS
def type(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.0001)
    print()
# Used a tutorial to create a typewriter effect (segment above).

def find_candy():
    global candy, health
    print("┌────┐ \n"
          "│ 🍬 │ \n"
          "└────┘")
    time.sleep(1)
    if candy == 0:
        type("What's that doing here?")
        time.sleep(1)
        candy = 1
    chance = random.randint(10, 25)
    type(f"You eat it and receive {chance} health.")
    health += chance

def orc_battle_health():
    if health < 10 and orc_health < 10:
        print("┌─────────────────┐ \n"
              f"│ {health}            {orc_health}  │ \n"
              "│ 🧍           👹 │ \n"
              "└─────────────────┘")
    elif health < 10 and orc_health > 9:
        print("┌─────────────────┐ \n"
              f"│ {health}            {orc_health} │ \n"
              "│ 🧍           👹 │ \n"
              "└─────────────────┘")
    elif health > 9 and orc_health < 10:
        print("┌─────────────────┐ \n"
              f"│ {health}           {orc_health}  │ \n"
              "│ 🧍           👹 │ \n"
              "└─────────────────┘")
    else:
        print("┌─────────────────┐ \n"
              f"│ {health}           {orc_health} │ \n"
              "│ 🧍           👹 │ \n"
              "└─────────────────┘")

def find_rock():
    global rock
    chance = random.randint(1, 7)
    if chance == 1:
        type("You spot a rock on the floor.")
        time.sleep(1)
        print("┌────┐ \n"
              "│ 🌑 │ \n"
              "└────┘")
        time.sleep(1)
        type("You grab it quickly. [+1 Rock]")
        rock += 1
        time.sleep(1)

def game_over():
    if health <= 0:
        print("┌───────────┐ \n"
              "│ GAME OVER │ \n"
              "└───────────┘")
        time.sleep(5)
        sys.exit()

def options(*valid_options): # Very happy with this. It simplifies the option system, and is scalable with the amount of options (choice = options("1", "2", "3", "4" etc.).
    while True:
        answer = input("Input your choice: ")
        if answer in valid_options:
            return answer
        else:
            print("Please enter a valid number.")

def main():
    global name, health, choice, decision, rock, skipgrem, orc_slip, candy, sword, swings, gremlin_fight, gremlin_encounter, candy_encounter, sword_encounter, orc_health

    print("┌────────────────┐ \n"
          "│  MINI DUNGEON  │ \n"
          "│      v0.2      │ \n"
          "└────────────────┘ made by jasper")
    time.sleep(2)
    while name == "":
        name = input("Please enter your name: ")
        if name == "":
            print("You must enter a name to begin!")
    # Used Gemini to generate code segment above to require a name input.
    time.sleep(1)
    type(f"You wake up.")
    time.sleep(1)
    type(f"Your name is {name}. That's all you remember.")
    # Original output was print("Your name is", name,", at least that's what you remember.")
    # This led to a space between the name and the comma, which was unwanted.
    # Used Gemini to correct code, using print(f"aaa {name} aaa") instead.

    time.sleep(1)
    type(f"You have {health} health.\n")
    time.sleep(1)
    type("You find yourself in a dungeon, with no clear way out.")
    time.sleep(1)
    type("It's dark, with only a few torches lighting up the room.")
    time.sleep(1)
    type("You spot two corridors. The first has a chest in the distance, and the second leads far away.")
    time.sleep(1)
    print("┌───────────────────────────────┐ \n"
          "│ OPTIONS:                      │ \n"
          "│ Search the room (1)           │ \n"
          "│ Enter the first corridor (2)  │ \n"
          "│ Enter the second corridor (3) │ \n"
          "└───────────────────────────────┘")

    choice = options("1", "2", "3")

    if choice == "1":
        decision = 1
    elif choice == "2":
        type("You enter the corridor with the chest.")
        decision = 2
    elif choice == "3":
        type("You stumble down the second corridor.")
        decision = 3

    time.sleep(1)

    if decision == 1:
        chance = random.randint(1, 2)
        if chance == 1:
            type("You search the dimly lit room and find a piece of candy.")
            time.sleep(1)
            find_candy()
        elif chance == 2:
            type("You search the room and find nothing.")

        time.sleep(1)
        type("All of a sudden you hear a loud crash...")
        time.sleep(1)
        type("The first corridor leading to the chest has caved in.")
        time.sleep(1)

        print("┌───────────────────────────────────────────┐ \n"
              "│ OPTIONS:                                  │ \n"
              "│ Clear the rocks to the first corridor (1) │ \n"
              "│ Enter the second corridor (2)             │ \n"
              "└───────────────────────────────────────────┘")

        choice = options("1", "2")

        if choice == "1":
            type("You try clearing the rocks.")
            time.sleep(1)
            type("You fail.")
            time.sleep(1)
            type("Of course you fail.")
            time.sleep(1)
            type("You're not that strong.")
            time.sleep(1)
            chance = random.randint(5, 10)
            type(f"In fact, you take {chance} damage.")
            health -= chance
            time.sleep(1)
            type(f"With {health} health remaining, and decide to enter the second corridor instead.")
            time.sleep(1)
            decision = 3
        elif choice == "2":
            type("You slowly stumble down the second corridor.")
            time.sleep(1)
            decision = 3

    if decision == 2:
        chance = random.randint(1, 3)
        if chance == 1:
            type("Inside the chest you find a sharp rock. Ouch.")
            time.sleep(1)
            print("┌────┐ \n"
                  "│ 🌑 │ \n"
                  "└────┘")
            time.sleep(1)
            type("You pocket it. [+1 Rock]")
            rock += 1
        elif chance == 2:
            type("Inside the chest you find a piece of candy.")
            time.sleep(1)
            find_candy()
        elif chance == 3:
            type("You find nothing inside.")
        time.sleep(1)
        type("You head back to the room you woke up in.")
        time.sleep(1)

        print("┌───────────────────────────────┐ \n"
              "│ OPTIONS:                      │ \n"
              "│ Enter the second corridor (1) │ \n"
              "└───────────────────────────────┘")

        choice = options("1")

        if choice == "1":
            type("You begin heading down the second corridor.")
            time.sleep(1)
            decision = 3

    if decision == 3:
        type("Soon you spot a light in the distance.")
        time.sleep(1)
        type("Upon approaching, you realize there's something glowing on the ground.")
        chance = random.randint(1, 2)
        if chance == 1:
            time.sleep(1)
            type("It's a rock. Weird.")
            time.sleep(1)
            print("┌────┐ \n"
                  "│ 🌕 │ ← glowing\n"
                  "└────┘")
            time.sleep(1)
            type("You pocket it, just incase. [+1 Rock]")
            rock += 1
            time.sleep(1)
            type("You continue walking.")
            decision = 6
        elif chance == 2:
            time.sleep(1)
            type("It's a small gremlin!")
            time.sleep(2)
            chance = random.randint(1, 5)
            gremlin_encounter = "Yes"
            gremlin_health = 9
            if chance > 2:
                type(f'"{name}!?" the gremlin yells. "What are you doing down here?"')
                time.sleep(1)
                print("┌─────────────────────────────────────────────────────┐ \n"
                      "│ OPTIONS:                                            │ \n"
                      '│ "I just woke up here. Do you know the way out?" (1) │ \n'
                      '│ "Wait, who are you? Why do you know my name?" (2)   │ \n'
                      "└─────────────────────────────────────────────────────┘")

                choice = options("1", "2")

                if choice == "1":
                    type('"I just woke up here. Do you know the way out?" you ask.')
                    time.sleep(1)
                    type("The gremlin looks at you funny.")
                    time.sleep(1)
                    type('"You doubt my abilities?"')
                    time.sleep(1)
                    type('"Of course I know the way out, just keep going straight."')
                    time.sleep(1)
                    type('"But to pass, you must first answer my riddle!"')
                    time.sleep(1)
                    type("You pause.")
                    num1 = random.randint(3, 9)
                    num2 = random.randint(2, 9)
                    time.sleep(1)
                    type(f'"If I have {num2} golden coins-..."')
                    time.sleep(1)
                    type(f'"Wait.. no that\'s wrong."')
                    time.sleep(1)
                    type(
                        f'"If I have {num1} magical potions which each sell for {num2} coins, how many coins do I get if I sell all but one?"')
                    time.sleep(1)
                    print("┌─────────────────────────────────────────────────────┐ \n"
                          "│ INPUT:                                              │ \n"
                          '│ Answer the riddle! A wrong answer will be punished. │ \n'
                          "└─────────────────────────────────────────────────────┘")
                    choice = int(input("Input your answer: "))
                    num1 -= 1
                    num3 = num1 * num2
                    if choice == num3:
                        type('"Wow uhh, I should have picked something harder."')
                        time.sleep(1)
                        type('"You win! Yes, simply continue through and you shall reach the exit."')
                        time.sleep(1)
                        type("The gremlin tosses you a piece of candy.")
                        time.sleep(1)
                        print("┌────┐ \n"
                              "│ 🍬 │ \n"
                              "└────┘")
                        time.sleep(1)
                        if candy == 0:
                            type("You wonder why he has candy.")
                            time.sleep(1)
                            candy = 1
                        chance = random.randint(10, 25)
                        type(f"You eat it and receive {chance} health.")
                        health += chance
                        time.sleep(1)
                        type(f'"Farewell, {name}."')
                    else:
                        type('"BWAHAHWAHA!! You are wrong!"')
                        time.sleep(1)
                        type(f'"Now {name}, you must defeat me!"')
                        chance = 2
                        skipgrem = 1
                if choice == "2":
                    type('"Wait, who are you? Why do you know my name?" you ask.')
                    time.sleep(1)
                    type("The gremlin looks up at you.")
                    time.sleep(1)
                    type('"You..."')
                    time.sleep(1)
                    type('"You don\'t remember me?"')
                    time.sleep(1)
                    type("The gremlin looks mad.")
                    time.sleep(1)
                    type("Very mad.")
                    time.sleep(1)
                    type('"How dare you forget about me!"')
                    time.sleep(1)
                    type('"YOU PROMISED YOU WOULD REMEMBER!"')
                    time.sleep(2)
                    shouting_name = name.upper()
                    # Used Gemini to figure out how to convert a string to all uppercase.
                    # I think we went over this in class, but I didn't remember how.
                    type(f'"{shouting_name} YOU PROMISED!!"')
                    chance = 2
                    skipgrem = 1

            if chance < 3:
                if skipgrem == 1:
                    time.sleep(1)
                else:
                    type(f'"I am the evil gremlin!" the (evil) gremlin says.')
                    time.sleep(1)
                    type('"To continue down this path, you must defeat me!"')
                    time.sleep(2)

                if rock > 1:
                    type(f"You prepare to fight. You have {rock} rocks.")
                elif rock == 1:
                    type(f"You prepare to fight. You have {rock} rock.")
                else:
                    type(f"You prepare to fight. You have no rocks.")
                time.sleep(1)
                if health < 10:
                    print("┌─────────────────┐ \n"
                          f"│ {health}             {gremlin_health} │ \n"
                          "│ 🧍           👾 │ \n"
                          "└─────────────────┘")
                else:
                    print("┌─────────────────┐ \n"
                          f"│ {health}            {gremlin_health} │ \n"
                          "│ 🧍           👾 │ \n"
                          "└─────────────────┘")
                while gremlin_health > 0:
                    time.sleep(1)
                    find_rock()
                    type("One attack at a time...")
                    time.sleep(1)
                    print("┌──────────────────────────────┐ \n"
                          "│ OPTIONS:                     │ \n"
                          "│ Punch him (1)                │ \n"
                          f"│ Throw a rock; you have {rock} (2) │ \n"
                          "└──────────────────────────────┘")

                    choice = options("1", "2")

                    if choice == "1":
                        type("You throw a punch.")
                        chance = random.randint(1, 5)
                        time.sleep(1)
                        if chance > 2:
                            chance = random.randint(3, 8)
                            type(f"You swing and deal {chance} damage!")
                            time.sleep(1)
                            gremlin_health -= chance
                            type(f"The gremlin has {gremlin_health} health remaining.")
                            time.sleep(1)
                        else:
                            type("You miss. You're not very good at this.")
                            time.sleep(1)
                    elif choice == "2":
                        if rock > 0:
                            type("You throw a rock.")
                            chance = random.randint(1, 5)
                            time.sleep(1)
                            rock -= 1
                            if chance > 1:
                                chance = random.randint(5, 10)
                                type(f"You hit the gremlin for {chance} damage!")
                                gremlin_health -= chance
                                time.sleep(1)
                                type(f"The gremlin has {gremlin_health} health remaining.")
                                time.sleep(1)
                            elif chance == 1:
                                type("You miss. Somehow.")
                                time.sleep(1)
                        elif rock == 0:
                            type("You search for a rock, but don't find one.")
                            time.sleep(1)

                    if gremlin_health <= 0:
                        time.sleep(1)
                        type(f"The gremlin is defeated! You won with {health} health remaining.")
                        time.sleep(2)
                        type("You feel like your combat abilities have improved.")
                        gremlin_fight = 1
                        # This gives you a higher success rate when punching later on in the game!
                        break

                    type("The gremlin attacks you.")
                    chance = random.randint(1, 7)
                    time.sleep(1)
                    if chance > 2:
                        chance = random.randint(2, 6)
                        type(f"The gremlin does {chance} damage!")
                        health -= chance
                        time.sleep(1)
                        type(f"You have {health} health remaining.")
                    elif chance == 1:
                        type("The gremlin misses you.")
                        time.sleep(1)
                    if health < 10:
                        print("┌─────────────────┐ \n"
                              f"│ {health}             {gremlin_health} │ \n"
                              "│ 🧍           👾 │ \n"
                              "└─────────────────┘")
                    else:
                        print("┌─────────────────┐ \n"
                              f"│ {health}            {gremlin_health} │ \n"
                              "│ 🧍           👾 │ \n"
                              "└─────────────────┘")
                    time.sleep(1)

                    game_over()

    time.sleep(2)
    type("The hallway continues for a while.")
    time.sleep(1)
    type("Light shines in from slits carved into the stone above.")
    time.sleep(1)
    chance = random.randint(1, 2)
    if chance == 1:
        chance = random.randint(1, 3)
        if chance == 1:
            type("On the floor you find a rock.")
            time.sleep(1)
            print("┌────┐ \n"
                  "│ 🌑 │ \n"
                  "└────┘")
            time.sleep(1)
            type("You pocket it. [+1 Rock]")
            rock += 1
            time.sleep(1)
        if chance == 2:
            type("On the floor you find two rocks.")
            time.sleep(1)
            print("┌─────┐ \n"
                  "│ 🌑🌑 │ \n"
                  "└─────┘")
            time.sleep(1)
            type("You pocket them. [+2 Rocks]")
            rock += 2
            time.sleep(1)
        if chance == 3:
            type("On the floor you find three rocks.")
            time.sleep(1)
            print("┌─────────┐ \n"
                  "│ 🌑🌑🌑 │ \n"
                  "└─────────┘")
            time.sleep(1)
            type("You pocket them. [+3 Rocks]")
            rock += 3
            time.sleep(1)
        type("You keep moving, the stone cold against your feet.")
    elif chance == 2:
        type("Covered in cobwebs, you find a rusty sword lying on the side of the corridor.")
        time.sleep(1)
        print("┌────┐ \n"
              "│ 🗡️ │ \n"
              "└────┘")
        sword_encounter = "Yes"
        time.sleep(1)
        sword = 1
        swings = random.randint(4, 8)
        type(f"You pick it up. You figure it can handle around {swings} swings before it would break.")
        time.sleep(2)
        type("You keep moving, the stone cold against your feet.")
    time.sleep(1)
    type("Eventually you a come across a large room.")
    time.sleep(1)
    type("A doorway lies at the far end with sunlight shining through.")
    time.sleep(1)
    type("You found the entrance to the dungeon. The air feels fresh.")
    time.sleep(1)
    type("You hear a noise...")
    time.sleep(1)
    type("...breathing.")
    time.sleep(1)
    type("You turn, and spot a large orc, staring you down.")
    time.sleep(1)
    type('"You really thought, you could get out this easily?"')
    time.sleep(1)
    type('"No one gets past me!" he huffs.')
    time.sleep(1)

    # FINAL FIGHT
    if sword == 1:
        if rock > 1:
            type(f"You prepare to fight. You have a rusty sword and {rock} rocks.")
        elif rock == 1:
            type(f"You prepare to fight. You have a rusty sword and {rock} rock.")
        else:
            type(f"You prepare to fight. You have a rusty sword and no rocks.")
    else:
        if rock > 1:
            type(f"You prepare to fight. You have {rock} rocks.")
        elif rock == 1:
            type(f"You prepare to fight. You have {rock} rock.")
        else:
            type(f"You prepare to fight. You have no rocks.")
    time.sleep(1)

    orc_battle_health()

    while orc_health > 0:
        time.sleep(1)
        find_rock()
        type("One attack at a time...")
        time.sleep(1)
        if sword == 1:
            if swings > 1:
                print("┌───────────────────────────────────────────────┐ \n"
                      "│ OPTIONS:                                      │ \n"
                      "│ Punch him (1)                                 │ \n"
                      f"│ Throw a rock; you have {rock} (2)                  │ \n"
                      f"│ Swing with your sword; {swings} swings remaining (3) │ \n"
                      "└───────────────────────────────────────────────┘")
            elif swings == 1:
                print("┌──────────────────────────────────────────────┐ \n"
                      "│ OPTIONS:                                     │ \n"
                      "│ Punch him (1)                                │ \n"
                      f"│ Throw a rock; you have {rock} (2)                 │ \n"
                      f"│ Swing with your sword; {swings} swing remaining (3) │ \n"
                      "└──────────────────────────────────────────────┘")

            choice = options("1", "2", "3")

            if choice == "1":
                type("You throw a punch.")
                chance = random.randint(1, 5)
                time.sleep(1)
                if gremlin_fight == 1:
                    if chance > 1:
                        chance = random.randint(4, 9)
                        type(f"You swing and deal {chance} damage!")
                        time.sleep(1)
                        orc_health -= chance
                        type(f"The orc has {orc_health} health remaining.")
                        time.sleep(1)
                    else:
                        type("You miss.")
                        time.sleep(1)
                else:
                    if chance > 2:
                        chance = random.randint(3, 9)
                        type(f"You swing and deal {chance} damage!")
                        time.sleep(1)
                        orc_health -= chance
                        type(f"The orc has {orc_health} health remaining.")
                        time.sleep(1)
                    else:
                        type("You miss. You're not very good at this.")
                        time.sleep(1)
            elif choice == "2":
                if rock > 0:
                    type("You throw a rock.")
                    chance = random.randint(1, 6)
                    time.sleep(1)
                    rock -= 1
                    if chance > 1:
                        chance = random.randint(5, 11)
                        type(f"You hit the orc for {chance} damage!")
                        orc_health -= chance
                        time.sleep(1)
                        type(f"The orc has {orc_health} health remaining.")
                    elif chance == 1:
                        type("You miss. Somehow.")
                        time.sleep(1)
                elif rock == 0:
                    type("You search for a rock, but don't find one.")
                    time.sleep(1)
            elif choice == "3":
                type("You swing at the orc.")
                chance = random.randint(1, 14)
                time.sleep(1)
                if chance > 1:
                    chance = random.randint(4, 18)
                    type(f"You hit the orc for {chance} damage!")
                    orc_health -= chance
                    swings -= 1
                    time.sleep(1)
                    if swings < 1:
                        type("The sword shatters upon impact.")
                        time.sleep(1)
                        type("You no longer have a sword.")
                        time.sleep(1)
                        swings = 0
                        sword = 2
                if chance == 1:
                    type("The orc reacts before you swing, grabbing the sword out of your hand.")
                    time.sleep(1)
                    type("The orc throws it across the room before you can react.")
                    time.sleep(1)
                    chance = random.randint(1, 4)
                    type(f"It shatters. You take {chance} damage from the flying debris.")
                    time.sleep(1)
                    health -= chance
                    swings = 0
                    sword = 2
        else:
            print("┌──────────────────────────────┐ \n"
                  "│ OPTIONS:                     │ \n"
                  "│ Punch him (1)                │ \n"
                  f"│ Throw a rock; you have {rock} (2) │ \n"
                  "└──────────────────────────────┘")

            choice = options("1", "2")

            if choice == "1":
                type("You throw a punch.")
                chance = random.randint(1, 5)
                time.sleep(1)
                if gremlin_fight == 1:
                    if chance > 1:
                        chance = random.randint(4, 9)
                        type(f"You swing and deal {chance} damage!")
                        time.sleep(1)
                        orc_health -= chance
                        type(f"The orc has {orc_health} health remaining.")
                    else:
                        type("You miss.")
                        time.sleep(1)
                else:
                    if chance > 2:
                        chance = random.randint(3, 9)
                        type(f"You swing and deal {chance} damage!")
                        time.sleep(1)
                        orc_health -= chance
                        type(f"The orc has {orc_health} health remaining.")
                        time.sleep(1)
                    else:
                        type("You miss. You're not very good at this.")
                        time.sleep(1)
            elif choice == "2":
                if rock > 0:
                    type("You throw a rock.")
                    chance = random.randint(1, 6)
                    time.sleep(1)
                    rock -= 1
                    if chance > 1:
                        chance = random.randint(5, 11)
                        type(f"You hit the orc for {chance} damage!")
                        orc_health -= chance
                        time.sleep(1)
                        type(f"The orc has {orc_health} health remaining.")
                    elif chance == 1:
                        type("You miss. Somehow.")
                        time.sleep(1)
                elif rock == 0:
                    type("You search for a rock, but don't find one.")
                    time.sleep(1)

        if orc_health <= 0:
            type(f"The orc is defeated! You won with {health} health remaining.")
            time.sleep(2)
            type("You stumble out of the dungeon, into the sun.")
            break

        if orc_slip == 1:
            type("The orc regains his balance, but is unable to attack yet.")
            orc_slip = 0
            time.sleep(1)
        else:
            type("The orc attacks you with his club.")
            chance = random.randint(1, 7)
            time.sleep(1)
            if chance > 1:
                chance = random.randint(3, 12)
                type(f"The orc does {chance} damage!")
                health -= chance
                time.sleep(1)
                type(f"You have {health} health remaining.")
            elif chance == 1:
                type("The orc swings and misses, throwing him off balance for one turn.")
                time.sleep(1)
                orc_slip = 1

        orc_battle_health()
        game_over()

    time.sleep(2)
    print("┌─────────────┐ \n"
          "│ YOU ESCAPED │ \n"
          "└─────────────┘ \n")
    time.sleep(1)

    if candy == 1:
        candy_encounter = "Yes"

    print("GAME STATS: \n"
          f"Remaining health: {health} \n"
          f"Remaining rocks: {rock} \n"
          f"Encountered gremlin: {gremlin_encounter} \n"
          f"Found candy: {candy_encounter} \n"
          f"Found rusty sword: {sword_encounter} \n")
    time.sleep(2)
    type("Thank you for playing! Play again for a different route!")
    time.sleep(60)

if __name__ == "__main__": # Again, everything in the main() function was made entirely by Gemini, explaining how, why and what it does.
    main()

# All changes to this version listed at the top. Happy with the improvements. If I did this from scratch, I would try using local variables more, but right now I'm unsure how I would implement them.
# ദ്ദി◝ ⩊ ◜.ᐟ