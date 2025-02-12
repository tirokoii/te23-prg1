#take present

inventory = ["fork", "york"]
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

            if choice in presents[x][1]:
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

take_present()