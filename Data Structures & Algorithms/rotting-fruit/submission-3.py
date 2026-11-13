class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        visited = set()

        def bfs(r,c):

            if (r < 0 or r == ROWS or c < 0 or c == COLUMNS or grid[r][c] != 1 or (r,c) in visited):
                return 

            nonlocal fresh
            fresh -= 1
            q.append((r,c))
            visited.add((r,c))

        q = deque()
        count = 0
        fresh = 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2 and (r,c) not in visited:
                    q.append((r,c))
                    visited.add((r,c))

        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            count += 1
        return count if fresh == 0 else -1


