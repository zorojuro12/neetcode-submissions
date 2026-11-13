class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charset = set()
        maxLen = 0

        for r in range(len(s)):
            if s[r] in charset:
                while s[r] in charset:
                    charset.remove(s[l])
                    l += 1
            charset.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen

