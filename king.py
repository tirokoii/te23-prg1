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

allowedDices = [4, 6, 8, 10, 12, 20]
playGame = "yes"

playerOneName = input("Player 1 name: ")
playerTwoName = input("Player 2 name: ")

while True:
     rounds =  input("How many round would you like to play?")

     if rounds.isdigit:
          rounds = int(rounds)
          break
     else:
          print

while True:

        diceSideChoice = input("please choose between the dices, 4, 6, 8, 10, 12, 20: ")

        if diceSideChoice == 4 or 6 or 8 or 10 or 12 or 20:
            diceSideChoice = int(diceSideChoice) #Makes dice choice into integer
            break
        else:
            print("Please choose a valid number")


while playGame.lower() == "yes":

        gameRound += 1
        playerOne = randint(1, diceSideChoice)
        playerTwo = randint(1, diceSideChoice)

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

playGame = input("Do you want to play again? [yes/no]: ")
        
        
        


#To do:
#Choose amount of rounds
#Choose between different dices. Fix to a specific set of dices.

