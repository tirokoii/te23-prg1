# Stastioner med angivna temperaturer
# Print ut medel temperatur
# Print stationerna med högsta temperaturer och sedan medel temperatur

temp = [10, 40, 19, 28, -27, -31, 24, 18, -28]
amount = 0
station = 0

for i in temp:
    amount += i

mid = amount/len(temp)
print(f"Average value: {mid:.1f}")

for i in temp:
    station += 1
    if i > mid:
        print(f"station {station}: {i}")

