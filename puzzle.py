class Puzzle:
    def __init__(self, pieces_advertised, picture_ratio):
        self.pieces_advertised = pieces_advertised
        self.picture_ratio = picture_ratio
        self.piece_ratio = None

    def possible_grid_sizes(self):
        grid_sizes = []
        for i in range(1, self.pieces_advertised):
            factors = get_factors(i)
            print(i)

            for i2 in factors:
                for i3 in factors:
                    if i2 < i3:
                        if abs(i3 / i2 - self.picture_ratio) <= 0.1:
                            grid_sizes.append((i2, i3))
                            print(abs(i3 / i2 - self.picture_ratio))
                        else:
                            if abs(i2 / i3 - self.picture_ratio) <= 0.1:
                                grid_sizes.append((i2, i3))
                                print(abs(i3 / i2 - self.picture_ratio))

        return grid_sizes

    def piece_ratio(self):
        pass




def get_factors(n):
    factors = []

    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    return factors
