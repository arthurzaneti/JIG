from puzzle import Puzzle

try:

    pieces_advertised = int(input("Enter the number of supposed pieces: "))

    # x = input("Enter the horizontal size of the jigsaw image: ")
    # y = input("Enter the vertical size of the jigsaw image: ")

    # picture_ratio = lambda x, y: x / y if x > y else y / x
    picture_ratio = 16 / 9

    puzzle = Puzzle(pieces_advertised, picture_ratio)
    # puzzle.get_factors()
    print(puzzle.possible_grid_sizes())



except Exception:
    pass
