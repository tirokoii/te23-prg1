answer = input("Write an integer: ") #Prints a text that the user can answer to
number = int(answer) #Gives the answer from above a value of a integer
square = number * number #Times squares the number
print("Your number squared is", square) #Prints the answer

answer2 = input("Write an number: ")
number2 = float(answer2) #Can now write any numbers
square2 = number2 * number2
print(f"Your number squared is {square2:.2f}") #Keeps the decimals to 2

i = 19
print(f"Results:{i}")
j = 107
print(f"Results:{j:5}")
k = 4
print(f"Results:{k:03}")