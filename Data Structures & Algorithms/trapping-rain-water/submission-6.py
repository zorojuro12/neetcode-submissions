class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        maxW = 0

        while l < r:
            if rightMax < leftMax and l < r:
                r -= 1
                water = rightMax - height[r]
                if water > 0:
                    maxW += water
                rightMax = max(rightMax, height[r])
            elif leftMax <= rightMax and l < r:
                l += 1
                water = leftMax - height[l]
                if water > 0:
                    maxW += water
                leftMax = max(leftMax, height[l])
        return maxW
