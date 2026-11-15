class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        res = []
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            l = i + 1
            r = len(nums) - 1
            target = 0

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < target and l < r:
                    l += 1
                elif threeSum > target and l < r:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
                        
