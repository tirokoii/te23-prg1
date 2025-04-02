# Calculate (Standardavikelse) for a couple of values
# The numbers should be in a list
# The formula: o = squrt((1/n)*sum(n)*(x - medel)(x - medel))

from math import sqrt

x = []

while len(x) < 10:
    x.append(int(input('skriv in ett värde: ')))

total = 0
for i in x:
    total += i
mid = total/len(x)

o = sqrt((1/n)*sum(len(n))*(x -mid)(x - mid))