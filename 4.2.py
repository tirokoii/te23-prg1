#Ett program som skriver ut en tabell för talen 1 till 12
#På varje rad ska det finnas talet i kvadrat och talet i kubik
n = 1

for i in range(1, 13):
    print(f"{n:8d}{n*n:8d}{n*n*n:8d}")
    n += 1


















"""from random import randint

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
        print(tal, end=", ")"""     