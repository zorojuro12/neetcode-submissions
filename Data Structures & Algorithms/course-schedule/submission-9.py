class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        prevMap = defaultdict(list)
        for crs, preq in prerequisites:
            prevMap[crs].append(preq)

        def dfs(crs):
            if crs in visited:
                return False

            visited.add(crs)
            for preq in prevMap[crs]:
                if not dfs(preq):
                    return False
            visited.remove(crs)
            prevMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        
