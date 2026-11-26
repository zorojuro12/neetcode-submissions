class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLUMNS = len(board[0])
        visited = set()

        def dfs(r,c):

            if (r < 0 or r == ROWS or c < 0 or c == COLUMNS or board[r][c] != 'O' or (r,c) in visited):
                return

            board[r][c] = 'T'
            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for c in range(COLUMNS):
            if board[0][c] == 'O' and (0,c) not in visited:
                dfs(0,c)
            if board[ROWS - 1][c] == 'O' and (ROWS - 1, c) not in visited:
                dfs(ROWS - 1, c)

        for r in range(ROWS):
            if board[r][0] == 'O' and (r, 0) not in visited:
                dfs(r, 0)
            if board[r][COLUMNS - 1] == 'O' and (r, COLUMNS - 1) not in visited:
                dfs(r, COLUMNS - 1)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        