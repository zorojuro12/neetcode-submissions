class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k = len(nums)
        for i in nums:
            if len(nums) < 2 * k:
                nums.append(i)
        return nums