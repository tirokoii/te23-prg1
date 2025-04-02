# Jämför list med tuple på annat sätt än ==, om listan och tuplen är lika lång eller har samma inehåll ska de var lika med
# Ta ut längd på listorna och jämför - len - plocka ut längden på dem separat och jämför
# Ta ut inehållen individuellt - jämför inehållen i dem (det går)

while True:
    tuple_input = sorted(tuple(input("tuple: ")))
    list_input = sorted(list(input("list: ")))

    while True:
        tuple_input = list(tuple_input)
        if len(tuple_input) == len(list_input):
            if tuple_input == list_input:
                print("Listan och tuplen är lika lång och har samma inehåll")
                break
            else:
                print("Tuplen och listan är lika långa")
                break
        else:
            if tuple_input == list_input:
                print("Listan och tuplen har samma inehåll")
                break

        print("Tuplen och listan är inte lika lång och har inte samma värden")
        break


