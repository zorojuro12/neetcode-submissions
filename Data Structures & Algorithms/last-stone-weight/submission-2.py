class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones = [list of weight of ith stone]
        # Step : 2 heavist with weight x and y and smash them.
        # if x == y: both destoryed
        # if x < y: weight of y = y - x and vice versa

        max_heap_stones = [-wgt for wgt in stones]
        heapq.heapify(max_heap_stones)
        while len(max_heap_stones) > 1:
            heavy_1 = -heapq.heappop(max_heap_stones)
            heavy_2 = -heapq.heappop(max_heap_stones)

            if heavy_1 > heavy_2:
                heavy_1 = heavy_1 - heavy_2
                heapq.heappush(max_heap_stones, -heavy_1)
            
        if len(max_heap_stones) > 1:
            print("Error")
        elif len(max_heap_stones) == 1:
            for stone in max_heap_stones:
                return -stone
        elif (len(max_heap_stones) == 0):
            return 0