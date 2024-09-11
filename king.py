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

playerOneName = input("Player 1 name: ")
playerTwoName = input("Player 2 name: ")

while playerOneScore < 3:

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

    #play_game = input("Do you want to play again? {yes/no} ")
if playerOneScore > playerTwoScore:
    print(f"Congrats {playerOneName} won the game!")
else:
    print(f"Congrats {playerTwoName} won the game!")



