class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = 0
        seen = set()
        for i in s:
            if i in seen:
                result += 2
                seen.remove(i)
            else:
                seen.add(i)
                
        if seen:
            return result + 1
        else:
            return result
        
        
        
            