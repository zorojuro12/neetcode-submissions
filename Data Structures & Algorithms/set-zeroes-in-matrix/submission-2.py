class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        ROWS = [False] * rows
        COLS = [False] * cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    ROWS[r] = True
                    COLS[c] = True

        for r in range(rows):
            for c in range(cols):
                if ROWS[r] == True or COLS[c] == True:
                    matrix[r][c] = 0


        