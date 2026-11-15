class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        max_heap = []
        for ch, cnt in count.items():
            max_heap.append((-cnt, ch))

        heapq.heapify(max_heap)

        res = []
        prevCh = None
        while max_heap or prevCh:

            if prevCh and not max_heap:
                return ""

            cnt, ch = heapq.heappop(max_heap)
            res.append(ch)
            cnt += 1

            if prevCh:
                heapq.heappush(max_heap, prevCh)
                prevCh = None

            if cnt != 0:
                prevCh = (cnt, ch)
        return "".join(res)

