class Sudoku_Square:
    def __init__(self, x, y, number, sudoku):
        self.x = x
        self.y = y
        self.number = number
        self.sudoku = sudoku

    def get_number(self):
        return self.number

    def get_possible_numbers(self):
        possible_answer = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        block_numbers = self.sudoku.get_block_square_numbers(self.x, self.y)
        for i in range (len(block_numbers)):
            possible_answer.discard(block_numbers[i])

        #remove all number in the vertical row.
        vertical_numbers = self.sudoku.get_vertical_numbers(self.x)
        for i in range (len(vertical_numbers)):
            possible_answer.discard(vertical_numbers[i])

        #remove all number in the horizontal row.
        horizontal_numbers = self.sudoku.get_horizontal_numbers(self.y)
        for i in range (len(horizontal_numbers)):
            possible_answer.discard(horizontal_numbers[i])
        
        return possible_answer
    
    def set_number(self, number):
        self.number = number