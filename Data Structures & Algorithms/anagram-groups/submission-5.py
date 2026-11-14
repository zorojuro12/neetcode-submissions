class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return list of lists 
        # each list is words that are anagrams
        # anagrams are (act, cat) words with same length and same characters rearranged.

        # create hashmap where the dict of each word is the key and the values are the words

        dict_anagram = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            dict_anagram[tuple(count)].append(s)

        return list(dict_anagram.values())
            
