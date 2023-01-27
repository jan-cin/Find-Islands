import sys
from typing import List
from utils.file_readers import read_ocean_file


class Ocean:
    """Ocean is class for storing ocean grid and counting islands on the ocean"""
    def __init__(self, ocean_map: List[List[str]]):
        """Param ocean_map must be List[List[str] of '0' and '1'"""
        self.ocean = ocean_map
        self.island_count = 0
        self.__rows = len(self.ocean)
        self.__cols = 0 if self.__rows == 0 else len(self.ocean[0])

    def __setattr__(self, key: str, value):
        """Override of setting attribute for validating if pass ocean map is valid"""
        # assertions when ocean_map is passed
        if key == "ocean":
            # exit if ocean_map is empty
            if len(value) == 0:
                self.__dict__[key] = value
                return
            # check if ocean_map is two dimensional
            if any([isinstance(item, list) for sublist in value for item in sublist]):
                raise ValueError("Expected two dimensional list")
            # check if ocean_map has only 1s and 0s
            unpacked_ocean = [item for sublist in value for item in sublist]
            if not all([str(i) == '1' or str(i) == '0' for i in unpacked_ocean]):
                raise ValueError("Found other values than 1 and 0")
            # check if each row of ocean_map has same length
            if len(set([len(i) for i in value])) != 1:
                raise ValueError("Not all rows has same length")
            # if no above IF was fired, then passed ocean_map is correct and attribute can be set
            self.__dict__[key] = value
        else:
            self.__dict__[key] = value

    def count_islands(self):
        """Searching through ocean, marking visited lands with X and counting total number of islands"""
        for r in range(self.__rows):
            for c in range(self.__cols):
                if self.ocean[r][c] == '1':
                    self.island_count += 1
                    self.explore_island(r, c)

    def explore_island(self, r, c):
        # this should probably be private function
        """Function for exploring a tile of ocean grid. If it is lands, it is explored recursively"""
        # if we are out-of-grid, then exit
        if r < 0 or r >= self.__rows or c < 0 or c >= self.__cols:
            return
        # if we are on tile that was already visited or is water, then exit
        current_tile = self.ocean[r][c]
        if current_tile == 'X' or current_tile == '0':
            return
        # If any of the above IFs wasn't fired, then it means we are on previously not visited tile,so:
        # 1) mark it as visited
        self.ocean[r][c] = 'X'
        # 2) and explore all nearby tiles
        for iR in [-1, 0, 1]:
            for iC in [-1, 0, 1]:
                self.explore_island(r + iR, c + iC)

    def __str__(self):
        """Prints nicely formatted ocean map"""
        s = ""
        for line in self.ocean:
            s += ''.join(line) + '\n'
        return s


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("In order to run island counter, parameter with valid path to *.txt file", file=sys.stdout)
        quit()
    ocean_grid = read_ocean_file(sys.argv[1])
    o = Ocean(ocean_grid)
    o.count_islands()
    print(o.island_count, file=sys.stdout)
