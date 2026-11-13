class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashset_S = {}
        hashset_T = {}

        for i in range(len(s)):
            hashset_S[s[i]] = hashset_S.get(s[i], 0) + 1
            hashset_T[t[i]] = hashset_T.get(t[i], 0) + 1

        return hashset_S == hashset_T
