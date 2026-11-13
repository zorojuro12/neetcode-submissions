class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsort = sorted(nums)
        num_k =  numsort[-k:]
        for i in num_k:
            return i