class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        sR = s[::-1]
        
        return (s == sR)