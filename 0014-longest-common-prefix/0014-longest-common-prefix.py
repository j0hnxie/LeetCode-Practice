class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        n = len(min(strs))
        
        res = ""
        while i < n:
            cur = strs[0][i]
            for s in strs:
                if s[i] != cur:
                    return res
                
            res += cur
            i += 1
        return res
            