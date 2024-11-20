#variabler = värde
#if villkor:
#while villkor:

import sys, time

inventory = []

def print(text):
    for characters in text:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.01) #Sets a time for every letter to print
    
name = input("\nHello, whats your name? \n")
greeting = ("Welcome [name], You wake up after a long nights sleep ...")
greeting = greeting.replace("[name]", name)
print(greeting)


while True:
    print("You find yourself mystically in an hamsters body, where you lep over a field in hunt for the golden dandelion.\n")
    print("You flinch and freeze in you thought, are you looking at the [dandelion] or your mystical [hamster]-body?")

    choice = input("\nWhat are you choosing? \n").lower()

    if "hamster" in choice:
        print("In a dream like slow motion you stare at the fluffy ball, your mind clouded by oats and dust")
        break
    elif "dandelion" in choice:
        print("You scream in horror like the dandelion allergy individual you are, god bless you, you put the dandelion in you hamster-pouch")
        inventory.append("dandelion")
        break
    else:
        print("Your spelling skills are not on the strong side ...\n\n\n\n\n")

print("\nWell, well, look at that\n")


if "dandelion" in choice:
    while True:
        print("What an beautiful flower, you are tempted to eat it. But something tells you its not a good idea\n")
        print("After shoving the dandelion gently in you hamster-pouch you lift you head, the boundless field shines like gold in the glimmering sun. In the distance you see a [road], beside it is a majestic [forest] with trees stretching all the way to the sky.")

        choice = input("Where do you want to go?\n").lower()

        if "road" in choice:
            while True:
                print("You have decided to make your way to the road, hoping to meet another hamster that can inform you of where this is\n")
                print("Ohh no! An owl jumps up from nowhere, will you [flee] or [fight]?")
                choice = input("\nWhat do you want to do?\n").lower()

                if "flee" in choice:
                    while True:
                        print("You see an opening between the owls long legs, the gap is big enough for a small mouse to fit. But the razor sharp claws make you hesitate")
                        print("\nAt last you take a lep of faith as you run towards the massive bird. As you close you eyes you hope to make it ...\n")
                        print("Luckily you land in a hole, as you fall down the hole the giant bird tries to reach you with its giant claws but its only grasping in air.")
                        print("\nAs ou continue your way down the hole you are meet with two paths [left] and [right]")
                        
                        choice = input("Where do you want to go?\n").lower()

                        if "left" in choice:
                            print("You walk down a long dark path, as you are walking a [crack] in the wall peaks your interest\n")
                            choice = input("Do you want to take a closer look or keep [walking]?\n").lower()

                            if "crack" in choice:
                                while True:
                                    print("The crack is big enough for you to [reach] your tiny hamster hand into\n")
                                    choice = input("Do you want to reach your tiny hand into the crack or keep [walking]?\n").lower()
                                    
                                    if "reach" in choice:
                                        while True:
                                            print("As you reach your hand into the crack something touches you hand, it's so sharp you almost cut yourself\n")
                                            print("You grab the object and struggle to get it out of the crack, after struggling you finally get the object out\n")
                                            print("What a strange thing, this object is a paper, how strange, you look closer and a text magically appears, It reads as followed...\n")
                                            print("WAKE UP\n\n")
                                            print("As you read the paper you begin to feel dizzy, but that doesn't stop you from completing your quest!\n")
                                            print("You put the paper in you hamster pouch\n")
                                            inventory.append("strange paper")

                                            print("You wonder if there is anything else interesting in the other tunnel")
                                            choice = input("Do you want to [turn] around or continue [walking]?\n").lower()

                                            if "turn" in choice:
                                                print("You turn around an decide to follow the other tunnel.") #Keep writing on the turn choice

                                    elif "walking" in choice:
                                        print("As you keep walking you finally se the light of day sweeping through the cracks of dirt.") #Copy the code from the other walking when done
                                    else:
                                        ("Try to improve your spelling...\n\n\n\n\n")

                            if "walking" in choice:
                                while True:
                                    print("As you keep walking you finally se the light of day sweeping through the cracks of dirt.")
                                    print("Reaching the end a blinding light hits you eyes, forcing them shut. When you finally open them you se an busy street of hamsters, children playing, merchants selling their goods, knights patrolling.")
                                    print("A small child bumps into you, making you remember your mission as clear as water. You were supposed to bring the flower to the king to save his only daughter")
                                    print("You have to hurry!\n\n")
                                    print("As you reach the castle there are 4 guards all standing still like statues in front of the giant metal door\n")
                                    choice = input("Do you want to interact with one of the guards?[yes]/[no]\n")
                                    
                                    if "yes" in choice:
                                        print("The four guards are named Theo, Leo, Deion and Seion\n")
                                        choice = input("Which guard do you want to interact with?\n") #Continue yes answer
                                    elif "no" in choice:
                                        print("You walk up to the door, it seems so natural for you that it's strange. Almost as if you have done this thousands of times...\n")
                                        print("The door slowly opens as the golden filled palace fills your mind, such a marvelous sight. In the middle of the decorative room you se the king") #continue story
                            else:
                                print("You can't do that...\n\n\n\n\n")

                        elif "right" in choice:
                            while True:                                
                                print("You decide to take right, are you sure this is a good idea...")
                                print("O well there is no turning back now, you keep walking till you reach an pub, on the sign hanging over the wooden door is the name hungry bug")
                                choice = input("Do you want to keep on [walking] or go into the [pub]\n").lower()
                        else: 
                            print("You letters are not making sense...\n\n\n\n\n")

                elif "fight" in choice:
                    print("This is not a good idea...")
                    print("You get scared in the last second, luckily there is a hole nearby you that you can barely squeeze through. Your body moves on its own launching itself against the hole")
                    print("The darkness hits you, realizing you have escaped the scary owl you begin wandering down the dark tunnel. You reach two paths [left] and [right]")
                    choice = input("Where do you want to go?\n").lower()
                else:
                    print("Wow, you are as good as a ten year old at spelling!\n\n\n\n\n\n")

        elif "forest" in choice:
            print("You look a final time at the road with you dark and boundless eyes and decide to make you way into the forest")
            print("\nWhen you finally arrived the moon has already risen, you think to yourself, how can it take that long to walk?")
            print("\nYou look into the dark and erie forest, are you sure you won't regret [treespassing] the old witches forest? There is still a chance to [turn] around")
            choice = input("What do you want to do?\n").lower() #Continue forest story

        elif "eat" in choice:
            print("A voice in your head tells you that eating this dandelion won't do any good to you ... Are you really sure you want to eat this holy flower?")
            choice = input("\nDo you really want to EAT the dandelion?[yes]/[no]\n").lower()
            if choice == "yes":
                print("In one bite there is no trace of the flowers existence. The fluffy fur begins to glow as you are swaying side to side, the sky is really blue and beautiful ...")
                print(...)
                print("The sky has suddenly become dark and full with sparkles, it is as if they are calling to you. As you begin reaching out to them you se and familiar figure. It's a hand, your hand ...")
            elif choice == "no":
                print("You ponder if this choice will change your future, but the picture of an oat appears in you mind. As you think about the massive amount of oat you will gain from this golden flower the light of the sun shines through.")
                print("As the light blinds you the [road] ahead peaks your curiosity")
                choice = input("\nWhat do you want to do?\n").lower()
        else:
            print("Not being able to spell is not very good for you ...\n\n\n\n\n\n")

elif choice == "hamster":
    print("As you come back to your senses you se an [road] in the distance of the golden field, beside it an majestic stretches to the sky")
    choice = input("\nWhat do you want to do?\n").lower()

