inventory = []
name = input("\nHello, whats your name? \n")
greeting = ("Welcome to my world [name], You wake up after a long nights sleep ...")
greeting = greeting.replace("[name]", name)
print(greeting)

print("You find yourself mystically in an hamsters body, where you lep over an field in hunt for the golden dandelion.")
print("You flinch and freeze in you thought, are you looking at the [dandelion] or your mystical [hamster]-body?")
choice = input("What are you choosing? \n").lower()
if "hamster" in choice:
    print("In a dream like slow motion you stare at the fluffy ball, your mind clouded by oats and dust")
elif "dandelion" in choice:
    print("You scream in horror like the dandelion allergy individual you are, god bless you, you put the dandelion in you hamster-pouch")
    inventory.append("dandelion")
else:
    print("Your spelling is not on the strong side")

print("Well, well, look at that")

if choice == "dandelion":
    print("What an beautiful flower, you are tempted to [eat] it. But something tells you its not a good idea")
    print("You look up after shoving the dandelion gently in you hamster-pouch you lift you head, the boundless field shines like gold in the glimmering sun. In the distance you see a [road], beside it are majestic trees stretching all the way to the sky.")
    choice = "What do you want to do?\n"
    if choice == "road":
        print("You have decided to make your way to the road, hoping to meet another hamster that can inform you of where this is")
        print("Ohh no! An owl jumps against you, will you [flee] or [fight]")
        choice = input("What do you want to do?\n") #Continue fight

    if choice == "forest":
        print("You look a final time at the road with you dark and boundless eyes and decide to make you way into the forest")
        print("When you finally arrived the moon has already risen, you think to yourself, how can it take that long to walk?")
        print("You look into the dark and erie forest, are you sure you won't regret [treespasing] the old witches forest? There is still a chance to [turn] around")
        choice = input("What do you want to do?\n") #Continue forest story

    if choice == "eat":
        print("A voice in your head tells you that eating this dandelion won't do any good to you ... Are you really sure you want to eat this holy flower?")
        choice = input("Do you want to EAT the dandelion?\n")
        if choice == "yes":
            print("In one bite there is no trace of the flowers existence. The fluffy fur begins to glow as you are swaying side to side, the sky is really blue and beautiful ...")
            print(...)
            print("The sky has suddenly become dark and full with sparkles, it is as if they are calling to you. As you begin reaching out to them you se and familiar figure. It's a hand, your hand ...") #Continue of no
        
elif choice == "hamster":
    print("As you come back to your senses you se an [road] in the distance of the golden field, beside it an majestic stretches to the sky")
    choice = "What do you want to do?\n"

