class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # keep hashmap of each new char in s
        # keep hashmap of every char in t
        # when adding new char, check if value match with hash_t
        # if yes have += 1. need = len(hash_t)
        # if have == need, track resLen and res = s[l:r+1]
        # after that
        # start incrementing l and while have == need, keep track resLen and res
        # for each char l, check if in hash_t and if val matches have -= 1
        # when have no longer equal need, stop increment l and start r += 1 again until
        # have == need:

        # return res
        if t == "":
            return

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        have = 0
        need = len(count_t)
        res, resLen = [-1,-1], float("infinity")
        window = {}
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""        
                
