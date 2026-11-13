class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        total = 0

        while l < r:
            minMax = min(maxLeft, maxRight)
            water = 0
            if maxLeft < maxRight:
                l += 1
                water = minMax - height[l]
                if water >= 0:
                    total += water
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1
                water = minMax - height[r] 
                if water >= 0:
                    total += water
                maxRight = max(maxRight, height[r])
        
        return total
