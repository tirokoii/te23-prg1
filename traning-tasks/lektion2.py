

print("Hello and welcome to my program")

while True: #Creates a loop

    firstName = input("Please write your first name: ")

    if firstName.isalpha(): #Checks if firstName is written with letters
        print(f"Good day {firstName}. Thank you for gracing me with your presence.") 
        break #Breaks the loop
    else: #If the firstName isn't written with letters continues the loop
        print("Please answer with letters...")


print("I would like to know more about you. I promise im not gonna steal you information!")

while True:

    lastName = input("Please write your last name: ")

    if lastName.isalpha():
        print(f"Thank you for the answer {firstName} {lastName}.") 
        break
    else:
        print("Please answer with letters...")

while True:
    
    age = input("Please write your age in numbers: ")

    if age.isdigit(): #Checks if age is written with numbers
        age = int(age) #Changes age to integer
        
        if age < 67:
            print(f"Wow {age}! Soon you will retire.")
        elif age > 67 and age < 200:
            print(f"Wow {age}, so young!")
        elif age > 200:
            print(f"{age} interesting, how was it? the dinosaurs I mean.")
        break
    else:
        print("Please write your age using only numbers...")
        
print(f"Thank for participating in this program {firstName} {lastName} the {age} year old!")
