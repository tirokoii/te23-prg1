board_size = []

for i in range(0, 10):
    row = []
    for i in range(0, 10):
        row.append(0)
    board_size.append(row)

player_one_board = board_size
player_one_record = board_size
player_two_board = board_size
player_two_record = board_size

ships = {
    "1" : [2, "hunter"],
    "2" : [3, "submarine"],
    "3" : [3, "cruiser"],
    "4" : [4, "battleship"],
    "5" : [5, "carrier"]
}

def check_coordinate(x, y):
    print(x)
    print(y)
    print("nice")

def playerTurn(player):
    if player == ("one"):
        active_board = player_one_board
        active_record_board = player_one_record
    else:
        active_board = player_two_board
        active_record_board = player_two_record
    current_ship = 0
    while current_ship <= 5:
        current_ship += 1
        print(f"Where do you want to place your {ships[str(current_ship)][1]}")
        print("The coordinates should be x, y")
        coordinate = input()
        check_coordinate(coordinate[1], coordinate[3])

while True:
    print("Player one starts to choose their board layout.")
    playerTurn("one")
