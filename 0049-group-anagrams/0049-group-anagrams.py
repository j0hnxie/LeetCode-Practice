class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for cur in strs:
            sort = ''.join(sorted(cur))
            if sort in anagrams:
                anagrams[sort].append(cur)
            else:
                anagrams[sort] = [cur]
        res = []
        for key, value in anagrams.items():
            res.append(value)
        return res
            