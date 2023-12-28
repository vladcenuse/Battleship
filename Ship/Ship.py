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

    #TODO when implementing computer shooting patern, consider the case where we have 2 adiecent ships and we the computer hits both of them
    #TODO in caz ca 2 nave sunt lipite si le lovim pe ambele, sa nu considere ai-ul ca este doar o nava ( )
    #TODO Daca nu reusesc sa fixez asta, sa nu puna playerul navele lipite una de alta

# ship = Ship(3, "h")
# ship.horizontal_ship(0, 0)
# print(ship.coordinates)
# ship.hit_ship(0, 0)
# print(ship.coordinates)
# ship.hit_ship(0, 1)
# print(ship.coordinates)
# ship.hit_ship(0, 2)
# print(ship.coordinates)
# ship.check_if_sunk()
# print(ship.isSunk)