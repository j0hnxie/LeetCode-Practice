class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        if len(ransomNote) > len(magazine):
            return False
        
        chars = [0] * 26
        
        for i in magazine:
            chars[ord(i) - 97] += 1
        
        for i in ransomNote:
            chars[ord(i) - 97] -= 1
            if chars[ord(i) - 97] < 0:
                return False
            
        return True