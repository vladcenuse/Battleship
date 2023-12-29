from texttable import Texttable
from Ship.Ship import Ship


class Board:
    def __init__(self,player_type):
        self.board = [0] * 100  # 10x10 grid
        self.player_type = player_type


    """
    0 = initial state (unknown)
    1 = empty
    2 = ship 
    3 = hit
    """

    def get_matrix_square_value(self, row, column):
        return self.board[row * 10 + column]
    def get_position_in_matrix(self, row, column):
        return row * 10 + column
    def set_matrix_square(self, row, column, value):
        self.board[row * 10 + column] = value
    def check_if_position_is_valid(self, row, column):
        # This is to check if the input position to shoot is valid
        if row < 0 or row > 9 or column < 0 or column > 9:
            raise ValueError("Invalid position! The bounds are not respected ")
        elif self.get_matrix_square_value(row, column) == 1 or self.get_matrix_square_value(row, column) == 3 :
            raise ValueError("Invalid position! You already shot here!")
        else:
            return True

    def turn_matrix_into_symbols(self, player_type):
        """
        0 --> ~
        1 --> O
        2 --> X
        3 --> H
        :return:
        """
        temp_board = []
        if player_type == "human":
            for i in self.board:
                if i == 0:
                    temp_board.append("~")
                elif i == 1:
                    temp_board.append("O")
                elif i == 2:
                    temp_board.append("X")
                elif i == 3:
                    temp_board.append("H")
        elif player_type == "computer":
            for i in self.board:
                if i == 0:
                    temp_board.append("~")
                elif i == 1:
                    temp_board.append("O")
                elif i == 2:
                    temp_board.append("X")
                elif i == 3:
                    temp_board.append("H")
        return temp_board

    def __str__(self):
        board_to_print = self.turn_matrix_into_symbols(player_type=self.player_type)

        table = Texttable()
        table.set_cols_align(["c"] * 10)
        table.set_cols_valign(["m"] * 10)
        table.set_cols_dtype(["t"] * 10)
        for i in range(10):
            table.add_row(board_to_print[i * 10: i * 10 + 10])

        return table.draw()

    def add_ship(self, ship: Ship):
        if ship.orientation == "h":
            for i in ship.coordinates:
                self.set_matrix_square(i[0], i[1], 2)
        elif ship.orientation == "v":
            for i in ship.coordinates:
                self.set_matrix_square(i[0], i[1], 2)

    def check_if_ship_fits(self, ship: Ship):

        for i in ship.coordinates:
            position = self.get_position_in_matrix(i[0], i[1])
            if position > 99:
                raise ValueError("Invalid position! The ship is out of bounds!")

        if ship.orientation == "h":
            for i in ship.coordinates:
                if self.get_matrix_square_value(i[0], i[1]) == 2:
                    raise ValueError("Invalid position! Ships are overlapping!")
                elif i[1] > 9:
                    raise ValueError("Invalid position! The ship is out of bounds!")
        elif ship.orientation == "v":
            for i in ship.coordinates:
                if self.get_matrix_square_value(i[0], i[1]) == 2:
                    raise ValueError("Invalid position! Ships are overlapping!")
                elif i[0] > 9:
                    raise ValueError("Invalid position! The ship is out of bounds!")

