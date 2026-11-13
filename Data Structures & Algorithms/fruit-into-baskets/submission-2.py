class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        count = defaultdict(list)
        maxOutput = 0
        total = 0

        for r in range(len(fruits)):
            count[fruits[r]] = count.get(fruits[r], 0) + 1
            total += 1

            while len(count) > 2:
                count[fruits[l]] -= 1
                total -= 1
                if not count[fruits[l]]:
                    del count[fruits[l]]
                l += 1

            maxOutput = max(maxOutput, total)
        return maxOutput
