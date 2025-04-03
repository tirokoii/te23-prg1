# Calculate (Standardavikelse) for a couple of values
# The numbers should be in a list
# The formula: o = squrt((1/n)*sum(n)*(x - medel)(x - medel))
# x = numbers

from math import sqrt

x = []

while len(x) < 10:
    x.append(int(input('skriv in ett värde: ')))

f = 0
total = 0
while True:
    for i in x:
        total += i
        f += (1/i)*sum(i)
    mid = total/len(x)  
    o = sqrt(f*(x -mid)(x - mid))