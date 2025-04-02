from math import pi

def ärfloat(floaty):
    while True :
        try :
            radie = float(input(floaty))
            return radie
        except ValueError :
            print("En bokstav är ingen siffra")

radie = ärfloat("Vad är cirkelns radie? ")


if  radie <= 0:
    print("Det går inte att räkna med negativa eller noll radianer.")
else:
    omkrets = radie*2*pi
    area = pi*radie*radie

    print(f"Omkrets: {omkrets: .3f}")
    print(f"Arean:   {area: .3f}")
