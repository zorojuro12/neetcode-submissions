class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        fresh = 0
        q = deque()

        def bfs(r,c):
            if (r < 0 or r == rows or c < 0 or c == columns or grid[r][c] != 1 or (r,c) in visited):
                return 

            nonlocal fresh
            if grid[r][c] == 1 and (r,c)not in visited:
                fresh -= 1
                visited.add((r,c))
                q.append([r,c])



        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
        
        level = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            level += 1

        return level if fresh == 0 else -1
            

