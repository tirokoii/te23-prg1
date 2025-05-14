import random

inventory_list = ["feather", "pillow", "cat statue", "broom", "santa's helper", "cache", "pen", "witch hat", "utensils", "tooth brush", "candy", "lamp", "monkey paw", "calculator", "tea", "broom", "wig"]
inventory = []
present_inventory = []

for i in range(1, 11):
    item = random.choice(inventory_list)
    inventory.append(item)

class House:
    def __init__(self, color, description):
        self.color = color
        self.description = description

class Present:
    def __init__(self, description, item, worth):
        self.description = description
        self.item = item
        self.worth = worth

common = [
    ["shoes", 200],
    ["children's book", 200],
    ["bag", 300],
    ["socks", 100]
]

uncommon = [
    ["speaker", 500],
    ["card game", 500],
    ["flower", 700]
]

rare = [
    ["slippers", 1200],
    ["shark toy", 800]
]

legendary = [
    ["lost diamond", 10000]
]

present_description = ["red", "blue", "green", "pink", "dotted", "striped", "heart", "long", "short", "big", "small"]
weight = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4]

def printHouse():
    print(f"There is a {house_one.color} {house_one.description} house and a {house_two.color} {house_two.description} house")

def printPresent():
    if present_amount == 1:
        print(f"There is one single item in the room, a {present_one.description} present")
    elif present_amount == 2:
        print(f"There are two items in the room, a {present_one.description} present and a {present_two.description} present")
    elif present_amount == 3:
        print(f"There are three items in the room, a {present_one.description} present, a {present_two.description} present and a {present_three.description} present")
    elif present_amount == 4:
        print(f"There are four items in the room, a {present_one.description} present, a {present_two.description} present, a {present_three.description} present and a {present_four.description} present")
    else:
        print("There are no more presents")
    
house_color_list = ["red", "green", "yellow", "white", "brown", "blue", "orange"]
game = True


print("Welcome to SantaGrinch!")
print("You are the Grinch out to destroy christmas, nicely. Because you feel bad about stealing presents from children you exchange items from you own home")
print("Good luck!\n")

