class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = []
        for i in nums:
            j = i ** 2
            squared.append(j)
        
        return sorted((squared))