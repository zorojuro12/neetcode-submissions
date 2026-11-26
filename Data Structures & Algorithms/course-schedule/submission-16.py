class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = defaultdict(list)
        cycle = set()
        for crs, prereq in prerequisites:
            prevMap[crs].append(prereq)

        def dfs(crs):
            if crs in cycle:
                return False

            if prevMap[crs] == []:
                return True

            cycle.add(crs)
            for preq in prevMap[crs]:
                if not dfs(preq):
                    return False
            
            cycle.remove(crs)
            prevMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True