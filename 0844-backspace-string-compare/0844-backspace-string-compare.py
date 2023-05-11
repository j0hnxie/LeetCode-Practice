class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        i = len(s) - 1
        j = len(t) - 1
        
        while i >= 0 or j >= 0:
            skip = 0
            while i >= 0:
                if s[i] == "#":
                    skip += 1
                    i -= 1
                elif skip > 0:
                    skip -= 1
                    i -= 1
                else:
                    break
            skipJ = 0
            while j >= 0:
                if t[j] == "#":
                    skipJ += 1
                    j -= 1
                elif skipJ > 0:
                    skipJ -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False
            
            i -= 1
            j -= 1
        return True