from Players.Computer import Computer
from Players.Human import Human
import random


class Game:
    def __init__(self):
        self.human = Human()
        self.computer = Computer()
        self.computer_won = False
        self.player_won = False
        self.computer_last_hit_coordinates = None
        self.computer_hit_a_ship = False
        self.ship_direction = None

    def place_ships(self):
        #ship_size = [5, 4, 3, 3, 2] #TODO uncomment this
        ship_size = [5]
        for size in ship_size:
            print("Enter the coordinates for the ship of size " + str(size))
            self.human.input_and_add_ship(size)
            print("Your board looks like this so far: ")
            print(self.human.board)
        self.computer.place_5_ships()

    def input_and_shoot(self):
        valid_shot = False
        while valid_shot == False:
            valid_shot = True
            print("Enter the coordinates for the shot: ")
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
                else:
                    self.computer.board.set_matrix_square(row, column, 1)
                    print("Miss!")
            except ValueError as ve:
                print(ve)
                valid_shot = False

    def check_for_ship_direction(self, row, column):
        # TODO we need to check that the neighbour squares are either 0 or 3 (unknown or hit)
        # TODO we need to check that squares are not outside the matrix

        if (row-1) >= 0 and (row-1) <= 9 and (column) >= 0 and (column) <= 9:
            if self.human.board.get_matrix_square_value(row - 1, column) == 3:
                 self.ship_direction = "v"
                 return
        if (row+1) >= 0 and (row+1) <= 9 and (column) >= 0 and (column) <= 9:
            if self.human.board.get_matrix_square_value(row + 1, column) == 3:
                 self.ship_direction = "v"
                 return
        if (row) >= 0 and (row) <= 9 and (column-1) >= 0 and (column-1) <= 9:
            if self.human.board.get_matrix_square_value(row, column - 1) == 3:
                 self.ship_direction = "h"
                 return
        if (row) >= 0 and (row) <= 9 and (column+1) >= 0 and (column+1) <= 9:
            if self.human.board.get_matrix_square_value(row, column + 1) == 3:
                 self.ship_direction = "h"
                 return
        else:
            self.ship_direction = None

    def computer_shot(self):
        if self.computer_hit_a_ship == False:
            (row, column) = random.choice(self.computer.shooting_pattern)
            temp_list = []
            for i in self.computer.shooting_pattern:
                if i != (row, column):
                    temp_list.append(i)
            self.computer.shooting_pattern = temp_list
            print("Computer shoots: " + str(row) + " " + str(column))
            if self.human.board.get_matrix_square_value(row, column) == 2:
                print("Hit!")
                self.human.board.set_matrix_square(row, column, 3)
                for ship in self.human.ships:
                    ship.hit_ship(row, column)
                    ship.check_if_sunk()
                    if ship.isSunk == True:
                        print("The computer sunk a ship!")
                        self.human.ships.remove(ship)
                        if self.human.player_lost() == True:
                            self.computer_won = True
                    else:
                        self.computer_hit_a_ship = True
                        self.computer_last_hit_coordinates = (row, column)
            else:
                self.human.board.set_matrix_square(row, column, 1)
                print("Miss!")
        else:
            # TODO we treat 2 cases, one if we know the direction of the ship and one if we don't
            self.check_for_ship_direction(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1])
            if self.ship_direction == None:  # This means that we only hit the ship once and we don't know the direction
                # we need to pick a random neighbour square
                initial_row = self.computer_last_hit_coordinates[0]
                initial_column = self.computer_last_hit_coordinates[1]

                valid_coordinates =[]
                if self.computer_last_hit_coordinates[0] - 1 >= 0 and self.computer_last_hit_coordinates[0] - 1 <= 9 and self.computer_last_hit_coordinates[1] >= 0 and self.computer_last_hit_coordinates[1] <= 9:
                    if self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0] - 1, self.computer_last_hit_coordinates[1]) == 0 or self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0] - 1, self.computer_last_hit_coordinates[1]) == 2:
                        valid_coordinates.append((self.computer_last_hit_coordinates[0] - 1, self.computer_last_hit_coordinates[1]))
                if self.computer_last_hit_coordinates[0] + 1 >= 0 and self.computer_last_hit_coordinates[0] + 1 <= 9 and self.computer_last_hit_coordinates[1] >= 0 and self.computer_last_hit_coordinates[1] <= 9:
                    if self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0] + 1, self.computer_last_hit_coordinates[1]) == 0 or self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0] + 1, self.computer_last_hit_coordinates[1]) == 2:
                        valid_coordinates.append((self.computer_last_hit_coordinates[0] + 1, self.computer_last_hit_coordinates[1]))
                if self.computer_last_hit_coordinates[0] >= 0 and self.computer_last_hit_coordinates[0] <= 9 and self.computer_last_hit_coordinates[1] - 1 >= 0 and self.computer_last_hit_coordinates[1] - 1 <= 9:
                    if self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] - 1) == 0 or self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] - 1) == 2:
                        valid_coordinates.append((self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] - 1))
                if self.computer_last_hit_coordinates[0] >= 0 and self.computer_last_hit_coordinates[0] <= 9 and self.computer_last_hit_coordinates[1] + 1 >= 0 and self.computer_last_hit_coordinates[1] + 1 <= 9:
                    if self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] + 1) == 0 or self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] + 1) == 2:
                        valid_coordinates.append((self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] + 1))
                (row, column) = random.choice(valid_coordinates)

                temp_list = []
                for i in self.computer.shooting_pattern:
                    if i != (row, column):
                        temp_list.append(i)
                self.computer.shooting_pattern = temp_list
                print("Computer shoots: " + str(row) + " " + str(column))
                if self.human.board.get_matrix_square_value(row, column) == 2:
                    print("Hit!")
                    self.ship_direction = self.check_for_ship_direction(row, column)
                    self.human.board.set_matrix_square(row, column, 3)
                    self.computer_last_hit_coordinates = (row, column)
                    for ship in self.human.ships:
                        ship.hit_ship(row, column)
                        ship.check_if_sunk()
                        if ship.isSunk == True:
                            print("The computer sunk a ship!")
                            self.human.ships.remove(ship)
                            self.computer_hit_a_ship = False
                            self.computer_last_hit_coordinates = None
                            if self.human.player_lost() == True:
                                self.computer_won = True

                else:
                    self.human.board.set_matrix_square(row, column, 1)
                    print("Miss!")
                    self.computer_last_hit_coordinates = (initial_row, initial_column)
                    #TODO after checking coords ..
            else:  # This means that we know the direction of the ship
                if self.ship_direction == "v":
                    valid_coords = []
                    if self.computer_last_hit_coordinates[0] - 1 >= 0 and self.computer_last_hit_coordinates[0] - 1 <= 9 and self.computer_last_hit_coordinates[1] >= 0 and self.computer_last_hit_coordinates[1] <= 9:
                        if self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0] - 1, self.computer_last_hit_coordinates[1]) == 0 or self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0] - 1, self.computer_last_hit_coordinates[1]) == 2:
                            valid_coords.append((self.computer_last_hit_coordinates[0] - 1, self.computer_last_hit_coordinates[1]))
                    if self.computer_last_hit_coordinates[0] + 1 >= 0 and self.computer_last_hit_coordinates[0] + 1 <= 9 and self.computer_last_hit_coordinates[1] >= 0 and self.computer_last_hit_coordinates[1] <= 9:
                        if self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0] + 1, self.computer_last_hit_coordinates[1]) == 0 or self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0] + 1, self.computer_last_hit_coordinates[1]) == 2:
                            valid_coords.append((self.computer_last_hit_coordinates[0] + 1, self.computer_last_hit_coordinates[1]))

                    (row, column) = random.choice(valid_coords)

                    temp_list = []
                    for i in self.computer.shooting_pattern:
                        if i != (row, column):
                            temp_list.append(i)
                    self.computer.shooting_pattern = temp_list
                    print("Computer shoots: " + str(row) + " " + str(column))
                    if self.human.board.get_matrix_square_value(row, column) == 2:
                        print("Hit!")
                        self.human.board.set_matrix_square(row, column, 3)
                        self.computer_last_hit_coordinates = (row, column)
                        for ship in self.human.ships:
                            ship.hit_ship(row, column)
                            ship.check_if_sunk()
                            if ship.isSunk == True:
                                print("The computer sunk a ship!")
                                self.human.ships.remove(ship)
                                self.computer_hit_a_ship = False
                                self.computer_last_hit_coordinates = None
                                self.ship_direction = None
                                if self.human.player_lost() == True:
                                    self.computer_won = True
                    else:
                        self.human.board.set_matrix_square(row, column, 1)
                        print("Miss!")
                        self.computer_last_hit_coordinates = (row, column)
                elif self.ship_direction == "h":
                    valid_coords = []
                    if self.computer_last_hit_coordinates[0] >= 0 and self.computer_last_hit_coordinates[0] <= 9 and self.computer_last_hit_coordinates[1] - 1 >= 0 and self.computer_last_hit_coordinates[1] - 1 <= 9:
                        if self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] - 1) == 0 or self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] - 1) == 2:
                            valid_coords.append((self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] - 1))
                    if self.computer_last_hit_coordinates[0] >= 0 and self.computer_last_hit_coordinates[0] <= 9 and self.computer_last_hit_coordinates[1] + 1 >= 0 and self.computer_last_hit_coordinates[1] + 1 <= 9:
                        if self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] + 1) == 0 or self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] + 1) == 2:
                            valid_coords.append((self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] + 1))
                    (row, column) = random.choice(valid_coords)
                    temp_list = []
                    for i in self.computer.shooting_pattern:
                        if i != (row, column):
                            temp_list.append(i)
                    self.computer.shooting_pattern = temp_list
                    print("Computer shoots: " + str(row) + " " + str(column))
                    if self.human.board.get_matrix_square_value(row, column) == 2:
                        print("Hit!")
                        self.human.board.set_matrix_square(row, column, 3)
                        self.computer_last_hit_coordinates = (row, column)
                        for ship in self.human.ships:
                            ship.hit_ship(row, column)
                            ship.check_if_sunk()
                            if ship.isSunk == True:
                                print("The computer sunk a ship!")
                                self.human.ships.remove(ship)
                                self.computer_hit_a_ship = False
                                self.computer_last_hit_coordinates = None
                                self.ship_direction = None
                                if self.human.player_lost() == True:
                                    self.computer_won = True

    def determine_a_winner(self):
        if self.player_won == True:
            print("The human has won! Congratulations")
            exit(0)
        if self.computer_won == True:
            print("The human has lost! Take the L")
            exit(0)

    @staticmethod
    def print_menu():
        print("\n\033[1mWelcome to Battleship!\033[0m")
        print("-------------------------------------------------------")
        print("\033[1mRules:\033[0m")
        print("\u2022 You have 5 ships to place on the board.")
        print("\u2022 Ships can be placed horizontally or vertically.")
        print("\u2022 Ships must not overlap.")
        print("\u2022 The human and the computer take turns shooting at each other.")
        print("\u2022 The first one to sink all the ships wins.")
        print(
            "\n\033[1mDisclaimer:\033[0m For a better experience, please maximize the terminal window and avoid placing ships near each other.")
        print("\n\033[1mGood luck!\033[0m")
        print("-------------------------------------------------------\n")


def game_unfolding():
    game = Game()
    game.print_menu()
    game.place_ships()
    game.computer.fill_shooting_pattern()
    print("Let the game begin!")
    print()
    print()
    round = 1
    while True:
        print("Round " + str(round))
        round += 1
        print()
        game.input_and_shoot()
        print("Computer's board:")
        print(game.computer.board)
        game.determine_a_winner()
        print()
        game.computer_shot()
        print("Human's board:")
        print(game.human.board)
        game.determine_a_winner()
