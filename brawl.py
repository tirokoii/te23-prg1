#Create a fight dice game with 2 players
# +Roles if time and brain power

#What roles?
#Bandit - There is a 20% chance to take a life from opponent
#Knight - There is a 20% chance to block an attack
#Priest - There is a 20% chance to heal yourself
#Barbarians - There is a 10% chance for crit hit

#How?

#Create variables for player 1 and player 2 - if player 2 is no then computer
#Make game = true and set game rounds too 0
#Create an loop for player 2
#Create an loop for game = True

# To next time: Make list for weapons that get randomly chosen - Fixed
# Fix the not a valid class message. - Fixed. 
#Fix play game again - Fixed?



from random import randint
import random, time
from colorama import init
init()
from colorama import Fore

game = True

while game == True:

    print(Fore.WHITE +"\nHello and welcome to the amazing brawl dice game!")
    print("In this game you'll get to choose a class and name for your character and then fight against an opponent \003")
    time.sleep (5)

    playerOneName = input(Fore.CYAN + "\nPlayer 1 please write your name: \n")

    playerOneLife = 10
    playerTwoLife = 10

    playerTwo = False

    gameRound = 0
    playGame = "yes"
    roles = ["knight", "priest", "bandit"]
    randomWeapon = ["sword", "gummi duck", "axe", "bone", "Spear", "cat", "lollipop", "shield", "pistol", "hammer", "scythe", "bow"]
    weapon = random.choice(randomWeapon)
    yesNo = ["yes", "no"]
    roleChoiceOne = 0
    roleChoiceTwo = 0
    roleWrong = True

    while True:
        playerTwoName = input(Fore.WHITE + "\nIs there an second player? yes/no: \n")

        if playerTwoName.lower() == "yes" or playerTwoName.lower() == "y":
            playerTwoName = input(Fore.LIGHTMAGENTA_EX + "\nPlayer 2 please write your name: \n")
            playerTwo = True
            break
        elif playerTwoName.lower() == "no" or playerTwoName.lower() == "n":
            print("\nYou'll now be playing with a computer.")
            playerTwoName = "computer"
            playerTwo = False
            break
        else:
            print("Please write yes or no")
        
    if playerTwoName.lower() == "computer":
        computerClassRan = randint(1, 4)

        if computerClassRan == 1:
            roleChoiceTwo = "priest"
            
        elif computerClassRan == 2:
            roleChoiceTwo = "knight"
            
        elif computerClassRan == 3:
            roleChoiceTwo = "bandit"
            
        elif computerClassRan == 4:
            roleChoiceTwo = "none"
            



    while roleChoiceOne == 0:

        roleChoiceOne = input(Fore.CYAN + "\nPlayer 1 do you want to choose an class? yes/no\n")
        time.sleep(1)

        if roleChoiceOne.lower() == "yes" or roleChoiceOne.lower() == "y" or roleChoiceOne.lower() == "no" or roleChoiceOne.lower() == "n":

            while True:
                if roleChoiceOne.lower() == "yes" or roleChoiceOne.lower() == "y":
                    while roleWrong == True: 
                        print("\n\n\n\n")
                        print(Fore.WHITE + "\nThere are 3 different classes to choose from. \n")
                        print("knight: Has a 10% CHANCE to dodge and 10% chance take 1 extra damage for running into the opponent.")
                        print("bandit: Has a 20% CHANCE to steal the others win or loss.")
                        print("priest: Has a 10% CHANCE to heal it self and 10% chance to heal the opponent. \n")
                        print("If you don't want a class write in none below.\n")
                        roleChoiceOne = input(Fore.CYAN + "Please write which class you'll like to be: \n")
                        if roleChoiceOne in roles:
                            print(Fore.WHITE + "Ok, fantastic! \n")
                            time.sleep(1)
                            roleWrong = False
                            break
                        elif roleChoiceOne.lower() == "no" or roleChoiceOne.lower() == "n":
                            roleChoiceOne = "none"
                            roleWrong = False
                        else:
                            print("Not a valid class.\n")
                            time.sleep(1)
                            
                elif roleChoiceOne.lower() == "no" or roleChoiceOne.lower() == "n":
                    roleChoiceOne = "none"
                break
        else:
            print("Please write yes or no")
            roleChoiceOne = 0


    while roleChoiceTwo == 0:

        if playerTwo == True:
            roleChoiceTwo = input(Fore.LIGHTMAGENTA_EX + "\nPlayer 2 do you want to choose an class? yes/no\n")
            time.sleep(1)

            if roleChoiceTwo.lower() == "yes" or roleChoiceTwo.lower() == "y" or roleChoiceTwo.lower() == "no" or roleChoiceTwo.lower() == "n":

                while True:
                        if roleChoiceTwo.lower() == "yes" or roleChoiceTwo.lower() == "y":
                            while roleWrong == False:

                                print("\n\n\n\n")
                                print(Fore.WHITE + "\nThere are 3 different classes to choose from. \n")
                                print("knight: Has a 10% CHANCE to dodge and 10% chance take 1 extra damage for running into the opponent.")
                                print("bandit: Has a 20% CHANCE to steal the others win or loss.")
                                print("priest: Has a 10% CHANCE to heal itself and 10% chance to heal the opponent. \n")
                                print("If you don't want a class write in none below. ")

                                roleChoiceTwo = input(Fore.LIGHTMAGENTA_EX + "Please write which class you'll like to be: \n")
                                if roleChoiceTwo in roles:
                                    print(Fore.WHITE + "Ok, great choice! \n")
                                    input("Press enter")
                                    roleWrong = True
                                    break
                                elif roleChoiceTwo.lower() == "no" or roleChoiceTwo.lower() == "n":
                                    roleChoiceTwo = "none"
                                    roleWrong = True
                                else:
                                    print("Not a valid class.\n")
                        break
            else:
                print("Please write yes or no")
                roleChoiceTwo = 0

    while playGame.lower() == "yes" or playGame.lower() == "y":

        while True:
            playerOneRoll = randint(1, 20)
            playerTwoRoll = randint(1, 20)

            priestHealOne = randint(1, 10) # 2 is heal and 3 is fail,
            knightBlockOne = randint(1, 10) # 4 is block and 5 is fail,
            banditStealOne = randint(1, 10) # 6 and 7 is steal and 8 if fail

            priestHealTwo = randint(1, 10) 
            knightBlockTwo = randint(1, 10)
            banditStealTwo = randint(1, 10)


            if playerOneRoll > playerTwoRoll:
                gameRound += 1
                print(Fore.CYAN + f"{playerOneName} begins to charge against {playerTwoName} with an {weapon} in their hand!")

                if roleChoiceOne == "priest":
                    if priestHealOne == 2:
                            print(Fore.CYAN + f"{playerOneName} is attempting to put up an healing spell")
                            print(f"A giant array begins to glow beneath {playerOneName}'s feet! \n")
                            playerOneLife += 1
                            print(Fore.GREEN + f"{playerOneName} successfully healed them self. They now have {playerOneLife} lives")
                    elif priestHealOne == 3:
                        print(f"{playerOneName} is attempting to put up an healing spell")
                        print(f"A giant array begins to glow beneath {playerOneName}'s feet! \n")
                        playerTwoLife += 1
                        print(Fore.RED + f"Oh no, {playerOneName} failed to heal them self, they instead healed the opponent.")
                        print(Fore.CYAN + f"{playerTwoName} now has {playerTwoLife} lives")

                elif roleChoiceOne == "knight":
                    if playerOneRoll < playerTwoRoll:
                        if knightBlockOne == 4:
                            playerOneLife += 1
                            print(Fore.CYAN + f"{playerTwoName} charges against {playerOneName} with a killing intent!")
                            print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                            print(Fore.GREEN + f"{playerOneName} successfully blocked the attack!")
                        elif knightBlockOne == 5:
                            print(f"{playerTwoName} charges against {playerOneName} with a killing intent!")
                            print(Fore.CYAN + f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                            print(Fore.RED + f"A loud bonk echoes throughout the battleground, {playerOneName} is attacked by {playerTwoName} with an {weapon}!")
                    elif playerOneRoll == playerTwoRoll:
                        if knightBlockOne and knightBlockTwo == 4:
                            playerOneLife -= 1
                            playerTwoLife -= 1
                            print(Fore.CYAN + f"{playerTwoName} charges against {playerOneName} with their shield!")
                            print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                            print(Fore.RED + f"{playerOneName} and {playerTwoName} collides, both takes 1 damage! {playerOneName} has {playerOneLife} and {playerTwoName} has {playerTwoLife}.")

                elif roleChoiceOne == "bandit":   
                            
                            if banditStealOne == 6 or banditStealOne == 7:
                                print(Fore.CYAN + f"The bandit {playerOneName} attempts to steal from {playerTwoName}!")
                                print(Fore.GREEN + f"{playerOneName} successfully stole {playerTwoName}'s roll!")
                                banditRoll = playerOneRoll
                                playerOneRoll = playerTwoRoll
                                playerTwoRoll = banditRoll
                            elif banditStealOne == 8:
                                print(Fore.CYAN + f"The bandit {playerOneName} attempts to steal from {playerTwoName}")
                                print(Fore.RED + f"{playerOneName} fails to steal from the opponent")

                if roleChoiceTwo == "priest":
                    if priestHealTwo == 2:
                            print(Fore.LIGHTMAGENTA_EX + f"{playerTwoName} is attempting to put up an healing spell")
                            print(f"A giant array begins to glow beneath {playerTwoName}'s feet! \n")
                            playerTwoLife += 1
                            print(Fore.GREEN + f"{playerTwoName} successfully healed them self. They now have {playerTwoLife} lives")
                    elif priestHealTwo == 3:
                        print(Fore.LIGHTMAGENTA_EX + f"{playerTwoName} is attempting to put up an healing spell")
                        print(f"A giant array begins to glow beneath {playerOneName}'s feet! \n")
                        playerOneLife += 1
                        print(Fore.RED + f"Oh no, {playerTwoName} failed to heal them self, they instead healed the opponent.")
                        print(Fore.LIGHTMAGENTA_EX + f"{playerOneName} now has {playerOneLife} lives")

                elif roleChoiceTwo == "knight":
                    if playerTwoRoll > playerOneRoll:
                        if knightBlockTwo == 4:
                            playerTwoLife += 1
                            print(Fore.LIGHTMAGENTA_EX + f"{playerOneName} charges against {playerTwoName} with a killing intent!")
                            print(f"{playerTwoName} takes out the shinning shield from the ground and is attempting to block {playerOneName}'s attack!")
                            print(Fore.GREEN + f"{playerTwoName} successfully blocked the attack!")
                        elif knightBlockTwo == 5:
                            print(Fore.LIGHTMAGENTA_EX + f"{playerOneName} charges against {playerTwoName} with a killing intent!")
                            print(f"{playerTwoName} takes out the shinning shield from the ground and is attempting to block {playerOneName}'s attack!")
                            print(Fore.RED + f"A loud bonk echoes throughout the battleground, {playerTwoName} is attacked by {playerOneName} with an {weapon}!")
                    elif playerOneRoll == playerTwoRoll:
                        if knightBlockOne and knightBlockTwo == 4:
                            playerOneLife -= 1
                            playerTwoLife -= 1
                            print(Fore.LIGHTMAGENTA_EX + f"{playerOneName} charges against {playerTwoName} with their shield!")
                            print(f"{playerTwoName} takes out the shinning shield from the ground and is attempting to block {playerOneName}'s attack!")
                            print(Fore.RED + f"{playerTwoName} and {playerOneName} collides, both takes 1 damage! {playerTwoName} has {playerTwoLife} and {playerOneName} has {playerOneLife}.")

                elif roleChoiceTwo == "bandit":   
                            if banditStealTwo == 6 or banditStealTwo == 7:
                                print(Fore.LIGHTMAGENTA_EX + f"The bandit {playerTwoName} attempts to steal from {playerOneName}!")
                                print(Fore.GREEN + f"{playerTwoName} successfully stole {playerOneName}'s roll!")
                                banditRoll = playerTwoRoll
                                playerTwoRoll = playerOneRoll
                                playerOneRoll = banditRoll
                            elif banditStealTwo == 8:
                                print(Fore.LIGHTMAGENTA_EX + f"The bandit {playerTwoName} attempts to steal from {playerOneName}")
                                print(Fore.RED + f"{playerTwoName} fails to steal from the opponent")

                playerTwoLife -= 1
                print(Fore.WHITE + f"{playerOneName} hit {playerTwoName} in the face with an {weapon}")
                print(Fore.WHITE + f"{playerTwoName} lost terribly to {playerOneName} and now has {playerTwoLife} lives left.")

                if gameRound == 1:
                    print(Fore.WHITE + f"You have now completed {gameRound} round!")
                elif gameRound > 1:
                    print(Fore.WHITE + f"You have now completed {gameRound} rounds!")  
                    
                input("Press enter\n")
            elif playerOneRoll < playerTwoRoll:
                gameRound += 1
                print(Fore.LIGHTMAGENTA_EX + f"{playerTwoName} begins to charge against {playerOneName} with an {weapon} in their hand!")

                if roleChoiceOne == "priest":
                    if priestHealOne == 2:
                            print(Fore.CYAN+ f"{playerOneName} is attempting to put up an healing spell")
                            print(f"A giant array begins to glow beneath {playerOneName}'s feet!")
                            print(Fore.GREEN + f"{playerOneName} successfully healed them self. They now have {playerOneLife} lives\n")
                            playerOneLife += 1
                    elif priestHealOne == 3:
                        print(Fore.CYAN + f"{playerOneName} is attempting to put up an healing spell")
                        print(f"A giant array begins to glow beneath {playerOneName}'s feet! \n")
                        playerTwoLife += 1
                        print(Fore.RED + f"Oh no, {playerOneName} failed to heal them self, they instead healed the opponent.")
                        print(f"{playerTwoName} now has {playerTwoLife} lives\n")

                elif roleChoiceOne == "knight":
                    if playerOneRoll < playerTwoRoll:
                        if knightBlockOne == 4:
                            playerOneLife += 1
                            print(Fore.CYAN + f"{playerTwoName} charges against {playerOneName} with a killing intent!")
                            print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                            print(Fore.GREEN + f"{playerOneName} successfully blocked the attack!\n")
                        elif knightBlockOne == 5:
                            print(Fore.CYAN + f"{playerTwoName} charges against {playerOneName} with a killing intent!")
                            print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                            print(Fore.RED + f"A loud bonk echoes throughout the battleground, {playerOneName} is attacked by {playerTwoName} with an {weapon}!\n")
                    elif playerOneRoll == playerTwoRoll:
                        if knightBlockOne and knightBlockTwo == 4:
                            playerOneLife -= 1
                            playerTwoLife -= 1
                            print(Fore.CYAN + f"{playerTwoName} charges against {playerOneName} with their shield!")
                            print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                            print(Fore.RED + f"{playerOneName} and {playerTwoName} collides, both takes 1 damage! {playerOneName} has {playerOneLife} and {playerTwoName} has {playerTwoLife}.\n")

                elif roleChoiceOne == "bandit":   
                            
                            if banditStealOne == 6 or banditStealOne == 7:
                                print(Fore.CYAN + f"The bandit {playerOneName} attempts to steal from {playerTwoName}!")
                                print(Fore.GREEN + f"{playerOneName} successfully stole {playerTwoName}'s roll!\n")
                                banditRoll = playerOneRoll
                                playerOneRoll = playerTwoRoll
                                playerTwoRoll = banditRoll
                            elif banditStealOne == 8:
                                print(Fore.CYAN + f"The bandit {playerOneName} attempts to steal from {playerTwoName}")
                                print(Fore.RED + f"{playerOneName} fails to steal from the opponent\n")

                if roleChoiceTwo == "priest":
                    if priestHealTwo == 2:
                            print(Fore.LIGHTMAGENTA_EX + f"{playerTwoName} is attempting to put up an healing spell")
                            print(f"A giant array begins to glow beneath {playerTwoName}'s feet! \n")
                            playerTwoLife += 1
                            print(Fore.RED + f"{playerTwoName} successfully healed them self. They now have {playerTwoLife} lives\n")
                    elif priestHealTwo == 3:
                        print(Fore.LIGHTMAGENTA_EX + f"{playerTwoName} is attempting to put up an healing spell")
                        print(f"A giant array begins to glow beneath {playerOneName}'s feet! \n")
                        playerOneLife += 1
                        print(Fore.RED + f"Oh no, {playerTwoName} failed to heal them self, they instead healed the opponent.")
                        print(f"{playerOneName} now has {playerOneLife} lives\n")

                elif roleChoiceTwo == "knight":
                    if playerTwoRoll < playerOneRoll:
                        if knightBlockTwo == 4:
                            playerTwoLife += 1
                            print(Fore.LIGHTMAGENTA_EX + f"{playerOneName} charges against {playerTwoName} with a killing intent!")
                            print(f"{playerTwoName} takes out the shinning shield from the ground and is attempting to block {playerOneName}'s attack!")
                            print(Fore.GREEN + f"{playerTwoName} successfully blocked the attack!\n")
                        elif knightBlockTwo == 5:
                            print(Fore.LIGHTMAGENTA_EX + f"{playerOneName} charges against {playerTwoName} with a killing intent!")
                            print(f"{playerTwoName} takes out the shinning shield from the ground and is attempting to block {playerOneName}'s attack!")
                            print(Fore.LIGHTMAGENTA_EX + f"A loud bonk echoes throughout the battleground, {playerTwoName} is attacked by {playerOneName} with an {weapon}!\n")
                    elif playerOneRoll == playerTwoRoll:
                        if knightBlockOne and knightBlockTwo == 4:
                            playerOneLife -= 1
                            playerTwoLife -= 1
                            print(Fore.LIGHTMAGENTA_EX + f"{playerOneName} charges against {playerTwoName} with their shield!")
                            print(f"{playerTwoName} takes out the shinning shield from the ground and is attempting to block {playerOneName}'s attack!")
                            print(Fore.LIGHTMAGENTA_EX + f"{playerTwoName} and {playerOneName} collides, both takes 1 damage! {playerTwoName} has {playerTwoLife} and {playerOneName} has {playerOneLife}.\n")

                elif roleChoiceTwo == "bandit":   
                            if banditStealTwo == 6 or banditStealTwo == 7:
                                print(Fore.LIGHTMAGENTA_EX + f"The bandit {playerTwoName} attempts to steal from {playerOneName}!")
                                print(Fore.GREEN + f"{playerTwoName} successfully stole {playerOneName}'s roll!\n")
                                banditRoll = playerTwoRoll
                                playerTwoRoll = playerOneRoll
                                playerOneRoll = banditRoll
                            elif banditStealTwo == 8:
                                print(Fore.LIGHTMAGENTA_EX + f"The bandit {playerTwoName} attempts to steal from {playerOneName}")
                                print(Fore.GREEN + f"{playerTwoName} fails to steal from the opponent\n")
    
                playerOneLife -= 1
                print(Fore.WHITE + f"{playerTwoName} hit {playerOneName} in the face with an {weapon}")
                print(Fore.WHITE + f"{playerOneName} lost hard time to and now has {playerOneLife} lives left.\n")

                if gameRound == 1:
                    print(f"You have now completed {gameRound} round!")
                elif gameRound > 1:
                    print(f"You have now completed {gameRound} rounds!")       

                input("Press enter\n")

            else:
                gameRound += 1
                print("Both players tried to attack each other, but it seems like luck was on no ones side. I wish you the best of luck in the next round!")
                input("Press enter \n")

            if playerOneLife == 0:
                print(f"In a harsh battle between two masters {playerOneName} persisted and rose the victory flag. Congratulations to your victory over {playerTwoName}!")
                print(f"{playerOneName} you are now officially better then {playerTwoName}")
                game = False
                break
            elif playerTwoLife == 0:
                print(f"In a harsh battle between two masters {playerOneName} persisted and rose the victory flag. Congratulations to your victory over {playerTwoName}!")
                print(f"{playerOneName} you are now officially better then {playerTwoName}")
                game = False
                break

playGame = input("Would you like to play again? yes/no: ")
if playGame.lower() == "yes":
    game = True
else: 
    game = False