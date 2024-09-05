# Decide if its odd or even
# Roll the dice
# Winner is what was decided in the beginning

from random import randint

rule = input("odd or even?: ") #Sets a rule 
computer = randint(1, 6) #Randomize roll
player = randint(1, 6)
odd = (1, 3, 5) #Creates a function for when the numbers count as odd and even
even = (2, 4, 6)


if rule == "odd": #Implements the rule and sets if the rule is the same as odd
    computer_result = computer in odd
    player_result = player in odd
    if computer_result == player_result:
        print(f"Computer: {computer}, Player: {player}, It's a draw")
    elif computer_result:
        print(f"Computer: {computer}, Player {player}, Computer wins")
    else:
        print(f"Computer: {computer}, Player: {player}, Player wins")

if rule == "even": #Implements the rule and sets if the rule is the same as odd
    computer_result = computer in even
    player_result = player in even
    if computer_result == player_result:
        print(f"Computer: {computer}, Player: {player}, It's a draw")
    elif computer_result:
        print(f"Computer: {computer}, Player {player}, Computer wins")
    else:
        print(f"Computer: {computer}, Player: {player}, Player wins")




