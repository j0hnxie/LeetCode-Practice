class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        
        idx = 0
        res = ""
        while idx < min(len(strs[0]), len(strs[-1])) and strs[0][idx] == strs[-1][idx]:
            res += strs[0][idx]
            idx += 1
        return res