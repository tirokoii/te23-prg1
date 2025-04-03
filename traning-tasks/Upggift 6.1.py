#Program who never prints the same number even though the user has put in the same input

def intTry(question):
    while True:
        try:
            intput = int(input(question))
            return intput
        except ValueError:
            print('Det är ingen siffra')


number_list = []
round_count = 0

while True:
    round_count += 1
    number = intTry("Skriv in ett nummer: ")

    if number not in number_list:
        number_list.append(number)

    if round_count == 10:
        break

for num in number_list:
    print(num, end=" ")



