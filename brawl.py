#Create a fight dice game with 2 players
# +Roles if time

#What roles?
#Bandit - There is a 20% chance to take a life from opponent
#Knight - There is a 20% chance to block an attack
#Priest - There is a 20% chance to heal yourself

#How?

#Create variables for player 1 and player 2 - if player 2 is no then computer
#Make game = true and set game rounds too 0
#Create an loop for player 2
#Create an loop for game = True

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

        roleChoiceOne = input("Player one do you want to choose an class? yes/no ")
        if roleChoiceOne.lower() == "yes":
            print("\nThere are 3 different classes to choose from. \n")
            print("knight: Has a 10% CHANCE to dodge or take 1 extra damage for running into the opponent.")
            print("bandit: Has a 10% CHANCE to steal the others win or loss.")
            print("priest: Has a 10% CHANCE to heal it self or heal the opponent. \n")
            print("If you don't want a class write in none below. ")

            input("Please write which class you'll like to be: \n")
        elif roleChoice.lower() == "no":
            roleChoice = "none"
        else:
            print("Not a valid class.")

        roleChoiceTwo = input("Player one do you want to choose an class? yes/no ")
        if playerTwo == True:
            if roleChoiceTwo.lower() == "yes":
                print("\nThere are 3 different classes to choose from. \n")
                print("knight: Has a 10% CHANCE to dodge or take 1 extra damage for running into the opponent.")
                print("bandit: Has a 10% CHANCE to steal the others win or loss.")
                print("priest: Has a 10% CHANCE to heal it self or heal the opponent. \n")
                print("If you don't want a class write in none below. ")

                roleChoiceTwo = input("Please write which class you'll like to be: \n")
                if roleChoiceTwo == "knight" or "bandit" or "priest":
                    print("Ok")
        elif roleChoiceTwo.lower() == "no":
            roleChoiceTwo = "none"
        else:
            print("Not a valid class.")

while playGame.lower() == "yes":

    priestHealOne = (1, 10)
    knightBlockOne = (1, 10)
    banditStealOne = (1, 10)
    noAbility = (1)

    priestHealTwo = (1, 10)
    knightBlockTwo = (1, 10)
    banditStealTwo = (1, 10)
    noAbility = (1)

    while game == True:
        gameRound += 1
        playerOneRoll = randint(1, 12)
        playerTwoRoll = randint(1, 12)

        if gameRound == 1:
            print(f"You have now completed {gameRound} round!")
        elif gameRound > 1:
            print(f"You have now completed {gameRound} rounds!")
             

        if playerOneRoll > playerTwoRoll:
            
            playerTwoLife -= 1
            print(f"Player two lost and now has {playerTwoLife} lives left.")
            input("Press enter")
        elif playerOneRoll < playerTwoRoll:
            playerOneLife -= 1
            print(f"Player One lost and now has {playerOneLife} lives left.")
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

