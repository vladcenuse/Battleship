from Board.Board import Board
from Ship.Ship import Ship
from ui.ui import User_Inputs_Outputs

ui = User_Inputs_Outputs

class Human:
    def __init__(self):
        self.board = Board("human")
        self.ships = []

    def input_and_add_ship(self, size):
        placed = False
        while placed == False:
            placed = True
            try:
                row,column,orientation = User_Inputs_Outputs.place_ship()
                ship = Ship(size, orientation)
                if orientation == "h":
                    ship.horizontal_ship(row, column)
                    self.board.check_if_ship_fits(ship)
                elif orientation == "v":
                    ship.vertical_ship(row, column)
                    self.board.check_if_ship_fits(ship)
                else:
                    raise ValueError("Invalid orientation!")
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
