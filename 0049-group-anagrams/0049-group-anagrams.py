class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sort = str(sorted(s))
            if sort in groups:
                groups[sort].append(s)
            else:
                groups[sort] = [s]
        
        res = []
        for key, value in groups.items():
            res.append(value)
        
        return res
        