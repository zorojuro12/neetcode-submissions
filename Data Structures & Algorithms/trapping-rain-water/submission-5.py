class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        totalWater = 0

        while l < r:
            if maxLeft < maxRight and l < r:
                l += 1
                water = maxLeft - height[l]
                if water > 0:
                    totalWater += water
                maxLeft = max(maxLeft, height[l])
                
            elif maxRight <= maxLeft and l < r:
                r -= 1
                water = maxRight - height[r]
                if water > 0:
                    totalWater += water
                maxRight = max(maxRight, height[r])
        return totalWater

                
