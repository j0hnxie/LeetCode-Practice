class Solution:
    def minSteps(self, n: int) -> int:
        factor = 2

        res = 0
        while n > 1:
            while n % factor == 0:
                n //= factor
                res += factor
            factor += 1
        return res