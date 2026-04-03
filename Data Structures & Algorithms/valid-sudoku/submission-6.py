class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            this_row = {}
            for j in range(9):
                item = board[i][j]
                if item == ".":
                    pass
                else:
                    if item in this_row:
                        return False
                    else:
                        this_row[item] = item

        for i in range(9):
            this_column = {}
            for j in range(9):
                item = board[j][i]
                if item == ".":
                    pass
                else:
                    if item in this_column:
                        return False
                    else:
                        this_column[item] = item
        matrix  = []
        for sq in range(9):
            sub_board = {}
            for i in range(3):
                for j in range(3):
                    row = (sq//3) * 3 + i
                    col = (sq%3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in sub_board:
                        return False
                    else:
                        sub_board[board[row][col]] = board[row][col]
            
        return True



 

