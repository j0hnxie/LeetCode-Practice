class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0]
        n = len(target)

        for idx in range(1, n):
            diff = target[idx] - target[idx - 1]
            if diff > 0:
                res += diff
        return res