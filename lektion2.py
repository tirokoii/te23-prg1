

print("Hello and welcome to my program")

firstName = input("Please write your name: ")

print(f"Good day {firstName}. Thank you for gracing me with your presence.") 


print("I would like to know more about you.")

lastName = input("Please write your last name: ")

print(f"Thanks for the answer {firstName} {lastName}.")


age = input("Please write you age, in numbers: ")

ageConverted = int(age)
if int(ageConverted) <67:
    print(f"Wow {age}! Soon you will retire.")
else:
    print(f"{age}, so young!")

print(f"Thank for the answers {firstName} {lastName} the {age} year old.")



