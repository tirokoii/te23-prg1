mätIdag = float(input("Mätarställning i dag? "))
mätFör = float(input("Mätarställning för ett år sedan? "))
mil = print(f"Antal körda mil:     {(mätIdag-mätFör): .0f}")
liter = print(f"Antal liter bensin:  {((mätFör/mätIdag)*(mätIdag-mätFör)): .1f}")
förbrukning = print(f"Förbrukning per mil: {(mätFör/mätIdag): .2f}")