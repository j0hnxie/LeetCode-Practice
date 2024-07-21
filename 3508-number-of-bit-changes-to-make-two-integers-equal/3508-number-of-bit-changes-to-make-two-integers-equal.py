class Solution:
    def minChanges(self, n: int, k: int) -> int:
        n = str(bin(n))[2:]
        k = str(bin(k))[2:]

        if len(n) < len(k):
            return -1
        
        res = 0
        for idx in range(len(k)):
            kIdx = len(k) - 1 - idx
            nIdx = len(n) - 1 - idx
            if n[nIdx] == "1" and k[kIdx] == "0":
                res += 1
            elif n[nIdx] == "0" and k[kIdx] == "1":
                return -1
        remaining = len(n) - len(k)
        for idx in range(remaining):
            nIdx = len(n) - len(k) - 1 - idx
            if n[nIdx] == "1":
                res += 1
        return res