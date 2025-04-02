print("Welcome")

run = True

animals = ["Dog", "Cat", "Horse"]

while run:
    choice = input("What do you want to do? \n[1] Print out\n[2] Add animals\n[3] End\n")

    if choice == "1":
        print("Print out:")
        for animal in animals:
            print(animal)
    elif choice == "2":
        animal = input("Add an new animal: ")
        animals.append(animal)
    elif choice == "3":
        run = False