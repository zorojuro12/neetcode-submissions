class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        r = 0
        maxLength = 0

        for c in s:
            while c in charset:
                charset.remove(s[l])
                l += 1

            charset.add(c)
            maxLength = max(maxLength, r - l + 1)
            r += 1
        return maxLength
