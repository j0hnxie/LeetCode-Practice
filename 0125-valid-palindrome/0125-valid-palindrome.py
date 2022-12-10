class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s.replace(" ", "")
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.upper()
        i = 0
        j = len(s) - 1
        print(s)
        while  i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
            
        return True