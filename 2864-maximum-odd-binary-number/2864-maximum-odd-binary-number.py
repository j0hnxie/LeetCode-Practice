class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        total = len(s)
        ones = 0
        
        for char in s:
            if char == "1":
                ones += 1
        
        res = ""
        for i in range(ones - 1):
            res += "1"
        for i in range(total - ones):
            res += "0"
        res += "1"
        return res