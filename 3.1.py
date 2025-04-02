from math import pi

radie = float(input("Vad är cirkelns radie? "))


if  radie <= 0:
    print("Det går inte att räkna med negativa eller noll radianer.")
else:
    omkrets = radie*2*pi
    area = pi*radie*radie

    print(f"Omkrets: {omkrets: .3f}")
    print(f"Arean:   {area: .3f}")
