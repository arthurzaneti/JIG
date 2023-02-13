class Puzzle:
    def __init__(self, pieces_advertised, picture_ratio):
        self.pieces_advertised = pieces_advertised
        self.picture_ratio = picture_ratio  # don't think setting all these values to None is right, maybe there is a better way
        self.grids = None
        self.best_grid = None

    def possible_grids(self):
        grids = []
        for i in range(1, self.pieces_advertised):
            factors = get_factors(i)

            for i2 in factors:  # messy
                for i3 in factors:
                    if i2 < i3:  # checking to guarantee the ratio is bigger than one
                        if abs(i3 / i2 - self.picture_ratio) <= 0.2:  # arbitrary decision for 20% to be the maximal difference here

                            if grids.count([i3, i2]) == 0:  # checking to see if the element is already in the list
                                grids.append([i3, i2])

                    else:
                        if abs(i2 / i3 - self.picture_ratio) <= 0.2:
                            if grids.count([i2, i3]) == 0:
                                grids.append([i2, i3])

        self.grids = grids

    def piece_ratio(self):
        for i in self.grids:
            ratio = i[0] / i[1] / self.picture_ratio
            i.append(ratio)

    def filter_grids(self):
        filtered_grids = []

        for grid in self.grids:

            #  arbitrary decision to set the cap to exceeding pieces ate 10% the total advertised, might change later
            if 0 <= (grid[0] * grid[1] - self.pieces_advertised) <= (self.pieces_advertised / 10):
                filtered_grids.append([grid[0], grid[1], grid[0] * grid[1]])

        self.grids = filtered_grids

    def decide_best_grid(self):

        for grid in self.grids:
            exceeding_pieces = grid[2] - self.pieces_advertised
            score = abs(1 - grid[3]) * 100 + exceeding_pieces
            grid.append(score)

        best_grid = [0, 0, 0, 0, 100000000]  # find a way out of this later
        for grid in self.grids:
            if grid[4] < best_grid[4]:
                best_grid = grid
        self.best_grid = best_grid


def get_factors(n):
    factors = []

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors
