class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounts = {}
        tCounts = {}
        
        for char in s:
            sCounts[char] = sCounts.get(char, 0) + 1
        
        for char in t:
            tCounts[char] = tCounts.get(char, 0) + 1
        
        for key, value in sCounts.items():
            if sCounts.get(key, 0) != tCounts.get(key, 0):
                return False
            
        for key, value in tCounts.items():
            if sCounts.get(key, 0) != tCounts.get(key, 0):
                return False
            
        return True
            