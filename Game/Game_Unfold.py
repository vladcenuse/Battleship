from Players.Computer import Computer
from Players.Human import Human
from ui.ui import User_Inputs_Outputs

import random
ui = User_Inputs_Outputs


class Game:
    def __init__(self):
        self.human = Human()
        self.computer = Computer()
        self.computer_won = False
        self.player_won = False
        self.computer_last_hit_coordinates = None
        self.computer_hit_a_ship = False
        self.ship_direction = None
        self.last_hit_ship_initial_row = None
        self.last_hit_ship_initial_column = None

    def place_ships(self):
        ship_size = [5, 4, 3, 3, 2]
        for size in ship_size:
            ui.input_coordinate_for_ship(size)
            self.human.input_and_add_ship(size)
            ui.board_so_far()
            print(self.human.board)
        self.computer.place_5_ships()

    def input_and_shoot(self):
        valid_shot = False
        while valid_shot == False:
            valid_shot = True
            ui.input_coordinate_for_shot()
            try:
                (row, column) = ui.input_coordinates()
                self.computer.board.check_if_position_is_valid(row, column)
                if self.computer.board.get_matrix_square_value(row, column) == 2:
                    ui.hit()
                    self.computer.board.set_matrix_square(row, column, 3)
                    for ship in self.computer.ships:
                        ship.hit_ship(row, column)
                        ship.check_if_sunk()
                        if ship.isSunk == True:
                            ui.sunk_ship()
                            self.computer.ships.remove(ship)
                            if self.computer.computer_lost() == True:
                                self.player_won = True
                else:
                    self.computer.board.set_matrix_square(row, column, 1)
                    ui.miss()
            except ValueError as ve:
                print(ve)
                valid_shot = False

    def check_for_ship_direction(self, row, column):
        #  we need to check that the neighbour squares are either 0 or 3 (unknown or hit)
        #  we need to check that squares are not outside the matrix

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
            ui.computer_shot(row, column)
            if self.human.board.get_matrix_square_value(row, column) == 2:
                ui.hit()
                self.last_hit_ship_initial_row = row
                self.last_hit_ship_initial_column = column
                self.human.board.set_matrix_square(row, column, 3)
                for ship in self.human.ships:
                    ship.hit_ship(row, column)
                    ship.check_if_sunk()
                    if ship.isSunk == True:
                        ui.computer_sunk_ship()
                        self.human.ships.remove(ship)
                        if self.human.player_lost() == True:
                            self.computer_won = True
                    else:
                        self.computer_hit_a_ship = True
                        self.computer_last_hit_coordinates = (row, column)
            else:
                self.human.board.set_matrix_square(row, column, 1)
                ui.miss()
        else:
            # we treat 2 cases, one if we know the direction of the ship and one if we don't
            self.check_for_ship_direction(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1])
            if self.ship_direction == None:  # This means that we only hit the ship once and we don't know the direction
                # we need to pick a random neighbour square
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
                ui.computer_shot(row, column)
                if self.human.board.get_matrix_square_value(row, column) == 2:
                    ui.hit()
                    self.ship_direction = self.check_for_ship_direction(row, column)
                    self.human.board.set_matrix_square(row, column, 3)
                    self.computer_last_hit_coordinates = (row, column)
                    for ship in self.human.ships:
                        ship.hit_ship(row, column)
                        ship.check_if_sunk()
                        if ship.isSunk == True:
                            ui.computer_sunk_ship()
                            self.human.ships.remove(ship)
                            self.computer_hit_a_ship = False
                            self.computer_last_hit_coordinates = None
                            if self.human.player_lost() == True:
                                self.computer_won = True

                else:
                    self.human.board.set_matrix_square(row, column, 1)
                    ui.miss()
                    self.computer_last_hit_coordinates = (self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1])
            else:  # This means that we know the direction of the ship
                if self.ship_direction == "v":
                    valid_coords = []
                    if self.computer_last_hit_coordinates[0] - 1 >= 0 and self.computer_last_hit_coordinates[0] - 1 <= 9 and self.computer_last_hit_coordinates[1] >= 0 and self.computer_last_hit_coordinates[1] <= 9:
                        if self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0] - 1, self.computer_last_hit_coordinates[1]) == 0 or self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0] - 1, self.computer_last_hit_coordinates[1]) == 2:
                            valid_coords.append((self.computer_last_hit_coordinates[0] - 1, self.computer_last_hit_coordinates[1]))
                    if self.computer_last_hit_coordinates[0] + 1 >= 0 and self.computer_last_hit_coordinates[0] + 1 <= 9 and self.computer_last_hit_coordinates[1] >= 0 and self.computer_last_hit_coordinates[1] <= 9:
                        if self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0] + 1, self.computer_last_hit_coordinates[1]) == 0 or self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0] + 1, self.computer_last_hit_coordinates[1]) == 2:
                            valid_coords.append((self.computer_last_hit_coordinates[0] + 1, self.computer_last_hit_coordinates[1]))
                    if len(valid_coords) != 0:
                        (row, column) = random.choice(valid_coords)
                    else:
                        (row,column) = (self.last_hit_ship_initial_row, self.last_hit_ship_initial_column)
                        if self.human.board.get_matrix_square_value(row + 1, column) == 3:
                            row = row - 1
                        else:
                            row = row + 1
                    temp_list = []
                    for i in self.computer.shooting_pattern:
                        if i != (row, column):
                            temp_list.append(i)
                    self.computer.shooting_pattern = temp_list
                    ui.computer_shot(row, column)
                    if self.human.board.get_matrix_square_value(row, column) == 2:
                        ui.hit()
                        self.human.board.set_matrix_square(row, column, 3)
                        self.computer_last_hit_coordinates = (row, column)
                        for ship in self.human.ships:
                            ship.hit_ship(row, column)
                            ship.check_if_sunk()
                            if ship.isSunk == True:
                                ui.computer_sunk_ship()
                                self.human.ships.remove(ship)
                                self.computer_hit_a_ship = False
                                self.computer_last_hit_coordinates = None
                                self.ship_direction = None
                                if self.human.player_lost() == True:
                                    self.computer_won = True
                    else:
                        self.human.board.set_matrix_square(row, column, 1)
                        ui.miss()
                        self.computer_last_hit_coordinates = (self.last_hit_ship_initial_row, self.last_hit_ship_initial_column)
                elif self.ship_direction == "h":
                    valid_coords = []
                    if self.computer_last_hit_coordinates[0] >= 0 and self.computer_last_hit_coordinates[0] <= 9 and self.computer_last_hit_coordinates[1] - 1 >= 0 and self.computer_last_hit_coordinates[1] - 1 <= 9:
                        if self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] - 1) == 0 or self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] - 1) == 2:
                            valid_coords.append((self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] - 1))
                    if self.computer_last_hit_coordinates[0] >= 0 and self.computer_last_hit_coordinates[0] <= 9 and self.computer_last_hit_coordinates[1] + 1 >= 0 and self.computer_last_hit_coordinates[1] + 1 <= 9:
                        if self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] + 1) == 0 or self.human.board.get_matrix_square_value(self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] + 1) == 2:
                            valid_coords.append((self.computer_last_hit_coordinates[0], self.computer_last_hit_coordinates[1] + 1))
                    if len(valid_coords) != 0:
                        (row, column) = random.choice(valid_coords)
                    else:
                        (row,column) = (self.last_hit_ship_initial_row, self.last_hit_ship_initial_column)
                        if self.human.board.get_matrix_square_value(row, column + 1) == 3:
                            column = column - 1
                        else:
                            column = column + 1
                    temp_list = []
                    for i in self.computer.shooting_pattern:
                        if i != (row, column):
                            temp_list.append(i)
                    self.computer.shooting_pattern = temp_list
                    ui.computer_shot(row, column)
                    if self.human.board.get_matrix_square_value(row, column) == 2:
                        ui.hit()
                        self.human.board.set_matrix_square(row, column, 3)
                        self.computer_last_hit_coordinates = (row, column)
                        for ship in self.human.ships:
                            ship.hit_ship(row, column)
                            ship.check_if_sunk()
                            if ship.isSunk == True:
                                ui.computer_sunk_ship()
                                self.human.ships.remove(ship)
                                self.computer_hit_a_ship = False
                                self.computer_last_hit_coordinates = None
                                self.ship_direction = None
                                if self.human.player_lost() == True:
                                    self.computer_won = True
                    else:
                        self.human.board.set_matrix_square(row, column, 1)
                        ui.miss()
                        self.computer_last_hit_coordinates = (self.last_hit_ship_initial_row, self.last_hit_ship_initial_column)


    def determine_a_winner(self):
        if self.player_won == True:
            ui.print_human_win_message()
            exit(0)
        if self.computer_won == True:
            ui.print_computer_win_message()
            exit(0)




def game_unfolding():
    game = Game()
    ui.print_menu()
    game.place_ships()
    game.computer.fill_shooting_pattern()
    ui.print_start_message()
    ui.print_blank_space()
    ui.print_blank_space()
    round = 1
    while True:
        ui.print_round(round)
        round += 1
        ui.print_blank_space()

        game.input_and_shoot()

        combined_boards = ""
        computer_board_lines = str(game.computer.board).split('\n')
        human_board_lines = str(game.human.board).split('\n')

        for comp_line, human_line in zip(computer_board_lines, human_board_lines):
            combined_boards += comp_line + "    " + human_line + "\n"

        ui.print_board_players()
        print(combined_boards)

        game.determine_a_winner()
        ui.print_blank_space()

        game.computer_shot()

        combined_boards = ""
        computer_board_lines = str(game.computer.board).split('\n')
        human_board_lines = str(game.human.board).split('\n')

        for comp_line, human_line in zip(computer_board_lines, human_board_lines):
            combined_boards += comp_line + "    " + human_line + "\n"

        ui.print_board_players()
        print(combined_boards)

        game.determine_a_winner()

