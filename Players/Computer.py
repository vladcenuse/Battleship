import random
from Board.Board import Board
from Ship.Ship import Ship
from Players.Human import Human

class Computer:
    def __init__(self):
        self.board = Board("computer")
        self.ships = []
        self.shooting_pattern = []

    def player_lost(self):
        for ship in self.ships:
            if ship.isSunk == False:
                return False
        return True

    def place_5_ships(self):
        # 1 ship of size 5 , 1 ship of size 4, 2 ships of size 3 and 1 ship of size 2
        ship_size = [5, 4, 3, 3, 2]
        for size in ship_size:
            placed = False
            while placed == False:
                row = random.randint(0, 9)
                column = random.randint(0, 9)
                orientation = random.choice(["h", "v"])
                ship = Ship(size, orientation)
                if orientation == "h":
                    ship.horizontal_ship(row, column)
                    try:
                        self.board.check_if_ship_fits(ship)
                        self.ships.append(ship)
                        self.board.add_ship(ship)
                        placed = True
                    except ValueError as ve:
                        pass
                elif orientation == "v":
                    ship.vertical_ship(row, column)
                    try:
                        self.board.check_if_ship_fits(ship)
                        self.ships.append(ship)
                        self.board.add_ship(ship)
                        placed = True
                    except ValueError as ve:
                        pass

    def fill_shooting_pattern(self): # We use this for the bonus
        for i in range(10):
            for j in range(10):
                if (i + j) % 2 == 0:
                    self.shooting_pattern.append((i, j))


    def computer_shoot(self, human : Human):
        # In case the computer hits a ship, it will shoot around that square, and if it hits again, it will shoot in that direction until it sunks the ship, otherwise it will shoot in the other remaining directions
        #Start shooting from the pattern
        # Write the code for this








for i in range(1):
    PC = Computer()
    PC.place_5_ships()
    print(PC.board)
    print("\n")
