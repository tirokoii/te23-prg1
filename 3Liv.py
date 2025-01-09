# Choose a character/ ability, +1, -1, 0
# Computer rolls 1-6
# If 1-3, roll low
# If 4-6, roll high
# Both players roll
# Compare result depending on high or low roll round
# If low round the winner gets a life
# If high round the winner attacks
# When hp hits 0 die

from random import randint 
import random, sys, time

class Stats:
    def __init__(self, name, hp, de, at):
        self.name = name
        self.hp = hp
        self.de = de
        self.at = at

def print(text):
    for characters in text:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.01)

def letters(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.5)
        

def round(healer, attacker, defender):
    if round_level == "low":
        healer.hp += 1

        if healer.hp > 5:
            healer.hp = 5

        print(f"{healer.name} heals one hp and is now at {healer.hp}\n")
        input("\n")
        print("...\n\n\n")

    else:
        if defender.de == 2 and attacker.at == 2:
            defender.de -= 2
            print(f"{defender.name} takes 0 dmg! Their health is still {defender.hp}\n")
            input("\n")
            print("...\n\n")

        elif defender.de == 1 and attacker.at == 2:
            defender.de -= 1
            defender.hp -= 1
            print(f"{defender.name} takes 1 dmg! Their health is now {defender.hp}\n")
            input("\n")
            print("...\n\n")

        elif defender.de == 0 and attacker.at == 2:
            defender.hp -= 2
            print(f"{defender.name} takes 2 dmg! Their health is now {defender.hp}\n")
            input("\n")
            print("...\n\n")

        elif defender.de == 1 and attacker.at == 1:
            defender.de -= 1
            print(f"{defender.name} takes 0 dmg! Their health is still {defender.hp}\n")
            input("\n")
            print("...\n\n")

        else:
            defender.hp -= 1
            print(f"{defender.name} takes 1 dmg! Their health is now {defender.hp}\n")
            input("\n")
            print("...\n\n")


play = "yes"

print("Hello and welcome to 3 lives!\n")
print("In this game you get to compete with a computer by rolling dices high or low\n")
print("-------------------------------------------------------------------------------\n\n")

while play.lower() == "yes" or play.lower() == "y":
    
    player_name = input("What's your name brave solider?\n")
    print("\n---\n\n")

    while True:
        print("There are 3 abilities to choose from, defense [k], attack [b] and nothing [v]\n")
        choice = input("What character ability do you want?\n")

        if choice.lower() == "k":
            player = Stats(player_name, 3, 2, 1)
            break

        elif choice.lower() == "b":
            player = Stats(player_name, 3, 1, 2)
            break

        elif choice.lower() == "v":
            player = Stats(player_name, 3, 1, 1)
            break

        else:
            print("Not a choice...\n\n\n")

    computer_choice = randint(1, 3)
    names = ["Ellon", "Parios", "Pleck", "Greger", "Matilda", "Stan", "Dante"]
    computer_name = random.choice(names)
    print("\n___________________________________________________\n")
    print(f"Your opponents name is {computer_name}, I wish you both the best of luck!\n")
    input(" \n\n")

    if computer_choice == 1:
        computer = Stats(computer_name, 3, 2, 1)

    elif computer_choice == 2:
        computer = Stats(computer_name, 3, 1, 2)

    else:
        computer = Stats(computer_name, 3, 1, 1)


    print("Stats:\n")
    print("_______________________________________\n\n")
    print(f"{computer.name}\n----------\n hp: {computer.hp}\n de: {computer.de}\n at: {computer.at}\n\n")
    print(f"{player.name}\n----------\n hp: {player.hp}\n de: {player.de}\n at: {player.at}\n")
    print("_______________________________________\n")
    input("")
    print("\n\n...\n\n")

    while player.hp > 0 and computer.hp > 0:

        roll = randint(1, 6)

        if roll < 4:
            print("It's a low round, try to roll as low as possible\n")
            print("The fighter with the lowest roll will heal one health\n\n")
            round_level = "low"

        elif roll > 3:
            print("It's a high round, try to roll as high as possible\n")
            print("The fighter with the highest roll will attack\n\n")
            round_level = "high"

        player_roll = randint(1, 6)
        computer_roll = randint(1, 6)

        print("Roll")
        letters("iiiiiiiiiiiiiiiiiiiiing\n\n")
        print("__________________________\n\n")
        print("Your rolled numbers are:\n")
        print("--------\n")
        print(f"{player.name}: {player_roll}\n")
        print(f"{computer.name}: {computer_roll}\n")
        print("__________________________\n")

        if round_level == "low":
            if player_roll < computer_roll:
                round(player, player, computer)

            elif player_roll > computer_roll:
                round(computer, computer, player)

            else:
                print("Both fighters look at each other in awkward silence...\n")
                input("\n")
                print("...\n\n\n")

        else:
            if player_roll > computer_roll:
                round(player, player, computer)

            elif player_roll < computer_roll:
                round(computer, computer, player)

            else:
                print("Both fighters look at each other in awkward silence...\n")
                input("\n")
                print("...\n\n\n")

    if player.hp > 0 or computer.hp > 0:
        print("GAME OVER\n")
        print("-----------\n\n")

        if player.hp > 0:
            print(f"{player.name} lost against {computer.name},, better luck next time!\n")

        else:
            print(f"{computer.name} lost against {player.name}, better luck next time!\n")


        while True:

            play = input("Do you want to play again? [y/n]\n\n")
        
            if play.lower() == "yes" or play.lower() == "y":
                letters("Restarting")
                letters("...")
                break

            elif play.lower() == "no" or play.lower() == "n":
                letters("Turning off")
                letters("...")
                break

            else:
                print("That is not a option...")