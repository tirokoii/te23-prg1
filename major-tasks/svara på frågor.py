
def svara():
    while True:
        try:
            svar = int(input("vill du fråga om provet eller egna projektet\n 1: provet \n 2:projekt \n 3:avsluta\n"))
            return svar
        except ValueError :
            print("Nähh, det går int\n")
    
gå = "s"

while gå == "s":
    svar = svara()

    if svar == 1:
        print("\nGjort: Santa Grinch\nHur gick det: Bra och dåligt")
        print("Vad gick mindre bra: Att jobba med for loopar, definition, klasser och lootsystemet")
        print("Fortsätta med: Att välja, byta ut och spara presenter samt logiken bakom spelets mekanik och mål")
        print("Ändra på: Kanske byta ut loot systemet\n")
    elif svar == 2:
        print("\nGjort: Prov\nHur gick det: Si sådär")
        print("Vad gick mindre bra: for loopen, vad de två operatorerna % och != gör men även syntax")
        print("Fortsätta med: Göra lite research på de operatorerna jag hade problem med, samt titta mer på for loopar och syntax")
        print("Ändra på: Sättet jag lär in mig på, jobba mer med the fundementals och titta på andras koder\n")
    elif svar == 3:
        gå = "q"
    else: 
        print("Hallå, nej")
    