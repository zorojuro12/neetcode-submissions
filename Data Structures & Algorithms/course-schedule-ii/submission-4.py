class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        prevMap = defaultdict(list)
        visited = set()
        cycle = set()

        for crs, preq in prerequisites:
            prevMap[crs].append(preq)

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
            res.append(crs)
            visited.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res