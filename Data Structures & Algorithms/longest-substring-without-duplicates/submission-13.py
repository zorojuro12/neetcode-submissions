class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        maxLen = 0
        hashmap = {}

        while r < len(s):
            while s[r] in hashmap:
                del hashmap[s[l]]
                l += 1
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen 