while game == True:
    for i in range(0, 2):
        de_range = random.randint(1, 100)
        if de_range < 20:
            house_description = "old"
        elif de_range < 40:
            house_description = "swedish"
        elif de_range < 55:
            house_description = "wooden"
        elif de_range < 70:
            house_description = "new"
        elif de_range < 80:
            house_description = "lovely"
        elif de_range < 90:
            house_description = "stylish"
        elif de_range < 95:
            house_description = "concrete"
        else:
            house_description = "fancy"
        if i == 1:
            house_one = House(random.choice(house_color_list), house_description)
        else:
            house_two = House(random.choice(house_color_list), house_description)

    present_amount = random.randint(2, 4)

    weight_roll = random.choice(weight)

    if weight_roll == 1:
        present = random.choice(common)
    elif weight_roll == 2:
        present = random.choice(uncommon)
    elif weight_roll == 3:
        present = random.choice(rare)
    else:
        present = random.choice(legendary)
    
    present_one = Present(random.choice(present_description), present[0], present[1])
    present_two = Present(random.choice(present_description), present[0], present[1])
    present_three = Present(random.choice(present_description), present[0], present[1])
    present_four = Present(random.choice(present_description), present[0], present[1])

    again = True
    inside = True
    house = True
    
    while again == True:
        house = True
        inside = True
        again = True
        if len(inventory) == 0:
            inside = False
            house = False
            again = False
            game = False
        printHouse()
        choice = input("Which house do you want to enter? ")
        if choice.lower() == house_one.color or choice.lower() == house_one.color + " " + "house" or choice.lower() == house_one.color + " " + house_one.description  or choice.lower() == house_one.color + " " + house_one.description + " " + "house":
            while house == True:
                choice = choice + " 1"
                if str.split(choice)[1] == "1":
                    print(f"Entering the {str.split(choice)[0]} house")
                else:
                    print(f"Entering the {str.split(choice)[0]} {str.split(choice)[1]} house")
                choice = input("Are you sure you want to take presents from this house? [y/n] ")
                if choice.lower() == "yes" or choice.lower() == "y":
                    while inside == True:
                        printPresent()
                        if present_amount == 0:
                            inside = False
                        x = 1
                        i = 0
                        present_loop = True
                        while present_loop == True and present_amount > 0:
                            choice = input("Which present do you want to take? ")
                    
                            if choice.lower() == present_one.description or choice.lower() == present_one.description + " " + "present":
                                print("Choose an item to replace the present: \n")
                                print("\nInventory\n")
                                for item in inventory:
                                    print(f"{x}. {item}")
                                    x += 1

                                choice = input("Item: ")

                                while True:
                                    if choice in inventory[i] or choice == str(i + 1):
                                        print(f"Exchanging the {inventory[i]} for the {present_one.description} present")
                                        present_inventory.append(present_one)
                                        present_amount -= 1
                                        if present_amount == 1:
                                            present_one = present_two
                                        elif present_amount == 2:
                                            present_one = present_two
                                            present_two = present_three
                                        elif present_amount == 3:
                                            present_one = present_two
                                            present_two = present_three
                                            present_three = present_four
                                        del inventory[i]
                                        break
                                    elif int(choice) < 0 or int(choice) > len(inventory):
                                        choice = input("Item: ")
                                    else:
                                        print("Try again")
                                    i += 1
                                present_loop = False
                                break
                            elif choice == present_two.description or choice.lower() == present_two.description + " " + "present":
                                print("Choose an item to replace the present: \n")
                                print("\nInventory\n")
                                for item in inventory:
                                    print(f"{x}. {item}")
                                    x += 1
                                choice = input("Item: ")
                                while True:
                                    if int(choice) < len(inventory) or int(choice) > len(inventory) or choice not in inventory[i]:
                                        print("Try again")
                                    elif choice in inventory[i] or choice == str(i + 1):
                                        print(f"Exchanging the {inventory[i]} for the {present_two.description} present")
                                        present_inventory.append(present_two)
                                        present_amount -= 1
                                        if present_amount == 2:
                                            present_two = present_three
                                        elif present_amount == 3:
                                            present_two = present_three
                                            present_three = present_four
                                        del inventory[i]
                                        break
                                    i += 1
                                present_loop = False
                            elif choice == present_three.description or choice.lower() == present_three.description + " " + "present":
                                print("Choose an item to replace the present: \n")
                                print("\nInventory\n")
                                for item in inventory:
                                    print(f"{x}. {item}")
                                    x += 1
                                choice = input("Item: ")
                                while True:
                                    if choice in inventory[i] or choice == str(i + 1):
                                        print(f"Exchanging the {inventory[i]} for a {present_three.description} present")
                                        present_inventory.append(present_three)                                               
                                        present_amount -= 1
                                        if present_amount == 3:
                                            present_three = present_four
                                        del inventory[i]
                                        break
                                    i += 1
                                present_loop = False
                            elif choice.lower() == present_four.description or choice.lower() == present_four.description + " " + "present":
                                print("Choose an item to replace the present: \n")
                                print("\nInventory\n")
                                for item in inventory:
                                    print(f"{x}. {item}")
                                    x += 1
                                choice = input("Item: ")
                                while True:
                                    if choice in inventory[i] or choice == str(i + 1):
                                        print(f"Exchanging the {inventory[i]} for a {present_four.description} present")
                                        present_inventory.append(present_four)
                                        del inventory[i]
                                        break
                                    i += 1
                                present_loop = False
                            else:
                                print("You may have spelled it wrong, try again")
                        while True:
                            choice = input("Do you want to take another present? [y/n] ")
                            if choice.lower() == "y" or choice.lower() == "yes":
                                if len(inventory) == 0:
                                    inside = False
                                    house = False
                                    again = False
                                    game = False
                                if present_amount == 0:
                                    print("You are now leaving the house")
                                    inside = False
                                    house = False
                                    again = False
                                break
                            elif choice.lower() == "n" or choice.lower() == "no":
                                inside = False
                                house = False
                                again = False
                                break
                            else:
                                print("Try writing yes, y, n or no.")
                elif choice.lower() == "no" or choice.lower() == "n":
                    print("You walk right back out...")
                    house = False
                else:
                    print("Seems you have written something wrong")
                    
        elif choice.lower() == house_two.color or choice.lower() == house_two.color + " " + "house" or choice.lower() == house_two.color + " " + house_two.description  or choice.lower() == house_two.color + " " + house_two.description + " " + "house":
             while house == True:
                choice = choice + " 1"
                if str.split(choice)[1] == "1":
                    print(f"Entering the {str.split(choice)[0]} house")
                else:
                    print(f"Entering the {str.split(choice)[0]} {str.split(choice)[1]} house")
                choice = input("Are you sure you want to take presents from this house? [y/n] ")
                if choice.lower() == "yes" or choice.lower() == "y":
                    while inside == True:
                        printPresent()
                        if present_amount == 0:
                            inside = False
                        x = 1
                        i = 0
                        present_loop = True
                        while present_loop == True and present_amount > 0:
                            choice = input("Which present do you want to take? ")
                    
                            if choice.lower() == present_one.description or choice.lower() == present_one.description + " " + "present":
                                print("Choose an item to replace the present: \n")
                                print("\nInventory\n")
                                for item in inventory:
                                    print(f"{x}. {item}")
                                    x += 1
                                choice = input("Item: ")

                                while True:
                                    if choice in inventory[i] or choice == str(i + 1):
                                        print(f"Exchanging the {inventory[i]} for the {present_one.description} present")
                                        present_inventory.append(present_one)
                                        present_amount -= 1
                                        if present_amount == 1:
                                            present_one = present_two
                                        elif present_amount == 2:
                                            present_one = present_two
                                            present_two = present_three
                                        elif present_amount == 3:
                                            present_one = present_two
                                            present_two = present_three
                                            present_three = present_four
                                        del inventory[i]
                                        break
                                    i += 1
                                present_loop = False
                                break
                            elif choice == present_two.description or choice.lower() == present_two.description + " " + "present":
                                print("Choose an item to replace the present: \n")
                                print("\nInventory\n")
                                for item in inventory:
                                    print(f"{x}. {item}")
                                    x += 1
                                choice = input("Item: ")
                                while True:
                                    if choice in inventory[i] or choice == str(i + 1):
                                        print(f"Exchanging the {inventory[i]} for the {present_two.description} present")
                                        present_inventory.append(present_two)
                                        present_amount -= 1
                                        if present_amount == 2:
                                            present_two = present_three
                                        elif present_amount == 3:
                                            present_two = present_three
                                            present_three = present_four
                                        del inventory[i]
                                        break
                                    i += 1
                                present_loop = False
                            elif choice == present_three.description or choice.lower() == present_three.description + " " + "present":
                                print("Choose an item to replace the present: \n")
                                print("\nInventory\n")
                                for item in inventory:
                                    print(f"{x}. {item}")
                                    x += 1
                                choice = input("Item: ")
                                while True:
                                    if choice in inventory[i] or choice == str(i + 1):
                                        print(f"Exchanging the {inventory[i]} for a {present_three.description} present")
                                        present_inventory.append(present_three)                                               
                                        present_amount -= 1
                                        if present_amount == 3:
                                            present_three = present_four
                                        del inventory[i]
                                        break
                                    i += 1
                                present_loop = False
                            elif choice.lower() == present_four.description or choice.lower() == present_four.description + " " + "present":
                                print("Choose an item to replace the present: \n")
                                print("\nInventory\n")
                                for item in inventory:
                                    print(f"{x}. {item}")
                                    x += 1
                                choice = input("Item: ")
                                while True:
                                    if choice in inventory[i] or choice == str(i + 1):
                                        print(f"Exchanging the {inventory[i]} for a {present_four.description} present")
                                        present_inventory.append(present_four)
                                        del inventory[i]
                                        break
                                    i += 1
                                present_loop = False
                            else:
                                print("You may have spelled it wrong, try again")
                        while True:
                            choice = input("Do you want to take another present? [y/n] ")
                            if choice.lower() == "y" or choice.lower() == "yes":
                                if len(inventory) == 0:
                                    inside = False
                                    house = False
                                    again = False
                                    game = False
                                if present_amount == 0:
                                    print("You are now leaving the house")
                                    inside = False
                                    house = False
                                    again = False
                                break
                            elif choice.lower() == "n" or choice.lower() == "no":
                                inside = False
                                house = False
                                again = False
                                break
                            else:
                                print("Try writing yes, y, n or no.")
                elif choice.lower() == "no" or choice.lower() == "n":
                    print("You walk right back out...")
                    house = False
                else:
                    print("Seems you have written something wrong")
                    
        else:
            print("Hmm, seems we don't have that house...")

print("\n\nYou don't have anymore items to exchange presents for")
print("Calculating the worth of your presents...\n")
print("Items in presents:")
x = 0
earned = 0
for i in present_inventory:
    print(f"{i.item}: {i.worth}")
    x += 1
    earned += i.worth
    if x > 9:
        break
    else:
        i = present_inventory[x]

with open("score.txt", "a+") as scores:
    scores.write(f"{earned}\n")

with open("score.txt", "r") as scores:
    score_list = scores.readlines()

int_list = [int(n) for n in score_list]
hs = max(int_list)
print(f"High Score: {hs}")

print(f"\nYou earned: {earned}\n")
print("Thank you for playing!")
