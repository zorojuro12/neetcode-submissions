class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        for i in range(len(nums)): # i = 0
            curSum = 0 # curSUm = 2
            for j in range(i, len(nums)): # j = 1 to 5
                curSum += nums[j]
                if curSum >= target:
                    minLen = min(minLen, j - i + 1)
                    break
        return 0 if minLen == float("inf") else minLen
