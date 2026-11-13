class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        arr1 = []
        for i in range(len(nums) - 1):
            arr1.append(nums[i])

        arr2 = []
        for i in range(1, len(nums)):
            arr2.append(nums[i])

        memo1 = [-1] * (len(nums) - 1)
        memo2 = [-1] * (len(nums) - 1)

        def dfs(i, nums, memo):
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]

            memo[i] = max(dfs(i+1, nums, memo), nums[i] + dfs(i+2, nums, memo))
            return memo[i]

        return max(dfs(0, arr1, memo1), dfs(0, arr2, memo2))