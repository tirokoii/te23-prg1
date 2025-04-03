# Calculate (Standardavikelse) for a couple of values
# The numbers should be in a list
# The formula: o = (sum(x - mid)^2)/n
# x = numbers

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
    
