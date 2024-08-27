class Solution:
    def updateBoard(self, board, click):
        rows, cols = len(board), len(board[0])
        if board[click[0], click[1]] == 'M':
            board[click[0], click[1]] = 'X'
            return board
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        
        def countMines(row, col):
            count = 0
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if r in range(rows) and \
                   c in range(cols) and \
                   board[r][c] == 'M':
                    count += 1
            return count
        
        def dfs(row, col):
            if row not in range(rows) or \
               col not in range(cols) or \
               board[row][col] != 'E':
                return
            mines = countMines(row, col)
            if mines > 0:
                board[row][col] = str(mines)
            else:
                board[row][col] = 'B'
                for dr, dc in directions:
                    dfs(row+dr, col+dc)
        
        dfs(click[0], click[1])
        return board



