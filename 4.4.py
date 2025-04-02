rader = int(input("Hur många rader? "))

for i in range(1, rader + 1): # Rader
    for j in range(1, rader + 1): # Nummer på raderna
        print(f"{i*j:3d}", end=" ")
    print("")

#Tog hjälp av internet, för att förstå - inte för att visa kunskaper