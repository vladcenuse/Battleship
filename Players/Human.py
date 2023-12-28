from Board.Board import Board
from Ship.Ship import Ship

class Human:
    def __init__(self):
        self.board = Board("human")
        self.ships = []

    def input_and_add_ship(self, size):
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


    def player_lost(self):
        for ship in self.ships:
            if ship.isSunk == False:
                return False
        return True

    def input_and_shoot(self):
        try:
            row = int(input("Row: "))
            column = int(input("Column: "))
            self.board.check_if_position_is_valid(row, column)
            if self.board.get_matrix_square_value(row, column) == 2:
                print("Hit!")
                self.board.set_matrix_square(row, column, 3)
                for ship in self.ships:
                    ship.hit_ship(row, column)
                    ship.check_if_sunk()
                    if ship.isSunk == True:
                        print("You sunk a ship!")
                        self.ships.remove(ship)
                        if self.player_lost() == True:
                            print("You won!")
            else :
                self.board.set_matrix_square(row, column, 1)
                print("Miss!")
        except ValueError as ve:
            print(ve)

# player = Human()
# ship_size = [5,4,3,3,2]
# for size in ship_size:
#     player.input_and_add_ship(size)
#     print(player.board)

#TODO add disclaimer to not place ships near each other