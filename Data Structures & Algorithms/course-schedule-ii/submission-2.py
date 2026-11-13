class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prevMap = {}
        for i in range(numCourses):
            prevMap[i] = []
        for crs, preq in prerequisites:
            prevMap[crs].append(preq)

        visit, cycle = set(), set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True

            cycle.add(crs)
            for preq in prevMap[crs]:
                if not dfs(preq):
                    return False
            cycle.remove(crs)
            output.append(crs)
            visit.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output

        