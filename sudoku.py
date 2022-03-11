from Sudoku_Square import *

class Sudoku:
    def __init__(self, sudoku_squares):
        self.sudoku_squares = sudoku_squares

    def get_block_square_numbers(self, x, y):
        starting_x = (x % 3)*3
        stop_x = starting_x + 3
        starting_y = (x % 3)*3
        stop_y = starting_y + 3

        result = []

        for y_index in range(starting_y, stop_y, 1):
            for x_index in range(starting_x, stop_x, 1):
                number  = self.get_sudoku_square(x_index, y_index).get_number()
                if (number != -1):
                    result.append(number)


    
    def get_sudoku_square(self, x, y):
        return self.sudoku_squares[y*9+x]

        
