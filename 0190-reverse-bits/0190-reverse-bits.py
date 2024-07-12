class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        for idx in range(32):
            res = res << 1
            cur = n & 1
            res += cur
            n = n >> 1
        return res