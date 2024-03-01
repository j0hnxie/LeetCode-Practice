class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        total = len(s)
        ones = 0
        
        for char in s:
            if char == "1":
                ones += 1
        
        res = "1" * (ones - 1) + "0" * (total - ones) + "1"
        return res