class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = defaultdict(list)
        visited = set()

        for crs, prereq in prerequisites:
            prevMap[crs].append(prereq)

        def dfs(crs):
            if crs in visited:
                return False

            if prevMap[crs] == []:
                return True

            visited.add(crs)
            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            prevMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            