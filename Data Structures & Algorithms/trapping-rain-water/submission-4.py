class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        totalWater = 0
        maxLeft = height[l]
        maxRight = height[r]

        while l < r:
            minMax = min(maxLeft, maxRight)
            if maxLeft < maxRight:
                l += 1
                water = minMax - height[l]
                if water > 0:
                    totalWater += water
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1
                water = minMax - height[r]
                if water > 0:
                    totalWater += water
                maxRight = max(maxRight, height[r]) 
        return totalWater