class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        i = 0
        while i < len(s):
            # print(s)
            if s[i] == "#":
                if i == 0:
                    s = s[1: len(s)]
                else:
                    s = s[0: i - 1] + s[i + 1: len(s)]
                    i -= 1
            else:
                i += 1
        
        i = 0
        while i < len(t):
            if t[i] == "#":
                if i == 0:
                    t = t[1:len(t)]
                else:
                    t = t[0: i - 1] + t[i + 1: len(t)]
                    i -= 1
            else:
                i += 1
                
        # print(s)
        # print(t)
                
        return s == t