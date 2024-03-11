class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        res = ""
        for char in order:
            freq = counts.get(char, 0)
            res += char * freq
            if char in counts:
                del counts[char]
        
        for char, count in counts.items():
            res += char * count
            
        return res
        
        