apple = 7
pear = 13
soldOne = 1
soldTwo = 1


def sum():
    A = apple*1
    P = pear*1

    if A<P:
        print("Petra earned more")
    elif A>P:
        print("Axel earned more")
    else:
        print("They earned exactly the same")

def checkValue():

    soldA = soldOne
    soldP = soldTwo
    valueA = 0
    valueP = 0

    while True:
        try :
            valueA = int(input("Sold apples: "))
            valueP = int(input("Sold pears: "))
        except ValueError :
            print("Error")

        if valueA == soldA and valueP == soldP:
            sum()
            return valueA and valueP
        else:
            print("You didn't follow the instructions properly...")

print("\nAxel is selling apples and Petra pears at a nearby market. Who will earn more?\n")

print("Axel and Petra both sell 1 fruit each")
checkValue()
print("")

soldOne = 13
soldTwo = 7

print("Axel sell 13 apples and Petra 7 pears")
checkValue()
print("")

soldOne = 15
soldTwo = 8

print("Axel sells 15 apples and Petra 8 pears")
checkValue()
print("")

print("Results are:")
print("Axel and Petra both sell 1 fruit each :")
A = apple*1
P = pear*1
sum()
print("Axel sell 13 apples and Petra 7 pears :")
A = apple*13
P = pear*7
sum()
print("Axel sells 15 apples and Petra 8 pears :")
A = apple*15
P = pear*8
sum()



