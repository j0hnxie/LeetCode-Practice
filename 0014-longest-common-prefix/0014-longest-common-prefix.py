class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        for i in range(1 , len(strs)):
            if len(strs[i]) < len(pref):
                pref = pref[:len(strs[i])]
            for j in range(len(pref)):
                if pref[j] != strs[i][j]:
                    pref = pref[:j]
                    break
            
        return pref