class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        sResult = ""
        tResult = ""
        
        for i in s:
            if i == "#":
                sResult = sResult[:-1]
            else:
                sResult += i
        
        for i in t:
            if i == "#":
                tResult = tResult[:-1]
            else:
                tResult += i
                
        return tResult == sResult