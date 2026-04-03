class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True
        # check rows validity
        for row in board:
            rowItems = {}
            for item in row:
                if item == ".":
                    continue
                else:
                    if item in rowItems:
                        isValid = False
                        return isValid
                    else:
                        rowItems[item] = item
        # check columns validity
        for i in range(9):
            colItems = {}
            for j in range(9):
                if board[j][i] == ".":
                    continue
                else:
                    if board[j][i] in colItems:
                        isValid = False
                        return isValid
                    else:
                        colItems[board[j][i]] = board[j][i]

        # check subboards
        for sub in range(9):
            subItems = {}
            for i in range(3):
                for j in range(3):
                    row = (3*(sub//3)) + i
                    col = (3*(sub%3)) + j
                    if board[row][col] == ".":
                        continue
                    else:
                        if board[row][col] in subItems:
                            isValid = False
                            return isValid
                        else:
                            subItems[board[row][col]] = board[row][col]

        return isValid

