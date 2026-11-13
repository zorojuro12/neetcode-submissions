class Solution:
    def rob(self, nums: List[int]) -> int:

        for i in range(len(nums) - 3, -1, -1):
            maxAmt = 0
            for j in range(i+2, len(nums), 1):
                maxAmt = max(maxAmt, nums[i] + nums[j])
            nums[i] = maxAmt

        return max(nums)