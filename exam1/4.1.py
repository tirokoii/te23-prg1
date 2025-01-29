#Ett program som läser in ett godtyckligt antal positiva tal
#När användaren skriver ett negativt tal ska programmet skriva ut det största och minsta av de positiva talen
from random import randint

while True:
    tal = int(input("Vad är ditt tal? "))
    if tal < 0:
        print("Error")
    else:
        break


n = int(input("Skriv ett negativt tal för att ta ut största och minsta talet i din talordning "))
print("")
x = 0
plusTal = randint(1, 20)

if n < 0:
    for i in range(1, 9):
        tal += plusTal
        x += 1
        if x == 1:
            print(f"Minsta: {tal}", end=", ")
        elif x == 8:
            print("största:", tal) 
else:
    for i in range(1, 9):
        tal += plusTal
        print(tal, end=", ")
            