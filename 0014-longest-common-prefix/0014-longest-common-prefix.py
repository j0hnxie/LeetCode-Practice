class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        n = len(strs[0])
        res = ""
        while i < n:
            cur = strs[0][i]
            for s in strs:
                if i == len(s):
                    return res
                
                if s[i] != cur:
                    return res
            res += cur
            i += 1
        return res