# Beräkna Standardavikelse för ett antal värden
# Nummren ska vara i en lista
# Ekvationen: o = (sum(x - mid)^2)/n
# x = nummer

from math import sqrt

number_list = []

while len(number_list) < 5:
    number_list.append(int(input("Skriv in ditt tal: ")))
number_list.sort

x = 0

for n in number_list:
    x += n
mid = x/len(number_list)

sum_list = []
for n in number_list:
    sum_list.append(((n-mid)*(n-mid))/len(number_list))

print(f"{sqrt(sum(sum_list)):.2f}")
    
