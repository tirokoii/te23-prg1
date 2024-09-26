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
print("In this game you'll get to choose a class and name for your character.")

playerOneName = input("Player 1 please write your name: ")

playerOneLife = 10
playerTwoLife = 10

game = True
gameRound = 0
playGame = "yes"

knightRole = randint(1, 5) #Rolls chance, if rolls under or equals to 1 then it happens 
priestRole = randint(1, 5)
banditRole = randint(1, 5)



while True:
    playerTwoName = input("Is there an second player? yes/no: ")

    if playerTwoName.lower() == "yes":

        playerTwoName = input("Player 2 please write your name: ")
        break
    elif playerTwoName.lower() == "no":
        playerTwoName = "computer"
        break
    else:
        print("Please write y or n")

while playGame.lower() == "yes":

    while game == True:
        gameRound += 1
        gameRoundAnn = print(f"You have now completed {gameRound} rounds!")
        playerOneRoll = randint(1, 12)
        playerTwoRoll = randint(1, 12)

        if playerOneRoll > playerTwoRoll:
            playerTwoLife -= 1
            print(f"Player two lost and now has {playerTwoLife} lives left.")
            input("")
        elif playerOneRoll < playerTwoRoll:
            playerOneLife -= 1
            print(f"Player One lost and now has {playerOneLife} lives left.")
            input("")
        else:
            print("It was a tie. Good luck in the next round.")
            input("")

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

