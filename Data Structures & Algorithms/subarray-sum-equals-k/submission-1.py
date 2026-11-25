class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0 : 1}
        curSum = 0
        res = 0

        for num in nums:
            curSum += num
            diff = curSum - k

            # check if prefix exists
            res = res + prefixSum.get(diff, 0)

            # add prefix to the hashmap
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1

        return res
    