class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, column = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r = row + dr
                    c = column + dc
                    if (r in range(rows) and c in range(columns) and grid[r][c] == "1" and (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))


        count = 0
        rows = len(grid)
        columns = len(grid[0])
        visit = set()

        for r in range(rows):

            for c in range(columns):

                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    count += 1
        return count