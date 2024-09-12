#Rules
#Two players
#Player 1 rolls dice
#Player 2 rolls dice 
#Who rolled highest
#Highest wins
#Repeat till someone gets tre points
#

from random import randint

playerOneScore = 0
playerTwoScore = 0
gameRound = 0

d4 = randint(1, 4)
d6 = randint(1, 6)
d8 = randint(1, 8)
d10 = randint(1, 10)
d12 = randint(1, 12)
d20 = randint(1, 20)

diceList = ["d4", "d6", "d8", "d10", "d12", "d20"]


playGame = "yes"

playerOneName = input("Player 1 name: ")
playerTwoName = input("Player 2 name: ")

while playGame.lower() == "yes":

    diceChoice = input("please choose between the dices, d4, d6, d8, d10, dd12, d20: ")

    if diceChoice == diceList[0]:

        gameRound += 1
        playerOne = randint(1, 6)
        playerTwo = randint(1, 6)

        if playerOne > playerTwo:
            rollResults = playerOne - playerTwo
        elif playerOne < playerTwo:
            rollResults = playerTwo - playerOne
        else:
            rollResults = 0

        if playerOne > playerTwo:
            print(f"{playerOneName} won with {rollResults} more points than {playerTwoName}")
            playerOneScore += 1
        elif playerOne < playerTwo:
            print(f"{playerTwoName} won with {rollResults} more points than {playerOneName}")
            playerTwoScore += 1
        else:
            print(f"It was a draw between {playerOneName} and {playerTwoName}")
        
        if playerOneScore >= 2:
            print(f"Congrats {playerOneName} won the game!")
            playGame = "no"
        elif playerTwoScore >= 2:
            print(f"Congrats {playerTwoName} won the game!")
            playGame = "no"
        elif gameRound >= 3:
            print(f"After {gameRound} rounds nobody has won. {playerOneName} had {playerOneScore} and {playerTwoName} had {playerTwoScore}")
            playGame = "no"

        elif diceChoice == diceList[1]
    
playGame = input("Do you want to play again? [yes/no]: ")




#To do:

#Somehow won't run the loop. Need to fix¨
#Choose amount of rounds 
#Choose between different dice

