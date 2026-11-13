class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        counts1 = {}
        for i in range(len(s1)):
            counts1[s1[i]] = counts1.get(s1[i], 0) + 1

        i = 0
        counts2 = {}
        for j in range(len(s2)):
            counts2[s2[j]] = counts2.get(s2[j], 0 ) + 1
            if (j - i + 1) > len(s1):
                counts2[s2[i]] -= 1
                if counts2[s2[i]] == 0:
                    del counts2[s2[i]]
                i += 1
            if (j - i + 1) == len(s1):
                if counts1 == counts2:
                    return True
            
        return False
