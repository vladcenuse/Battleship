class Ship:
    def __init__(self, size, orientation):
        self.size = size
        self.coordinates = []
        self.isSunk = False
        self.orientation = orientation

    def horizontal_ship(self, row, column):
        self.orientation = "h"
        for i in range(self.size):
            self.coordinates.append([row , column + i])

    def vertical_ship(self, row, column):
        self.orientation = "v"
        for i in range(self.size):
            self.coordinates.append([row + i, column ])

    def check_if_sunk(self):
        if len(self.coordinates) == 0:
            self.isSunk = True
        else:
            self.isSunk = False

    def hit_ship(self, row, column):
        if [row, column] in self.coordinates:
            self.coordinates.remove([row, column])

