class Solution:
    def findComplement(self, num: int) -> int:
        num_str = bin(num)[2:]
        res = ""
        for char in num_str:
            if char == "1":
                res += "0"
            else:
                res += "1"

        return int(res, 2)