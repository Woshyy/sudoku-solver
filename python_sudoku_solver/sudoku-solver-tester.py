from sudoku import *

p = [8, 0, 6, 0, 1, 0, 0, 0, 0,
     0, 0, 3, 0, 6, 4, 0, 9, 0,
     9, 0, 0, 0, 0, 0, 8, 1, 6,
     0, 8, 0, 3, 9, 6, 0, 0, 0,
     7, 0, 2, 0, 4, 0, 3, 0, 9,
     0, 0, 0, 5, 7, 2, 0, 8, 0,
     5, 2, 1, 0, 0, 0, 0, 0, 4,
     0, 3, 0, 7, 5, 0, 2, 0, 0,
     0, 0, 0, 0, 2, 0, 1, 0, 5]

p_hard = [0, 0, 8, 0, 0, 0, 0, 0, 0,
          2, 0, 7, 0, 5, 0, 9, 0, 0,
          0, 0, 0, 0, 0, 9, 0, 3, 0,
          5, 0, 9, 0, 7, 0, 3, 0, 0,
          0, 4, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 1, 0, 0, 0, 0, 6,
          0, 8, 0, 0, 0, 0, 2, 0, 0,
          0, 3, 0, 0, 4, 0, 0, 0, 0,
          4, 0, 2, 7, 0, 0, 0, 1, 0]

assert(len(p) == 81)

sudo = Sudoku(p, 9, 9)

#assert for getting the 3 x 3 square block in sudoku
assert (sudo.get_block_square_numbers(0, 0) == [8, 6, 3, 9])
assert (sudo.get_block_square_numbers(4, 1) == [1, 6, 4])
assert (sudo.get_block_square_numbers(8, 2) == [9, 8, 1, 6])
assert (sudo.get_block_square_numbers(0, 3) == [8, 7, 2])
assert (sudo.get_block_square_numbers(3, 3) == [3, 9, 6, 4, 5, 7, 2])
assert (sudo.get_block_square_numbers(7, 4) == [3, 9, 8])
assert (sudo.get_block_square_numbers(1, 8) == [5, 2, 1, 3])
assert (sudo.get_block_square_numbers(5, 7) == [7, 5, 2])
assert (sudo.get_block_square_numbers(7, 6) == [4, 2, 1, 5])

#assert for getting the horizontal numbers in sudoku
assert (sudo.get_horizontal_numbers(0) == [8, 6, 1])
assert (sudo.get_horizontal_numbers(1) == [3, 6, 4, 9])
assert (sudo.get_horizontal_numbers(2) == [9, 8, 1, 6])
assert (sudo.get_horizontal_numbers(3) == [8, 3, 9, 6])
assert (sudo.get_horizontal_numbers(4) == [7, 2, 4, 3, 9])
assert (sudo.get_horizontal_numbers(5) == [5, 7, 2, 8])
assert (sudo.get_horizontal_numbers(6) == [5, 2, 1, 4])
assert (sudo.get_horizontal_numbers(7) == [3, 7, 5, 2])
assert (sudo.get_horizontal_numbers(8) == [2, 1, 5])

#assert for getting the vertical numbers in sudoku.
assert (sudo.get_vertical_numbers(0) == [8, 9, 7, 5])
assert (sudo.get_vertical_numbers(1) == [8, 2, 3])
assert (sudo.get_vertical_numbers(2) == [6, 3, 2, 1])
assert (sudo.get_vertical_numbers(3) == [3, 5, 7])
assert (sudo.get_vertical_numbers(4) == [1, 6, 9, 4, 7, 5, 2])
assert (sudo.get_vertical_numbers(5) == [4, 6, 2])
assert (sudo.get_vertical_numbers(6) == [8, 3, 2, 1])
assert (sudo.get_vertical_numbers(7) == [9, 1, 8])
assert (sudo.get_vertical_numbers(8) == [6, 9, 4, 5])


sudo_hard = Sudoku(p_hard, 9, 9)
sudo_hard.solve()