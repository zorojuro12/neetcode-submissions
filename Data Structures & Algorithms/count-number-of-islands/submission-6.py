class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, column = q.popleft()
                directions = [[-1, 0], [1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r = dr + row
                    c = dc + column

                    if (r in range(rows) and c in range(columns) and grid[r][c] == "1" and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
        
        
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        count = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    count += 1
        return count
        