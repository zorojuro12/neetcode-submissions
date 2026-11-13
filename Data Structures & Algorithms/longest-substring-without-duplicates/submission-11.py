class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        count = {}
        maxLength = 0
        
        while r < len(s):
            if s[r] not in count:
                count[s[r]] = count.get(s[r], 0) + 1
                maxLength = max(maxLength, r - l + 1)
                r += 1
            else:
                while s[r] in count:
                    count[s[l]] -= 1
                    if count[s[l]] == 0:
                        count.pop(s[l])
                    l += 1
        return maxLength

