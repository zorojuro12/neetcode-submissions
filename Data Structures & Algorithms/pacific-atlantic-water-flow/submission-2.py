class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLUMNS = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prevHeight):
            if (r < 0 or r == ROWS or c < 0 or c == COLUMNS or (r,c) in visit or heights[r][c] < prevHeight):
                return

            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])


        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLUMNS - 1, atlantic, heights[r][COLUMNS - 1])

        for c in range(COLUMNS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        res = []
        for r in range(ROWS):
            for c in range(COLUMNS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r, c])
        return res

        