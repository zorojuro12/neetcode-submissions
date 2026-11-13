class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            prevEnd = output[-1][1]

            if start <= prevEnd:
                output[-1][1] = max(end, prevEnd)
            else:
                output.append([start,end])
        return output
