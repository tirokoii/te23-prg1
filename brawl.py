#Create a fight dice game with 2 players
# +Roles if time and brain power

#What roles?
#Bandit - There is a 20% chance to take a life from opponent
#Knight - There is a 20% chance to block an attack
#Priest - There is a 20% chance to heal yourself

#How?

#Create variables for player 1 and player 2 - if player 2 is no then computer
#Make game = true and set game rounds too 0
#Create an loop for player 2
#Create an loop for game = True

# To next time: Make list for weapons that get randomly chosen.
# Fix the not a valid class message. Aka 

from random import randint

print("Hello and welcome to the amazing brawl dice game!")
print("In this game you'll get to choose a class and name for your character and then you'll fight \1")

playerOneName = input("Player 1 please write your name: \n")

playerOneLife = 10
playerTwoLife = 10

playerTwo = False

game = True
gameRound = 0
playGame = "yes"
roles = ["knight", "priest", "bandit"]
yesNo = ["yes", "no"]
roleChoiceOne = 0
roleChoiceTwo = 0

while True:
    
    playerTwoName = input("Is there an second player? yes/no: \n")

    if playerTwoName.lower() == "yes":
        playerTwoName = input("Player 2 please write your name: \n")
        playerTwo = True
    elif playerTwoName.lower() == "no":
        print("\nYou'll now be playing with a computer.")
        playerTwoName = "computer"
        playerTwo = False
    else:
        print("Please write yes or no")
    
    if playerTwoName.lower() == "computer":
        computerClassRan = randint(1, 4)

        if computerClassRan == 1:
            roleChoiceTwo = "priest"
            break
        elif computerClassRan == 2:
            roleChoiceTwo = "knight"
            break
        elif computerClassRan == 3:
            roleChoiceTwo = "bandit"
            break
        elif computerClassRan == 4:
            roleChoiceTwo = "none"
            break



while roleChoiceOne == 0:

    roleChoiceOne = input("\nPlayer 1 do you want to choose an class? yes/no\n")

    if roleChoiceOne in yesNo:
        if roleChoiceOne == yesNo:
            roleChoiceOne = 0

        while roleChoiceOne in yesNo:
            if roleChoiceOne.lower() == "yes":
                print("\nThere are 3 different classes to choose from. \n")
                print("knight: Has a 10% CHANCE to dodge and 10% chance take 1 extra damage for running into the opponent.")
                print("bandit: Has a 20% CHANCE to steal the others win or loss.")
                print("priest: Has a 10% CHANCE to heal it self and 10% chance to heal the opponent. \n")
                print("If you don't want a class write in none below. ")

                roleChoiceOne = input("Please write which class you'll like to be: \n")
                if roleChoiceOne in roles:
                    print("Ok, fantastic! \n")
                elif roleChoiceOne.lower() == "no":
                    roleChoiceOne = "none"
                else:
                    print("Not a valid class.")
                    roleChoiceOne = 1

            elif roleChoiceOne.lower() == "no":
                roleChoiceOne = "none"
          #  else:
           #     print("Not a valid class.")
    else:
        print("Please write yes or no")
        roleChoiceOne = 0


while roleChoiceTwo == 0:

    if roleChoiceTwo == yesNo:
        roleChoiceTwo = 0
    else:
        roleChoiceTwo = input("\nPlayer 2 do you want to choose an class? yes/no\n")

    if roleChoiceTwo in yesNo:
        while roleChoiceTwo in yesNo:
            if playerTwo == True:
                if roleChoiceTwo.lower() == "yes":
                    print("\nThere are 3 different classes to choose from. \n")
                    print("knight: Has a 10% CHANCE to dodge and 10% chance take 1 extra damage for running into the opponent.")
                    print("bandit: Has a 20% CHANCE to steal the others win or loss.")
                    print("priest: Has a 10% CHANCE to heal itself and 10% chance to heal the opponent. \n")
                    print("If you don't want a class write in none below. ")

                    roleChoiceTwo = input("Please write which class you'll like to be: \n")
                    if roleChoiceTwo in roles:
                        print("Ok, great choice! \n")
                    elif roleChoiceTwo.lower() == "no":
                        roleChoiceTwo = "none"
                   # else:
                    #    print("Not a valid class.")
    else:
        print("Please write yes or no")
        roleChoiceTwo = 0

