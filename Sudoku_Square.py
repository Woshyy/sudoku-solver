class Sudoku_Square:
    def __init__(self, x, y, number, sudoku):
        self.x = x
        self.y = y
        self.number = number
        self.sudoku = sudoku
        self.possible_answer = {}
    
    def set_possible_answer(self):
        self.possible_answer = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        #remove all numbers in the 9 x 9 block.
        block_square = self.sudoku.get_block_square_numbers(self.x, self.y)
        for i in range (len(block_square)):
            self.possible_answer.discard(block_square[i])

        #remove all number in the vertical row.

        #remove all number in the horizontal row.
        return

    def get_number(self):
        return self.number
    
    def set_number(self, number):
        self.number = number