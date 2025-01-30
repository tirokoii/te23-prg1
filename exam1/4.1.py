största = 0
minsta = 10e100000

while True:
    tal = float(input("Skriv in ett tal: "))
    if tal < 0:
        print(f"Största: {största}\nMinsta: {minsta}\n")
    elif tal > största:
        största = tal

    elif tal < minsta:
        minsta = tal

#Tog hjälp av internet, för att förstå - inte för att vissa kunskaper