class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        
        def addLand(r, c):
            if (r < 0 or r == rows or c < 0 or c == columns or grid[r][c] == -1 or (r,c) in visited):
                return 
            q.append([r,c])
            visited.add((r,c))
        
        
        q = deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0 and (r,c) not in visited:
                    q.append([r,c])
                    visited.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addLand(r + 1, c)
                addLand(r - 1, c)
                addLand(r, c - 1)
                addLand(r, c + 1)

            dist += 1
