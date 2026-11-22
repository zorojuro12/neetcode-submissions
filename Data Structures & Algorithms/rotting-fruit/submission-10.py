class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        q = deque()
        fresh = 0

        def bfs(r, c):
            if (r < 0 or r == rows or c < 0 or c == columns or grid[r][c] != 1 or (r,c) in visited):
                return
            
            nonlocal fresh
            if grid[r][c] == 1 and (r,c) not in visited:
                fresh -= 1
                q.append([r,c])
                visited.add((r, c))
            return


        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        minutes = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            minutes += 1
        
        return minutes if fresh == 0 else -1