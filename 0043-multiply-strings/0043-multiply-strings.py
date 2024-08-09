class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            large = num1
            small = num2
        else:
            large = num2
            small = num1

        n = len(large)
        m = len(small)

        res = 0
        factor = 1
        for idx in range(1, m + 1):
            cur_res = 0
            cur_m = int(small[m - idx])
            cur_factor = 1
            for idx2 in range(n):
                cur_n = int(large[n - 1 - idx2])
                cur_product = cur_m * cur_n
                cur_product *= cur_factor
                cur_factor *= 10
                cur_res += cur_product
            cur_res *= factor
            factor *= 10
            res += cur_res

        return str(res)

