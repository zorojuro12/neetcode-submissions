class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0

        for i in range(len(nums)):
            longest = 1
            print(nums[i] - 1)
            if nums[i] - 1 not in numSet:
                while nums[i] + longest in numSet:
                    longest += 1
            maxLen = max(longest, maxLen)
        return maxLen



              
