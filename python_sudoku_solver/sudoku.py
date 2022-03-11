from Sudoku_Square import *

EMPTY_SQUARE = 0

class Sudoku:
    def __init__(self, sudoku_squares_numbers, height, width):
        self.height = height
        self.width = width
        self.init_sudoku_squares(sudoku_squares_numbers)
    
    def solve_like_shit(self):
        swap = True
        height = self.get_height()
        width = self.get_width()
        while (swap):
            swap = False
            for y in range(height):
                for x in range(width):
                    square = self.get_sudoku_square(x, y)
                    if (square.get_number() != EMPTY_SQUARE):
                        continue; 
                    square.set_possible_answer()
                    if (len(square.get_possible_answer()) == 1):
                        square.set_number(square.get_possible_answer().pop())
                        swap = True 
    
    def solve(self):
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                square = self.get_sudoku_square(x, y)
                if square.get_number() == EMPTY_SQUARE:
                    possible_number = square.get_possible_numbers()
                    for n in possible_number:
                        square.set_number(n)
                        self.solve()
                        square.set_number(EMPTY_SQUARE)
                    return
        self.print_sudoku()

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
        height = self.get_height()
        width = self.get_width()

        for y in range (height):
            for x in range(width):
                square = Sudoku_Square(x, y, sudoku_squares_numbers[y * width + x], self)
                self.sudoku_squares.append(square)

    def print_sudoku(self):
        height = self.get_height()
        width = self.get_width()

        for y in range(height):
            for x in range(width):
                print(" " + str(self.get_sudoku_square(x, y).get_number()) + " ", end = "")
            print("")
         
