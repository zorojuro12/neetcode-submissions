class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, num in enumerate(temperatures):
            while stack and num > stack[-1][0]:
                temp, idx = stack.pop()
                res[idx] = i - idx

            stack.append([num, i])
        return res



