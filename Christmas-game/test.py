#take present
import random

'''inventory = ["fork", "york"]
presents_inventory = []
presents = [[["yogurt", 200, 1], "small"], [["hop", 300, 2], "big"]]

def take_present():
    x = 0
    y = 0
    z = 0
    con = "yes"
    while con == "yes":
        print("Take present")
        choice = input("")
        while True:

            if choice in presents[1]:
                print("yay")
                present = choice
                presents_inventory.append(present)
                for i in presents:
                    if choice == presents[x][1]:
                        for i in inventory:
                            print(inventory[z])
                            z += 1
                        replace = input("What item do you want to replace the present with?\n")
                        for i in inventory:
                            if replace == inventory[y]:
                                presents[x] = inventory[y]
                                print("You have now replaced the item")
                                con = "no"
                            y += 1
            x += 1

take_present()'''

'''class Present:
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

present_amount = random.randint(2, 4)

weight_roll = random.choice(weight)
house_roll = True

while house_roll == True:
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
    house_roll = False

present_inventory = []

present_inventory.append(present_one)
present_inventory.append(present_two)

present_inventory_two = [present_one, present_two, present_three, present_four]

print("2:", present_inventory_two)
print("1:", present_inventory)

print("You don't have anymore items to exchange presents for")
print("Calculating the worth of your presents")
x = 0

for i in present_inventory:
    print(f"{i.item}: {i.worth}")
    x += 1
    if x > 1:
        break
    else:
        i = present_inventory[x]

for i in present_inventory_two:
    print(f"{i.item}: {i.worth}")
    x += 1
    i = present_inventory[x]'''
x = 1
y = str(x + 1)
print(str(x + 1))
