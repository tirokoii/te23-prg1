

print("Hello and welcome to my program")

while True:

    firstName = input("Please write your name: ")

    if firstName.isalpha():
        print(f"Good day {firstName}. Thank you for gracing me with your presence.") 
        break
    else:
        print("Please answer with letters...")


while True:

    lastName = input("Please write your last name: ")

    if lastName.isalpha():
        print(f"Thank you for the answer {firstName} {lastName}.") 
        break
    else:
        print("Please answer with letters...")
        
while True:
    age = input("Please write your age in numbers: ")

    if age.isdigit():
        age = int(age)
        if age < 67:
            print(f"Wow {age}! Soon you will retire.")
        elif age > 67 and age < 200:
            print(f"Wow {age}, so young!")
        elif age > 200:
            print(f"{age} interesting, how was it? the dinosaurs I mean.")
        break
    else:
        print("Please write your age using only numbers...")
        
print(f"Thank for participating in this program {firstName} {lastName} the {age} year old.")
