from puzzle import Puzzle, get_factors

try:

    pieces_advertised = int(input("Enter the number of supposed pieces: "))

    x = float(input("Enter the horizontal size of the jigsaw image: "))
    y = float(input("Enter the vertical size of the jigsaw image: "))

    if x > y:
        picture_ratio = x / y
    else:
        picture_ratio = y / x

    puzzle = Puzzle(pieces_advertised, picture_ratio)

    puzzle.possible_grids()
    puzzle.filter_grids()
    puzzle.piece_ratio()
    puzzle.decide_best_grid()

    if puzzle.best_grid[4] > 100:
        print("JIG cannot find a way to make this ratio fit within this number of pieces."
              "That is, a piece ratio of less than 1.2 and less than 10% more pieces than the original puzzle")
    else:
        print("With a {} piece puzzle, JIG thinks it is likely that it actually has {} pieces. \n"
              "This is the result of a grid {} by {}, \n"
              "which results in piece ratios of {} and a final score of {}".format(puzzle.pieces_advertised,
                                                                                   puzzle.best_grid[2],
                                                                                   puzzle.best_grid[0],
                                                                                   puzzle.best_grid[1],
                                                                                   puzzle.best_grid[3],
                                                                                   puzzle.best_grid[4]))
except ValueError:
    print("JIG only accepts numbers...")

except ZeroDivisionError:
    print("You can´t have a 0 sided image...")
