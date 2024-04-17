class Solution:
    def isHappy(self, n: int) -> bool:
        while (n % 10) != n:
            size = int(math.log(n, 10) + 1)
            new_n = 0
            mod = 10
            for i in range(size):
                dig = n % 10
                new_n += dig * dig
                n = n // 10
            n = new_n
        return n == 1 or n == 7