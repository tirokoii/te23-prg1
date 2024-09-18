#Create an if program with gym prices, and outputs what is the most price worthy

#Write the different prices as variables
#Ask for how many times you are going to visit
#Compare the two prices and print out correct answer depending on what is more price worthy



print ("Hello, this program will compare the pricing between an yearly card or one time ticket.")

yearlyCard = input("What does an yearlyCard at you gym cost?: ")
oneTimeTicket = input("What does an one time ticket cost at your gym?: ")
yearlyCard = int(yearlyCard)
oneTimeTicket = int(oneTimeTicket)
gymVisits = input ("Please write in how many times are you planning on visiting your gym this year?: ")
gymVisits = int(gymVisits)

oneTimeTicket = gymVisits * oneTimeTicket

if yearlyCard < oneTimeTicket:
    print(f"It is {oneTimeTicket-yearlyCard} kr cheaper buying an yearly card than one time tickets")
    print(f"One time tickets costs: {oneTimeTicket} kr")
    print(f"An yearly card costs: {yearlyCard} kr")
elif yearlyCard > oneTimeTicket:
    print(f"It is {yearlyCard-oneTimeTicket} kr cheaper buying one time tickets than an yearly card")
    print(f"One time tickets costs: {oneTimeTicket} kr")
    print(f"An yearly card costs: {yearlyCard} kr")
else:
    print("There is no price difference between the both")
    print(f"Both cost: {yearlyCard}")