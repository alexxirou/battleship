import re
from itertools import islice

from randompos import *


class Ship:
    """A ship that can be placed on the grid"""

    def __repr__(self):
        """Give a representation for debugging."""
        return "Ship('{}', {})".format(self.name, self.positions)

    def __init__(self, name, positions):
        """Initialize name and position. Set hits to empty set."""
        self.name = name
        self.positions = positions
        self.hits = set()

    def __eq__(self, other):
        """Compare two ships."""
        return (self.name == other.name) and (self.positions == other.positions) and (self.hits == other.hits)

    def is_afloat(self):
        """Check if ship is afloat"""
        return self.positions != self.hits

    def shoot_at_ship(self, shot):
        """Check if the shot hits the ship. If so, remember the hit.
            Returns one of 'MISS', 'HIT', or 'DESTROYED'.
            """
        if shot in self.hits:
            res = "MISS"
        elif shot not in self.hits:
            self.hits.add(shot)
            if not self.is_afloat():
                res = "DESTROYED"
            else:
                res = "HIT"
        else:
            res = "MISS"
        return res



class Grid:
    """Encodes the grid on which the Ships are placed. Also remembers the
    shots that have been fired so far and if they were hits.
    """

    def __init__(self, sizex, sizey, ships=None, misses=None):
        """Initializes a board of the given size."""
        self.sizex = sizex
        self.sizey = sizey
        if ships == None:
            self.ships = []
        if misses == None:
            self.misses = set()

    def add_ship(self, ship):
        """Add a Ship to the grid."""
        self.ships.append(ship)
        return self.ships

    def shoot(self, shot):
        result = 0
        if shot not in self.misses:
            for ship in self.ships:
                if shot in ship.positions:
                    r = ship.shoot_at_ship(shot)
                    if r == "MISS":
                        self.misses.add(shot)
                        result = ("MISS", None)
                    if r == "HIT":
                        result= ("HIT", None)
                    if r == "DESTROYED":
                        result = ("DESTROYED", ship)
        if result != 0:
            return result
        else:
            self.misses.add(shot)
            return ("MISS", None)

class BlindGrid(Grid):
    """Encodes the opponent's view of the grid."""

    def __init__(self, Grid):
        """Given a grid, initializes hits, misses and sunken ships."""
        self.sizex = Grid.sizex
        self.sizey = Grid.sizey
        self.misses = Grid.misses
        self.sunken_ships = self._sunken_ships(Grid)
        self.hits = self._BlindGrid_hits(Grid)

    def _BlindGrid_hits(self, Grid):
        hits = set()
        for ship in Grid.ships:
            for hit in ship.hits:
                hits.add(hit)
        return hits

    def _sunken_ships(self, Grid):
        sunken_ships = []
        for ship in Grid.ships:
            if not ship.is_afloat():
                sunken_ships.append(ship)
        return sunken_ships

def load_grid_from_file(file):
    """Creating grid from a file function."""
    paramxy = []
    d = create_ship_from_line(file)
    with open(file) as file:
        first_line = file.readline()

        for coord in first_line.split(":"):
            paramxy.append(coord)
    g = Grid(int(paramxy[0]), int(paramxy[1]))

    for y in d.values():
        g.add_ship(y)
    return g


def create_ship_from_line(file):
    """Adding ships from a file function"""
    dico = {}
    i = 0
    with open(file) as file:
        for line in islice(file, 1, 6):
            ship = []
            pos = []
            for shipsinfo in re.split("[ :]", line):
                ship.append(shipsinfo)
            for x in range(1, len(ship) - 1, 2):
                list = []
                list.append(int(ship[x]))
                list.append(int(ship[x + 1]))
                list = tuple(list)
                pos.append(list)
            dico["s{0}".format(i)] = Ship(ship[0], set(pos))
            i = i + 1

    return dico


g = load_grid_from_file(filename1)
g2 = load_grid_from_file(filename2)
