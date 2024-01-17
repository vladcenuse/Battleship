class User_Inputs_Outputs:
    def __init__(self):
        pass

    @staticmethod
    def place_ship():
        row = int(input("Row: "))
        column = int(input("Column: "))
        orientation = input("Orientation(h/v):  ")

        return (row,column,orientation)
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
    @staticmethod
    def print_blank_space():
        print()
    @staticmethod
    def print_board_players():
        print("Computer's board:                              Human's board:")
    @staticmethod
    def print_start_message():
        print("Let the game begin!")
    @staticmethod
    def print_round(round):
        print("Round " + str(round))
    @staticmethod
    def print_human_win_message():
        print("The human has won! Congratulations")
    @staticmethod
    def print_computer_win_message():
        print("The human has lost! Take the L")
    @staticmethod
    def input_coordinate_for_ship(size):
        print("Enter the coordinates for the ship of size " + str(size))
    @staticmethod
    def board_so_far():
        print("Your board looks like this so far: ")
    @staticmethod
    def input_coordinate_for_shot():
        print("Enter the coordinates for the shot: ")
    @staticmethod
    def input_coordinates():
        row = int(input("Row: "))
        column = int(input("Column: "))
        return (row,column)
    @staticmethod
    def hit():
        print("HIT!")
    @staticmethod
    def miss():
        print("MISS!")
    @staticmethod
    def sunk_ship():
        print("You sunk a ship!")
    @staticmethod
    def computer_sunk_ship():
        print("The computer sunk a ship!")
    @staticmethod
    def computer_shot(row,column):
        print("Computer shoots: " + str(row) + " " + str(column))