class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for row in board:
            if not self.check(row):
                return False
        columns = zip(*board)
        for column in columns:
            if not self.check(column):
                return False
        grids = [[] for idx in range(9)]
        for row_idx in range(3):
            for column_idx in range(3):
                for grid_idx in range(3):
                    grids[row_idx * 3 + column_idx].\
                        extend(board[grid_idx + column_idx * 3][row_idx * 3: (row_idx + 1) * 3])
                if not self.check(grids[row_idx * 3 + column_idx]):
                    return False
        return True
    
    # @param num, a list of num
    # @return if all num in nums is unique
    def check(self, nums):
        flag = 0b000000000
        for num in nums:
            if num.isdigit():
                f = 0b10 << (int(num) - 1)
                if flag & f == f:
                    return False
                else:
                    flag = flag | f
        return True
