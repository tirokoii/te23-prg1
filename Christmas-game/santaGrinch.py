
import random

'''def house_roll():
    while True:
        print("Rolling...")
        house_color = ["red", "green", "yellow", "white", "brown", "blue", "Orange"]
        house_chance = random.randint(1, 100)

        if house_chance <= 20: #20%
            house_des = "old"
        elif house_chance <= 23: #3%
            house_des = "fancy"
        elif house_chance <= 34: #10%
            house_des = "swedish"
        elif house_chance <= 55: #20%
            house_des = "wood"
        elif house_chance <= 60: #5%
            house_des = "new"
        elif house_chance <= 80: # 20%
            house_des = "lovely"
        elif house_chance <= 90: #10%
            house_des = "concrete"
        else:
            house_des = "stylish" #10%

        while True:
            house_color = random.choice(house_color) 

            print(f"Do you want to enter the {house_color} {house_des} house?")
            enter_house = input("[Y/N]\n")

            if enter_house.lower() == "y" or enter_house.lower() == "yes":
                print("Enter house")
                break
            elif enter_house.lower() == "n" or enter_house.lower() == "no":
                print("Reroll...")
                break
            else:
                print("Incorrect")

        while enter_house.lower() == "y" or enter_house.lower() == "yes":
            run = input("Want to leave? [Y/N]\n")

            if run.lower() == "y" or run.lower() == "yes":
                print("You escape")
                enter_house = "no"
            elif run.lower() == "n" or run.lower() == "no":
                print("You continue")
                break
            
        break

def presentRoll():
    while True:
        present_amount = random.randint(1, 10)
        presents = []
        content_list = []
        
        for i in range(present_amount):
            present_description = ["red", "blue", "green", "pink", "dotted", "striped", "heart", "long", "short", "big", "small"]
            present_description = random.choice(present_description)
            content_chance = random.randint(1, 100)

            if content_chance < 20: #20%
                content = "shoes"
            elif content_chance <= 30: #10%
                content = "speaker"
            elif content_chance == 31: #1%
                content = "Diamond necklace"
            elif content_chance <= 61: #30%
                content = "children's book"
            elif content_chance <= 71: #10%
                content = "card game" 
            elif content_chance <= 86: #15%
                content = "bag"
            elif content_chance <= 91: #5%
                content = "slippers"
            else: #9%
                content = "shark toy"
            presents.append(present_description)
            content_list.append(content)
        
        print(f"There are {present_amount} presents a ")
        print(* presents, sep = ", a ")

        while True:

            take_present_choice = input("Take a present? [Y/N]\n")

            if take_present_choice.lower() == "y" or take_present_choice.lower() == "yes":
                present_choice = input("Which present do you want to take?\n")

                if present_choice in presents:
                    for present in presents:
                        present = presents.pop(0)
                        if present_choice == present:
                            break
                else:
                    print("Are you sure?")
            elif take_present_choice.lower() == "n" or take_present_choice.lower() == "no":
                print("Leaving...")
                break
            break
        break


        

presentRoll()'''

class House:
    def __init__(self, text_f, color, description, text_b):
        self.text_f = text_f
        self.color = color
        self.description = description
        self.text_b = text_b

Common = [
    ["shoes", 200, 1 ],
    ["children's book", 200, 1],
    ["bag", 300, 1],
    ["socks", 100, 1]
]

Uncommon = [
    ["speaker", 500, 2],
    ["card game", 500, 2],
    ["flower", 700, 2]
]

Rare = [
    ["slippers", 1200, 3],
    ["shark toy", 800, 3]
]

Legendary = [
    ["lost diamond", 10000, 4]
]

'''def present_roll():

    present_amount = random.randint(1, 10)
        
    for i in range(present_amount):
        Present.description = ["red", "blue", "green", "pink", "dotted", "striped", "heart", "long", "short", "big", "small"]
        Present.description = random.choice(Present.description)

        content_chance = random.randint(1, 100)

        if content_chance < 20: #20%
            Present.content = "shoes"
            Present.value = 200
        elif content_chance <= 30: #10%
            Present.content = "speaker"
            Present.value = 500
        elif content_chance == 31: #1%
            Present.content = "Diamond necklace"
            Present.value = 10000
        elif content_chance <= 61: #30%
            Present.content = "children's book"
            Present.value = 200
        elif content_chance <= 71: #10%
            Present.content = "card game" 
            Present.value = 500
        elif content_chance <= 86: #15%
            Present.content = "bag"
            Present.value = 300
        elif content_chance <= 91: #5%
            Present.content = "slippers"
            Present.value = 1200
        else: #9%
            Present.content = "shark toy"
            Present.value = 800

    return Present.content, Present.value, Present.description'''