while playGame.lower() == "yes":

    while game == True:
        playerOneRoll = randint(1, 20)
        playerTwoRoll = randint(1, 20)

        priestHealOne = randint(1, 10) # 2 is heal and 3 is fail,
        knightBlockOne = randint(1, 10) # 4 is block and 5 is fail,
        banditStealOne = randint(1, 10) # 6 and 7 is steal and 8 if fail

        priestHealTwo = randint(1, 10) 
        knightBlockTwo = randint(1, 10)
        banditStealTwo = randint(1, 10)


        if gameRound == 1:
            print(f"You have now completed {gameRound} round!")
        elif gameRound > 1:
            print(f"You have now completed {gameRound} rounds!")       

        if playerOneRoll > playerTwoRoll:
            print(f"{playerOneName} begins to charge against {playerTwoName}!")
            gameRound += 1

            if roleChoiceOne == "priest":
                if priestHealOne == 2:
                        print(f"{playerOneName} is attempting to put up an healing spell")
                        print(f"A giant array begins to glow beneath {playerOneName}'s feet! \n")
                        playerOneLife += 1
                        print(f"{playerOneName} successfully healed them self. They now have {playerOneLife} lives")
                elif priestHealOne == 3:
                    print(f"{playerOneName} is attempting to put up an healing spell")
                    print(f"A giant array begins to glow beneath {playerOneName}'s feet! \n")
                    playerTwoLife += 1
                    print(f"Oh no, {playerOneName} failed to heal them self, they instead healed the opponent.")
                    print(f"{playerTwoName} now has {playerTwoLife} lives")

            elif roleChoiceOne == "knight":
                if playerOneRoll < playerTwoRoll:
                    if knightBlockOne == 4:
                        playerOneLife += 1
                        print(f"{playerTwoName} charges against {playerOneName} with a killing intent!")
                        print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                        print(f"{playerOneName} successfully blocked the attack!")
                    elif knightBlockOne == 5:
                        print(f"{playerTwoName} charges against {playerOneName} with a killing intent!")
                        print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                        print(f"A loud bonk echoes throughout the battleground, {playerOneName} is attacked by {playerTwoName} who bonks their head hard!")
                elif playerOneRoll == playerTwoRoll:
                    if knightBlockOne and knightBlockTwo == 4:
                        playerOneLife -= 1
                        playerTwoLife -= 1
                        print(f"{playerTwoName} charges against {playerOneName} with their shield!")
                        print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                        print(f"{playerOneName} and {playerTwoName} collides, both takes 1 damage! {playerOneName} has {playerOneLife} and {playerTwoName} has {playerTwoLife}.")

            elif roleChoiceOne == "bandit":   
                        
                        if banditStealOne == 6 or banditStealOne == 7:
                            print(f"The bandit {playerOneName} attempts to steal from {playerTwoName}!")
                            print(f"{playerOneName} successfully stole {playerTwoName}'s roll!")
                            banditRoll = playerOneRoll
                            playerOneRoll = playerTwoRoll
                            playerTwoRoll = banditRoll
                        elif banditStealOne == 8:
                            print(f"The bandit {playerOneName} attempts to steal from {playerTwoName}")
                            print(f"{playerOneName} fails to steal from the opponent")

            if roleChoiceTwo == "priest":
                if priestHealTwo == 2:
                        print(f"{playerTwoName} is attempting to put up an healing spell")
                        print(f"A giant array begins to glow beneath {playerTwoName}'s feet! \n")
                        playerTwoLife += 1
                        print(f"{playerTwoName} successfully healed them self. They now have {playerTwoLife} lives")
                elif priestHealTwo == 3:
                    print(f"{playerTwoName} is attempting to put up an healing spell")
                    print(f"A giant array begins to glow beneath {playerOneName}'s feet! \n")
                    playerOneLife += 1
                    print(f"Oh no, {playerTwoName} failed to heal them self, they instead healed the opponent.")
                    print(f"{playerOneName} now has {playerOneLife} lives")

            elif roleChoiceTwo == "knight":
                if playerTwoRoll > playerOneRoll:
                    if knightBlockTwo == 4:
                        playerTwoLife += 1
                        print(f"{playerOneName} charges against {playerTwoName} with a killing intent!")
                        print(f"{playerTwoName} takes out the shinning shield from the ground and is attempting to block {playerOneName}'s attack!")
                        print(f"{playerTwoName} successfully blocked the attack!")
                    elif knightBlockTwo == 5:
                        print(f"{playerOneName} charges against {playerTwoName} with a killing intent!")
                        print(f"{playerTwoName} takes out the shinning shield from the ground and is attempting to block {playerOneName}'s attack!")
                        print(f"A loud bonk echoes throughout the battleground, {playerTwoName} is attacked by {playerOneName} who bonks their head hard!")
                elif playerOneRoll == playerTwoRoll:
                    if knightBlockOne and knightBlockTwo == 4:
                        playerOneLife -= 1
                        playerTwoLife -= 1
                        print(f"{playerOneName} charges against {playerTwoName} with their shield!")
                        print(f"{playerTwoName} takes out the shinning shield from the ground and is attempting to block {playerOneName}'s attack!")
                        print(f"{playerTwoName} and {playerOneName} collides, both takes 1 damage! {playerTwoName} has {playerTwoLife} and {playerOneName} has {playerOneLife}.")

            elif roleChoiceTwo == "bandit":   
                        if banditStealTwo == 6 or banditStealTwo == 7:
                            print(f"The bandit {playerTwoName} attempts to steal from {playerOneName}!")
                            print(f"{playerTwoName} successfully stole {playerOneName}'s roll!")
                            banditRoll = playerTwoRoll
                            playerTwoRoll = playerOneRoll
                            playerOneRoll = banditRoll
                        elif banditStealTwo == 8:
                            print(f"The bandit {playerTwoName} attempts to steal from {playerOneName}")
                            print(f"{playerTwoName} fails to steal from the opponent")

            playerTwoLife -= 1
            print(f"Player 2 lost and now has {playerTwoLife} lives left.")
            input("Press enter")
        elif playerOneRoll < playerTwoRoll:
            gameRound += 1

            if roleChoiceOne == "priest":
                if priestHealOne == 2:
                        print(f"{playerOneName} is attempting to put up an healing spell")
                        print(f"A giant array begins to glow beneath {playerOneName}'s feet! \n")
                        playerOneLife += 1
                        print(f"{playerOneName} successfully healed them self. They now have {playerOneLife} lives")
                elif priestHealOne == 3:
                    print(f"{playerOneName} is attempting to put up an healing spell")
                    print(f"A giant array begins to glow beneath {playerOneName}'s feet! \n")
                    playerTwoLife += 1
                    print(f"Oh no, {playerOneName} failed to heal them self, they instead healed the opponent.")
                    print(f"{playerTwoName} now has {playerTwoLife} lives")

            elif roleChoiceOne == "knight":
                if playerOneRoll < playerTwoRoll:
                    if knightBlockOne == 4:
                        playerOneLife += 1
                        print(f"{playerTwoName} charges against {playerOneName} with a killing intent!")
                        print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                        print(f"{playerOneName} successfully blocked the attack!")
                    elif knightBlockOne == 5:
                        print(f"{playerTwoName} charges against {playerOneName} with a killing intent!")
                        print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                        print(f"A loud bonk echoes throughout the battleground, {playerOneName} is attacked by {playerTwoName} who bonks their head hard!")
                elif playerOneRoll == playerTwoRoll:
                    if knightBlockOne and knightBlockTwo == 4:
                        playerOneLife -= 1
                        playerTwoLife -= 1
                        print(f"{playerTwoName} charges against {playerOneName} with their shield!")
                        print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                        print(f"{playerOneName} and {playerTwoName} collides, both takes 1 damage! {playerOneName} has {playerOneLife} and {playerTwoName} has {playerTwoLife}.")

            elif roleChoiceOne == "bandit":   
                        
                        if banditStealOne == 6 or banditStealOne == 7:
                            print(f"The bandit {playerOneName} attempts to steal from {playerTwoName}!")
                            print(f"{playerOneName} successfully stole {playerTwoName}'s roll!")
                            banditRoll = playerOneRoll
                            playerOneRoll = playerTwoRoll
                            playerTwoRoll = banditRoll
                        elif banditStealOne == 8:
                            print(f"The bandit {playerOneName} attempts to steal from {playerTwoName}")
                            print(f"{playerOneName} fails to steal from the opponent")

            if roleChoiceTwo == "priest":
                if priestHealTwo == 2:
                        print(f"{playerTwoName} is attempting to put up an healing spell")
                        print(f"A giant array begins to glow beneath {playerTwoName}'s feet! \n")
                        playerTwoLife += 1
                        print(f"{playerTwoName} successfully healed them self. They now have {playerTwoLife} lives")
                elif priestHealTwo == 3:
                    print(f"{playerTwoName} is attempting to put up an healing spell")
                    print(f"A giant array begins to glow beneath {playerOneName}'s feet! \n")
                    playerOneLife += 1
                    print(f"Oh no, {playerTwoName} failed to heal them self, they instead healed the opponent.")
                    print(f"{playerOneName} now has {playerOneLife} lives")

            elif roleChoiceTwo == "knight":
                if playerTwoRoll < playerOneRoll:
                    if knightBlockTwo == 4:
                        playerTwoLife += 1
                        print(f"{playerOneName} charges against {playerTwoName} with a killing intent!")
                        print(f"{playerTwoName} takes out the shinning shield from the ground and is attempting to block {playerOneName}'s attack!")
                        print(f"{playerTwoName} successfully blocked the attack!")
                    elif knightBlockTwo == 5:
                        print(f"{playerOneName} charges against {playerTwoName} with a killing intent!")
                        print(f"{playerTwoName} takes out the shinning shield from the ground and is attempting to block {playerOneName}'s attack!")
                        print(f"A loud bonk echoes throughout the battleground, {playerTwoName} is attacked by {playerOneName} who bonks their head hard!")
                elif playerOneRoll == playerTwoRoll:
                    if knightBlockOne and knightBlockTwo == 4:
                        playerOneLife -= 1
                        playerTwoLife -= 1
                        print(f"{playerOneName} charges against {playerTwoName} with their shield!")
                        print(f"{playerTwoName} takes out the shinning shield from the ground and is attempting to block {playerOneName}'s attack!")
                        print(f"{playerTwoName} and {playerOneName} collides, both takes 1 damage! {playerTwoName} has {playerTwoLife} and {playerOneName} has {playerOneLife}.")

            elif roleChoiceTwo == "bandit":   
                        if banditStealTwo == 6 or banditStealTwo == 7:
                            print(f"The bandit {playerTwoName} attempts to steal from {playerOneName}!")
                            print(f"{playerTwoName} successfully stole {playerOneName}'s roll!")
                            banditRoll = playerTwoRoll
                            playerTwoRoll = playerOneRoll
                            playerOneRoll = banditRoll
                        elif banditStealTwo == 8:
                            print(f"The bandit {playerTwoName} attempts to steal from {playerOneName}")
                            print(f"{playerTwoName} fails to steal from the opponent")
 
            playerOneLife -= 1
            print(f"Player 1 lost and now has {playerOneLife} lives left.")
            input("Press enter")

        else:
            gameRound += 1
            print("Both players tried to attack each other, but it seems like luck was on no ones side. I wish you the best of luck in the next round!")
            input("Press enter")

        if playerOneLife == 0:
            print(f"In a harsh battle {playerOneName} persisted and won. Congratulations to your victory over {playerTwoName}!")
            game = False
        elif playerTwoLife == 0:
            print(f"In a harsh battle {playerOneName} persisted and won. Congratulations to your victory over {playerTwoName}!")
            game = False

    playGame = input("Would you like to play again? yes/no: ")
    if playGame.lower() == "yes":
        game = True
    else: 
        game = False

