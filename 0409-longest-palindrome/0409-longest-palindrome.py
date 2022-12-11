class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        sets = set()
        
        for i in s:
            if i in sets:
                sets.remove(i)
            else:
                sets.add(i)
            
        if len(sets) != 0:
            return len(s) - len(sets) + 1
        else:
            return len(s)
        
        
        
            