#Första dagen 1 öre 
#Fördubblas varje dag

lön = 0.00358777
dagar = 1

while lön < 1000000:
    lön *= 2
    dagar += 1

print(f"Det har gått {dagar:1d} dagar innan man tjänat 10 miljoner")