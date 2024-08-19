class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
            
        s_idx = 0
        s_len = len(s)

        for char in t:
            if s[s_idx] == char:
                s_idx += 1
            
            if s_idx == s_len:
                return True
        
        return False