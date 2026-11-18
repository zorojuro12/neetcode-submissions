class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # a, b mean b before a

        prevMap = defaultdict(list)
        for crs, preq in prerequisites:
            prevMap[crs].append(preq)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if prevMap[crs] == []:
                return True

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