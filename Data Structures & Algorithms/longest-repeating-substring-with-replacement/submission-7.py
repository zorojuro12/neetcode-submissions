class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_cnt = {}

        # window count - most occuring character <= k (valid window)
        # hashmap to keep count of charcters in window
        # max of hashmap.keys()

        l = 0
        r = 0
        maxL = 0

        while r < len(s):
            window_cnt[s[r]] = window_cnt.get(s[r], 0) + 1

            # check if not valid window, make it valid
            while (r - l + 1) - max(window_cnt.values()) > k:
                window_cnt[s[l]] -= 1
                if window_cnt[s[l]] == 0:
                    del window_cnt[s[l]]
                l += 1
            
            maxL = max(maxL, r - l + 1)
            r += 1
        return maxL