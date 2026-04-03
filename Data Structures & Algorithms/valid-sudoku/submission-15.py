class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowEntries = {}
            for entry in row:
                if entry==".":
                    continue
                else:
                    if entry in rowEntries:
                        return False
                    else:
                        rowEntries[entry] = entry

        for i in range(len(board)):
            colEntries = {}
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                else:
                    if board[j][i] in colEntries:
                        return False
                    else:
                        colEntries[board[j][i]] = board[j][i]
                    

        for sq in range(9):
            subboardEntries = {}
            for i in range(3):
                for j in range(3):
                    row = (3 * (sq//3)) + i
                    col = (3 * (sq%3)) + j

                    if board[row][col] ==".":
                        continue
                    else:
                        if board[row][col] in subboardEntries:
                            return False
                        else:
                            subboardEntries[board[row][col]] = board[row][col]
        return True

                
