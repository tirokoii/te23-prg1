def ärfloat(floaty):
    while True :
        try :
            nummer = float(input(floaty))
            return nummer
        except ValueError :
            print("En bokstav är ingen siffra")

mätIdag = ärfloat("Mätarställning i dag? ")
mätFör = ärfloat("Mätarställning för ett år sedan? ")
mil = print(f"Antal körda mil:     {(mätIdag-mätFör): .0f}")
liter = print(f"Antal liter bensin:  {((mätFör/mätIdag)*(mätIdag-mätFör)): .1f}")
förbrukning = print(f"Förbrukning per mil: {(mätFör/mätIdag): .2f}")