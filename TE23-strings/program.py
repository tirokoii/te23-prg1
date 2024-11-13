import sys, time

inventory = []

def print(text):
    for characters in text:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.06) 
    

name = input("\nHello, whats your name? \n")
greeting = ("Welcome [name], You wake up after a long nights sleep ...")
greeting = greeting.replace("[name]", name)
print(greeting)

print("You find yourself mystically in an hamsters body, where you lep over an field in hunt for the golden dandelion.")
print("You flinch and freeze in you thought, are you looking at the [dandelion] or your mystical [hamster]-body?")

while True:
    choice = input("What are you choosing? \n").lower()

    if "hamster" in choice:
        print("In a dream like slow motion you stare at the fluffy ball, your mind clouded by oats and dust")
        break
    elif "dandelion" in choice:
        print("You scream in horror like the dandelion allergy individual you are, god bless you, you put the dandelion in you hamster-pouch")
        inventory.append("dandelion")
        break
    else:
        print("Your spelling skills are not on the strong side ...")

print("Well, well, look at that")

if "dandelion" in choice:
    print("What an beautiful flower, you are tempted to eat it. But something tells you its not a good idea")
    print("After shoving the dandelion gently in you hamster-pouch you lift you head, the boundless field shines like gold in the glimmering sun. In the distance you see a [road], beside it is a majestic [forest] with trees stretching all the way to the sky.")

    while True:
        choice = input("Where do you want to go?\n")

        if "road" in choice:
            print("You have decided to make your way to the road, hoping to meet another hamster that can inform you of where this is")
            print("Ohh no! An owl jumps against you, will you [flee] or [fight]")
            choice = input("What do you want to do?\n")

            if "flee" in choice:
                print("You se an opening between the owls long legs, the gap is big enough for a small mouse to fit. But the razor sharp claws make you hesitate")
                print("At last you take a lep of faith as you run towards the massive bird. As you close you eyes you hope to make it ...")

        elif "forest" in choice:
            print("You look a final time at the road with you dark and boundless eyes and decide to make you way into the forest")
            print("When you finally arrived the moon has already risen, you think to yourself, how can it take that long to walk?")
            print("You look into the dark and erie forest, are you sure you won't regret [treespassing] the old witches forest? There is still a chance to [turn] around")
            choice = input("What do you want to do?\n") #Continue forest story

        elif "eat" in choice:
            print("A voice in your head tells you that eating this dandelion won't do any good to you ... Are you really sure you want to eat this holy flower?")
            choice = input("Do you want to EAT the dandelion?\n")
            if choice == "yes":
                print("In one bite there is no trace of the flowers existence. The fluffy fur begins to glow as you are swaying side to side, the sky is really blue and beautiful ...")
                print(...)
                print("The sky has suddenly become dark and full with sparkles, it is as if they are calling to you. As you begin reaching out to them you se and familiar figure. It's a hand, your hand ...")
            elif choice == "no":
                print("You ponder if this choice will change your future, but the picture on an oat appears in you mind. As you think about the massive amount of oat you will gain from this golden flower, the light of the sun shines through.")
                print("As the light blinds you the road ahead is peaking your curiosity")
                choice = input("What do you want to do?\n")
        else:
            print("Not being able to spell is not very good for you ...")

        
elif choice == "hamster":
    print("As you come back to your senses you se an [road] in the distance of the golden field, beside it an majestic stretches to the sky")
    choice = "What do you want to do?\n"

