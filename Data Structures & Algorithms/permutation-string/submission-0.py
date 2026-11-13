class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1 = {}
        for l in range(len(s1)):
            count_s1[s1[l]] = count_s1.get(s1[l], 0) + 1

        i = 0
        count_s2 = {}
        for j in range(len(s2)):
            count_s2[s2[j]] = count_s2.get(s2[j], 0) + 1
            if (j - i + 1) > len(s1):
                count_s2[s2[i]] -= 1
                if count_s2[s2[i]] == 0:
                    del count_s2[s2[i]]
                i += 1
            if (j - i + 1) == len(s1):
                if count_s1 == count_s2:
                    return True
        return False