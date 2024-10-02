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

#How roles?
#

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
        break
    elif playerTwoName.lower() == "no":
        playerTwoName = "computer"
        playerTwo = False
        break
    else:
        print("Please write y or n")
    
    if playerTwoName.lower() == "computer":
        computerClass = randint(1, 4)

        if computerClass == 1:
            computerClass = "priest"
        elif computerClass == 2:
            computerClass = "knight"
        elif computerClass == 3:
            computerClass = "bandit"
        elif computerClass == 4:
            computerClass = "noClass"



while roleChoiceOne == 0:

    roleChoiceOne = input("Player 1 do you want to choose an class? yes/no ")

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
             #   print("Not a valid class.")
    else:
        print("Please write yes or no")
        roleChoiceOne = 0


while roleChoiceTwo == 0:

    if roleChoiceTwo == yesNo:
        roleChoiceTwo = 0
    else:
        roleChoiceTwo = input("Player 2 do you want to choose an class? yes/no ")

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
        gameRound += 1
        playerOneRoll = randint(1, 12)
        playerTwoRoll = randint(1, 12)

        priestHealOne = (1, 10) # 2 is heal and 3 is fail,
        knightBlockOne = (1, 10) # 4 is block and 5 is fail,
        banditStealOne = (1, 10) # 6 and 7 is steal,
        noAbility = (1)

        priestHealTwo = (1, 10) 
        knightBlockTwo = (1, 10)
        banditStealTwo = (1, 10)
        noAbility = (1)

        if roleChoiceOne == "priest":
            if priestHealOne == "2":
                print(f"{playerOneName} is attempting to put up an healing spell")
                print(f"A giant array begins to glow beneath {playerOneName}'s feet! \n")
                playerOneLife += 1
                print(f"{playerOneName} successfully healed them self. They now have {playerOneLife} lives")
            elif priestHealOne == 3:
                print(f"{playerOneName} is attempting to put up an healing spell")
                print(f"A giant array begins to glow beneath {playerTwoName}'s feet! \n")
                playerTwoLife += 1
                print(f"Oh no, {playerOneName} failed to heal them self, they instead healed the opponent.")
                print(f"{playerTwoLife} now has {playerTwoLife} lives")
        elif roleChoiceOne == "knight":
            if playerOneRoll < playerTwoRoll:
                if knightBlockOne == 4:
                    playerOneLife += 1
                    print(f"{playerTwo} charges against {playerOneName} with a killing intent!")
                    print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                    print(f"{playerOneName} successfully blocked the attack!")
                elif knightBlockOne == 5:
                    print(f"{playerTwo} charges against {playerOneName} with a killing intent!")
                    print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                    print(f"A loud bonk kan be heard as {playerOneName} first drops the shield on their toe and {playerTwoName} attacks, hitting the other players head!")
            elif playerOneRoll == playerTwoRoll:
                if knightBlockOne and knightBlockTwo == 4:
                    print(f"{playerTwo} charges against {playerOneName} with his shield!")
                    print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")
                    print(f"{playerOneName} and {playerTwoName} collides")
                elif knightBlockOne == 5:
                    print(f"{playerTwo} charges against {playerOneName} with a killing intent!")
                    print(f"{playerOneName} takes out the shinning shield from the ground and is attempting to block {playerTwoName}'s attack!")

        if gameRound == 1:
            print(f"You have now completed {gameRound} round!")
        elif gameRound > 1:
            print(f"You have now completed {gameRound} rounds!")       

        if playerOneRoll > playerTwoRoll:
            
            playerTwoLife -= 1
            print(f"Player 2 lost and now has {playerTwoLife} lives left.")
            input("Press enter")
        elif playerOneRoll < playerTwoRoll:
            playerOneLife -= 1
            print(f"Player 1 lost and now has {playerOneLife} lives left.")
            input("Press enter")
        else:
            print("It was a tie. Good luck in the next round.")
            input("Press enter")

        if playerOneLife == 0:
            print(f"Good work {playerTwoName} you won against {playerOneName}!")
            game = False
        elif playerTwoLife == 0:
            print(f"Good work {playerOneName} you won against {playerTwoName}")
            game = False

    playGame = input("Would you like to play again? yes/no: ")
    if playGame.lower() == "yes":
        game = True
    else: 
        game = False

