class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
             count[i] = 1 + count.get(i, 0) # count = num : freq

        array = []
        for num, freq in count.items():
            array.append([freq, num])
        array.sort()

        result = []
        while len(result) < k:
            result.append(array.pop()[1])
        return result     
        