class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        letters = collections.defaultdict(int)
        
        for i in magazine:
            letters[i] += 1
        
        for i in ransomNote:
            letters[i] -= 1
            if letters[i] < 0:
                return False
            
        return True
            