class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        maxHeap = []
        for c, cnt in count.items():
            maxHeap.append([-cnt, c])
        heapq.heapify(maxHeap)

        res = ""
        prev = None
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res


            
        