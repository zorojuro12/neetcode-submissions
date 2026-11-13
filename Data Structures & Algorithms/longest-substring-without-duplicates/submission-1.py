class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l  = 0 
        count = 0
        charset = set()

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            count = max(r - l + 1, count)
        return count