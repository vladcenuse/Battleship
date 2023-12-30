from unittest import TestCase
from Board.Board import Board
from Ship.Ship import Ship
from Players.Computer import Computer
from Players.Human import Human

class TestBoard(TestCase):
    def test_get_matrix_square_value(self):
        board = Board("human")
        board.board[0] = 1
        self.assertEqual(board.get_matrix_square_value(0,0),1)

    def test_get_position_in_matrix(self):
        board = Board("human")
        self.assertEqual(board.get_position_in_matrix(0,0),0)

    def test_set_matrix_square(self):
        board = Board("human")
        board.set_matrix_square(0,0,1)
        self.assertEqual(board.board[0],1)

    def test_check_if_position_is_valid(self):
        board = Board("human")
        self.assertEqual(board.check_if_position_is_valid(0,0),True)

    def test_turn_matrix_into_symbols(self):
        board = Board("human")
        board.board[0] = 1
        self.assertEqual(board.turn_matrix_into_symbols("human"),["O"] + ["~"] * 99)


class TestShip(TestCase):
    def test_horizontal_ship(self):
        ship = Ship(5,"h")
        ship.horizontal_ship(0,0)
        self.assertEqual(ship.coordinates,[[0,0],[0,1],[0,2],[0,3],[0,4]])

    def test_vertical_ship(self):
        ship = Ship(5,"v")
        ship.vertical_ship(0,0)
        self.assertEqual(ship.coordinates,[[0,0],[1,0],[2,0],[3,0],[4,0]])

    def test_check_if_sunk(self):
        ship = Ship(5,"h")
        ship.horizontal_ship(0,0)
        ship.hit_ship(0,0)
        ship.hit_ship(0,1)
        ship.hit_ship(0,2)
        ship.hit_ship(0,3)
        ship.hit_ship(0,4)
        ship.check_if_sunk()
        self.assertEqual(ship.isSunk,True)

    def test_hit_ship(self):
        ship = Ship(5,"h")
        ship.horizontal_ship(0,0)
        ship.hit_ship(0,0)
        self.assertEqual(ship.coordinates,[[0,1],[0,2],[0,3],[0,4]])

class TestComputer(TestCase):
    def test_computer_lost(self):
        computer = Computer()
        computer.ships = [Ship(5,"h")]
        computer.ships[0].hit_ship(0,0)
        computer.ships[0].hit_ship(0,1)
        computer.ships[0].hit_ship(0,2)
        computer.ships[0].hit_ship(0,3)
        computer.ships[0].hit_ship(0,4)
        self.assertEqual(computer.computer_lost(),False)

    def test_place_5_ships(self):
        computer = Computer()
        computer.place_5_ships()
        self.assertEqual(len(computer.ships),5)

    def test_fill_shooting_pattern(self):
        computer = Computer()
        computer.fill_shooting_pattern()
        self.assertEqual(len(computer.shooting_pattern),50)

class TestHuman(TestCase):
    def test_input_and_add_ship(self):
        human = Human()
        human.input_and_add_ship(5)
        self.assertEqual(len(human.ships),1)

    def test_player_lost(self):
        human = Human()
        human.ships = [Ship(5,"h")]
        human.ships[0].hit_ship(0,0)
        human.ships[0].hit_ship(0,1)
        human.ships[0].hit_ship(0,2)
        human.ships[0].hit_ship(0,3)
        human.ships[0].hit_ship(0,4)
        self.assertEqual(human.player_lost(),False)


