class Solution:
    def minChanges(self, n: int, k: int) -> int:
        k ^= n
        diffs = bin(k).count("1")
        k &= n
        return diffs if diffs == bin(k).count("1") else -1