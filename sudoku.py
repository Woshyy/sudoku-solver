from pickle import EMPTY_TUPLE
from Sudoku_Square import *

EMPTY_SQUARE = 0

class Sudoku:
    def __init__(self, sudoku_squares_numbers, height, width):
        self.init_sudoku_squares(sudoku_squares_numbers)
        self.height = height
        self.width = width

    #get all the numbers that has been chosen on the 9 x 9 square
    def get_block_square_numbers(self, x, y):
        starting_x = (x // 3)*3
        stop_x = starting_x + 3
        starting_y = (y // 3)*3
        stop_y = starting_y + 3

        result = []

        for y_index in range(starting_y, stop_y, 1):
            for x_index in range(starting_x, stop_x, 1):
                number  = self.get_sudoku_square(x_index, y_index).get_number()
                if (number != EMPTY_SQUARE):
                    result.append(number)
                    
        return result

    def get_horizontal_numbers(self, y):
        result = []
        width = self.get_width()

        for x in range(width):
            number  = self.get_sudoku_square(x, y).get_number()
            if (number != EMPTY_SQUARE):
                result.append(number)

        return result
    
    def get_vertical_numbers(self, x):
        result = []
        height = self.get_height()

        for y in range(height):
            number  = self.get_sudoku_square(x, y).get_number()
            if (number != EMPTY_SQUARE):
                result.append(number)

        return result


    
    def get_sudoku_square(self, x, y):
        return self.sudoku_squares[y * self.get_height() + x]
    
    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width
    
    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def init_sudoku_squares(self, sudoku_squares_numbers):
        self.sudoku_squares = []

        for i in range(len(sudoku_squares_numbers)):
            self.sudoku_squares.append(Sudoku_Square(sudoku_squares_numbers[i], self))
        
