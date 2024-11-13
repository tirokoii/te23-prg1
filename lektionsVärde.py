def ärint():
    while True :
        try :
            valtVärde = int(input("Välj en siffra: "))
            return valtVärde
        except ValueError :
            print("Felaktigt tal")

gömtVärde = 18
inputVärde = ärint()

if int(inputVärde) > gömtVärde :
    print("Det du skrev är större än det gömnda värdet", inputVärde)
elif int(inputVärde) < gömtVärde:
    print("Det var mindre än det gömda värdet: " + str(gömtVärde))
else :
    print("Ditt värde är samma som det gömnda värdet")
