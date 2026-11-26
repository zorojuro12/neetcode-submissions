class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = defaultdict(list)
        cycle = set()
        visited = set()
        for crs, prereq in prerequisites:
            prevMap[crs].append(prereq)

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)
            for preq in prevMap[crs]:
                if not dfs(preq):
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True