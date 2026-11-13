class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prevEnd = output[-1][1]

            if start <= prevEnd:
                output[-1][1] = max(end, prevEnd)
            else:
                output.append([start, end])
        return output