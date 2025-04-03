from random import randint

guess = 0 #Sets guess to base of 0
answer = randint(1, 10) #Randomizes an number

while guess != answer: #Creates loop where until guess is equal to answer the user has to continue guess

    guess = int(input("Guess a number between 1 and 10: ")) #Asks the user to guess what answer is
    if guess > answer:
         print("You guessed to high") #If guess is higher than answer tells the player
    elif guess < answer:
        print("You guessed to low")
    else:
         print("You won")