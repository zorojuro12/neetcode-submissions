class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        freqK = [[] for i in range(len(nums) + 1)]

        for n,c in count.items():
            freqK[c].append(n)

        res = []
        for i in range(len(freqK) - 1 , 0 , -1):
            for n in freqK[i]:
                res.append(n)
                if len(res) == k:
                    return res

