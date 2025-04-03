#Count from 1
#When you reach numbers divided by 7 and 11 clap, or number has 7 or 11 in it
#Make characters and player for the game
#If make it harder switch direction when clap

#Option nr 1
#Make a list of said numbers

#Option nr 2
#Make a if statement that checks if the number has 7 0r 11 in it or is dividable with 7 or 11

#Option nr 1 - characters
#Make a list that holds each character - so that they all have assigned seats already

#Option nr 2 - char
#Assign a seat to each character
from random import shuffle
count = 0
nameListCount = -1
countList = []
playerCountList = []
countList11 = ["11", "111", "211", "311" ]
characters = ["Henke", "Ash", "Billy", "Rasmus", "Jens", "player"]
shuffle(characters)
#list = [0, 1, 2, 3, 4]

while True:
    count += 1
    nameListCount += 1
    name = characters[nameListCount]

    for char in str(count):
        countList.append(char)
    
    if "player" in name:

        playerChoice = input("Write the number or clap: ")
            

        if playerChoice.isdigit():
            for char in (playerChoice):
                playerCountList.append(char)
            if "7" in playerCountList or countList11 in playerCountList and "7" in playerChoice or str(countList11) in playerChoice or (int(playerChoice) % 7 == 0) or (int(playerChoice) % 11 == 0): #If player chooses a number with 7 or 11 in it
                print("Wrong!")
                countList.clear()
                count = 0
            else:
                print(f"{name}: {count}")
                countList.clear()
                playerCountList.clear()
        else:
            if "clap" in playerChoice and (int(count) % 7 == 0) or (int(count) % 11 == 0) and "7" in countList or countList11 in countList:
                print(f"{name}: clap")
                countList.clear()
                playerCountList.clear()
            elif "clap" in playerChoice and (int(count) % 7 != 0) or (int(count % 11 != 0)) and "7" in countList or countList11 in countList:
                print(f"{name}: clap")
                print("Wrong!")
                countList.clear()
                playerCountList.clear()
                count = 0
            else:
                print("What?")
                countList.clear()
                playerCountList.clear()
                count = 0

    else:
        if "7" in countList or countList11 in countList:
            print(f"{name}: Clap")
            countList.clear()
        elif (int(count) % 7 == 0) or (int(count) % 11 == 0):
            print(f"{name}: Clap")
            countList.clear()
        else:
            print(f"{name}: {count}")
            countList.clear()

    if nameListCount == 5:
        nameListCount = -1
    


