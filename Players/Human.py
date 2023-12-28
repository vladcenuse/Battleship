from Board.Board import Board
from Ship.Ship import Ship

class Human:
    def __init__(self):
        self.board = Board("human")
        self.ships = []

    def input_and_add_ship(self, size):
        placed = False
        while placed == False:
            placed = True
            try:
                row = int(input("Row: "))
                column = int(input("Column: "))
                orientation = input("Orientation(h/v):  ")
                ship = Ship(size, orientation)
                if orientation == "h":
                    ship.horizontal_ship(row, column)
                    self.board.check_if_ship_fits(ship)
                elif orientation == "v":
                    ship.vertical_ship(row, column)
                    self.board.check_if_ship_fits(ship)
                self.ships.append(ship)
                self.board.add_ship(ship)
            except ValueError as ve:
                print(ve)
                placed = False


    def player_lost(self):
        for ship in self.ships:
            if ship.isSunk == False:
                return False
        return True


# player = Human()
# ship_size = [5,4,3,3,2]
# for size in ship_size:
#     player.input_and_add_ship(size)
#     print(player.board)

#TODO add disclaimer to not place ships near each other