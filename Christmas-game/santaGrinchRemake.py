import random
inventory_list = ["feather", "pillow", "cat statue", "broom", "santa's helper", "cache", "pen", "witch hat", "utensils", "tooth brush", "candy", "lamp", "monkey paw", "calculator", "tea", "broom", "wig"]
inventory = []

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

def presentsWhole():
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

    if present_amount == 1:
        present_one = Present(random.choice(present_description), present[0], present[1])
        print(f"There is one single item in the room, a {present_one.description} present")
    elif present_amount == 2:
        present_one = Present(random.choice(present_description), present[0], present[1])
        present_two = Present(random.choice(present_description), present[0], present[1])
        print(f"There are two items in the room, a {present_one.description} and a {present_two.description} present")
    elif present_amount == 3:
        present_one = Present(random.choice(present_description), present[0], present[1])
        present_two = Present(random.choice(present_description), present[0], present[1])
        present_three = Present(random.choice(present_description), present[0], present[1])
        print(f"There are three items in the room, a {present_one.description}, a {present_two.description} and a {present_three.description} present")
    else:
        present_one = Present(random.choice(present_description), present[0], present[1])
        present_two = Present(random.choice(present_description), present[0], present[1])
        present_three = Present(random.choice(present_description), present[0], present[1])
        present_four = Present(random.choice(present_description), present[0], present[1])
        print(f"There are three items in the room, a {present_one.description}, a {present_two.description}, a {present_three.description} and a {present_four.description} present")

    x = 1
    i = 0
    present_loop = True
    present_inventory = []
    while present_loop == True:
        while present_amount > 0:
            choice = input("Which present do you want to take? ")
            if choice.lower() == present_one.description:
                print("Choose an item to replace the present: \n")
                print("Inventory\n")
                for item in inventory:
                    print(f"{x}. {item}")
                    x += 1
                choice = input("Item: ")
                while True:
                    if choice in inventory[i] or choice == i + 1:
                        print(f"Exchanging the {inventory[i]} for the {present_one.description} present")
                        present_inventory.append(present_one)
                        del inventory[i]
                        break
                    i += 1
                present_loop = False
            elif choice == present_two.description:
                print("Choose an item to replace the present: \n")
                print("Inventory\n")
                for item in inventory:
                    print(f"{x}. {item}")
                    x += 1
                choice = input("Item: ")
                while True:
                    if int(choice) == i + 1 or choice.lower() in inventory[i]:
                        print(f"Exchanging the {inventory[i]} for a {present_two.description} present")
                        present_inventory.append(present_two)
                        del inventory[i]
                        break
                    i += 1
                present_loop = False
            elif choice == present_three.description:
                print("Choose an item to replace the present: \n")
                print("Inventory\n")
                for item in inventory:
                    print(f"{x}. {item}")
                    x += 1
                choice = input("Item: ")
                while True:
                    if choice in inventory[i] or choice == i + 1:
                        print(f"Exchanging the {inventory[i]} for a {present_three.description} present")
                        present_inventory.append(present_three)
                        del inventory[i]
                        break
                    i += 1
                present_loop = False
            elif choice == present_four.description:
                print("Choose an item to replace the present: \n")
                print("Inventory\n")
                for item in inventory:
                    print(f"{x}. {item}")
                    x += 1
                choice = input("Item: ")
                while True:
                    if choice.lower() in inventory[i] or choice == i + 1:
                        print(f"Exchanging the {inventory[i]} for a {present_four.description} present")
                        present_inventory.append(present_four)
                        del inventory[i]
                        break
                    i += 1
                present_loop = False
            else:
                print("You may have spelled it wrong, try again")
        present_amount -= 1

while True:
    
    house_color = ["red", "green", "yellow", "white", "brown", "blue", "orange"]
    house_enter = True
    def houseDescription():

        range = random.randint(1, 100)

        if range < 20:
            house_description = "old"
        elif range < 40:
            house_description = "swedish"
        elif range < 55:
            house_description = "wooden"
        elif range < 70:
            house_description = "new"
        elif range < 80:
            house_description = "lovely"
        elif range < 90:
            house_description = "stylish"
        elif range < 95:
            house_description = "concrete"
        else:
            house_description = "fancy"

        return house_description

    house_one = House(random.choice(house_color), houseDescription())
    house_two = House(random.choice(house_color), houseDescription())
    while house_enter == True:
        print(f"There is a {house_one.color} {house_one.description} house and a {house_two.color} {house_two.description} house")
        choice = input("Which house do you want to enter? ")
        if choice.lower() == house_one.color or house_one.description or house_one.color and house_one.description:
            while True:
                choice = input("Are you sure you want to take presents from this house? [y/n] ")
                if choice.lower == "yes" or "y":
                    while True:
                        presentsWhole()
                        choice = input("Do you want to take another present? [y/n] ")
                        if choice.lower() == "y" or "yes":
                            presentsWhole()
                        elif choice.lower() == "n" or "no":
                            while True:
                                choice = input("Do you want to leave then? [y/n] ")
                                if choice == "y" or "yes":
                                    house_enter == False
                                elif choice == "n" or "no":
                                    break
                                else:
                                    print("Something is wrong...")          
                elif choice.lower == "no" or "n":
                    while True:
                        choice = input("Do you want to leave? [y/n]")
                        if choice.lower() == "y" or "yes":
                            house_enter = False
                        elif choice.lower() == "n" or "no":
                            print("Okay")
                            break
                        else:
                            print("Sadly you can't")
                else:
                    print("Not possible")
        elif choice.lower() == house_two.color or house_two.description or house_two.color and house_two.description:
            print("Nice")
