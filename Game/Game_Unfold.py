from Players.Computer import Computer
from Players.Human import Human
import random


class Game:
    def __init__(self):
        self.human = Human()
        self.computer = Computer()
        self.computer_won = False
        self.player_won = False

    def place_ships(self):
        # ship_size = [5, 4, 3, 3, 2] #TODO uncomment this
        ship_size = [5]
        for size in ship_size:
            self.human.input_and_add_ship(size)
        self.computer.place_5_ships()
    def input_and_shoot(self):
        valid_shot = False
        while valid_shot == False:
            valid_shot = True
            try:
                row = int(input("Row: "))
                column = int(input("Column: "))
                self.computer.board.check_if_position_is_valid(row, column)
                if self.computer.board.get_matrix_square_value(row, column) == 2:
                    print("Hit!")
                    self.computer.board.set_matrix_square(row, column, 3)
                    for ship in self.computer.ships:
                        ship.hit_ship(row, column)
                        ship.check_if_sunk()
                        if ship.isSunk == True:
                            print("You sunk a ship!")
                            self.computer.ships.remove(ship)
                            if self.computer.computer_lost() == True:
                                self.player_won = True
                else :
                    self.computer.board.set_matrix_square(row, column, 1)
                    print("Miss!")
            except ValueError as ve:
                print(ve)
                valid_shot = False

    def computer_shot(self):
        self.computer.fill_shooting_pattern()
        (row,column) = random.choice(self.computer.shooting_pattern)
        for i in self.computer.shooting_pattern:
            if
        print("Computer shoots: " + str(row) + " " + str(column))




    def determine_a_winner(self):
        if self.player_won == True:
            print("The human has won! Congratulations")
            exit(0)
        if self.computer_won == True:
            print("The human has lost! Take the L")
            exit(0)


def game_unfolding():
    game = Game()
    game.place_ships()
    # while True:
    #     print(game.computer.board)
    #     game.input_and_shoot()
    #     game.determine_a_winner()
    for i in range(50):
        game.computer_shot()
    print(game.computer.shooting_pattern)


