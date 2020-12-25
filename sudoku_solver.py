class SudokuSolver:
    """
    intializes the boards
    @param: Board as 2d Matrix
    @return: None
    """
    def __init__(self, board):
        self.board = board

    """
    This method prints the board
    @param: None
    @return: None
    """
    def print_board(self):
        for row_index in range(len(self.board)):
            if row_index % 3 == 0:
                print("--------------------")
            for col_index in range(len(self.board[0])):
                if col_index %3 == 0:
                    print("|", end="")
                
                if col_index == 8:
                    print(self.board[row_index][col_index], end="\n")
                else:
                    print(str(self.board[row_index][col_index])+" ", end="")
    
    """
    This method sove sudoku using backtracking algorithm
    @param: None
    @return: Solution 
    """
    def solve_sudoko(self):
        #To find empty space in the board
        isEmpty = find_empty_space(self.board)
        if isEmpty:
            row = isEmpty
            col = isEmpty
        else:
            return True
        
        for i in range(1,10):
            #chekh is the move is valid
            if isValid(self.board, (row, col), i):
                self.board[row][col] = i

                if self.solve_sudoko():
                    return True
                
                self.board[row][col] = 0
        return False
    
    """
    This method finds the empty space in the board
    @param: None
    @return: row index, column index
    """
    def isEmpty(self):
        for row_index in range(len(self.board)):
            for col_index in range(len(self.board[0])):
                if self.board[row_index][col_index] == 0:
                    return (row_index, col_index)
        return None








"""
Driver Method for testing Sudoko Solver
"""
def main():
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    Solution = SudokuSolver(board)
    Solution.print_board()
    Solution.solve_sudoko()

if __name__ == "__main__":
    main()