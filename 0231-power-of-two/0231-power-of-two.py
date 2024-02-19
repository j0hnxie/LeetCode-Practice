class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 1
        
        while i < n:
            i *= 2
        
        if i == n:
            return True
        else:
            return False