class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        # return the minum rate of banana/hr so we finish within h:
        minimum = r
        while l <= r:
            mid = (l + r ) // 2
            hrrate = 0
            for bn in piles:
                hrrate = hrrate + math.ceil(float(bn / mid))

            if hrrate > h:
                l = mid + 1
            else:
                minimum = min(minimum, mid)
                r = mid - 1
        return minimum
        
            

