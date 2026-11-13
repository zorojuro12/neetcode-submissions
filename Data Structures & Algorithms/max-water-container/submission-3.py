class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxW = 0

        while l < r:
            if heights[l] < heights[r]:
                water = min(heights[l], heights[r]) * (r - l)
                maxW = max(water, maxW)
                l += 1
            else:
                water = min(heights[l], heights[r]) * (r - l)
                maxW = max(water, maxW)
                r -= 1
        return maxW
