class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        outputs = [intervals[0]]

        for start, end in intervals[1:]:
            prevEnd = outputs[-1][1]

            if start <= prevEnd:
                outputs[-1][1] = max(prevEnd, end)

            else:
                outputs.append([start, end])
        return outputs