def present_type():

    weight_roll = random.choice(weight)

    if weight_roll == 1:
        present = random.choice(Common)
    elif weight_roll == 2:
        present = random.choice(Uncommon)
    elif weight_roll == 3:
        present = random.choice(Rare)
    else:
        present = random.choice(Legendary)

    return present

def present_des():

    present_description = ["red", "blue", "green", "pink", "dotted", "striped", "heart", "long", "short", "big", "small"]
    present_description = random.choice(present_description)

    return present_description

def present_print():
     
    present_amount = random.randint(3, 8)
    x = 0

    for i in range(present_amount):
        present = present_type()
        des = present_des()
        present_list.append([present, des])
    print("You can see", end=" ")
    for item in present_list:
        print("a " + present_list[x][1], end=" present ")
        if x == (present_amount -1):
            print("and " + present_list[x][1], end=" present")
        x += 1

def house_roll_rarity():
    
    rarity = random.randint(1, 100)

    if rarity <= 20: #20%
        House.description = "old"
    elif rarity <= 23: #3%
        House.description = "fancy"
    elif rarity <= 34: #10%
        House.description = "swedish"
    elif rarity <= 55: #20%
        House.description = "wooden"
    elif rarity <= 60: #5%
        House.description = "new"
    elif rarity <= 80: # 20%
        House.description = "lovely"
    elif rarity <= 90: #10%
        House.description = "concrete"
    else: #10%
        House.description = "stylish"

    return House.description

def input_YN(prompt, message1, message2):
    while True:
        answer = input(prompt)

        if answer.lower() == "y" or answer.lower() == "yes":
            print(message1)
            return "yes"
        elif answer.lower() == "n" or answer.lower() == "no":
            print(message2)
            return "no"

def pick_present():
    choice = input("Pick a present:\n")
    if choice in present_list:
        print(f"You take the {choice} present")


present_amount = 0
present_list = []
weight = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
items_list = ["feather", "pillow", "cat statue", "broom", "santa's helper", "cache", "pen", "witch hat", "utensils", "tooth brush", "candy", ""]
House.color = ["red", "green", "yellow", "white", "brown", "blue", "orange"]

while True:

    house_one = House("There is a", random.choice(House.color), house_roll_rarity(), "house")
    house_two = House("and a", random.choice(House.color), house_roll_rarity(), "house")
    repeat_text = "no"

    while True:
        print(house_one.text_f, house_one.color, house_one.description, house_one.text_b, end = " ")
        print(house_two.text_f, house_two.color, house_two.description, house_two.text_b)

        house_choice = input("Enter a house? [Y/N] \n")

        if house_choice.lower() == "y" or house_choice.lower() == "yes":
            while house_choice.lower() == "yes" or house_choice.lower() == "y":
                    
                    if repeat_text.lower() == "yes" or repeat_text.lower() == "y":
                        print("\n")
                        print(house_one.text_f, house_one.color, house_one.description, house_one.text_b, end = " ")
                        print(house_two.text_f, house_two.color, house_two.description, house_two.text_b)
                        repeat_text = "no"
                    
                    house_enter = input(f"Which house do you want to enter? \n")
                    house_description = house_enter

                    if house_enter == house_one.color or house_enter == house_one.description:
                        print(f"You enter the {house_description} house...")                           

                        house_choice = input_YN("\nDo you want to leave the house?[Y/N]\n", "Okay, leave then", "Okay, stay")

                        present_print()

                        if house_choice == "no":
                            choice = input_YN("Do you want to take a present?[Y/N] \n", "Okay, then pick a present\n",  "Okay, leave then")
                                
                        elif house_choice == "yes":
                            break
                        else:
                            print("Can you not")
                            
                    elif house_choice == house_one.color or house_enter == house_two.description:
                        print("Hello")
                    else:
                        print("There is no such house...\n")
                        house_choice = input("Are you sure you want to enter one of the houses? [Y/N]\n")
                        repeat_text = "yes"

        elif house_choice.lower() == "n" or house_choice.lower() == "no":
            print("Reroll...\n\n")
            break
        else:
            print("There is no house called that...\n")
