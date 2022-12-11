class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dictionary = collections.defaultdict(int)
        result = 0

        for i in s:
            dictionary[i] += 1
            if dictionary[i] == 2:
                dictionary[i] = 0
                result += 2
            
        if result < len(s):
            result += 1
        
        return result
        
        
        
            