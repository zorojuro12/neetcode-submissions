class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        freq = [[-cnt, ch]for ch, cnt in count.items()]
        heapq.heapify(freq)

        res = ""
        prev = None

        while freq or prev:
            if prev and not freq:
                return ""
            cnt, ch = heapq.heappop(freq)
            res += ch
            cnt += 1

            if prev:
                heapq.heappush(freq, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, ch] 
        return res