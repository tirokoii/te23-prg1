import sys #Sys module
for line in sys.stdin: #For line in system turn into input
    if "q" == line.rstrip(): #If q is written then
        break
    print(f"Input : {line}")

print("Exit")

#Must redirect, doesn't function correctly otherwise