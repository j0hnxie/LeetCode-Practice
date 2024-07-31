class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        n = a + b + c
        num_a, num_b, num_c = 0, 0, 0
        for idx in range(n):
            # print(str(idx) + " " + str(a) + " " + str(b) + " " + str(c) + " " + str(num_a) + " " + str(num_b) + " " + str(num_c))
            if (a >= b and a >= c and num_a < 2) or (num_b == 2 and a > 0 and a >= c) or (num_c == 2 and a > 0 and a >= b):
                res += "a"
                a -= 1
                num_a += 1
                num_b = 0
                num_c = 0
            elif (b >= c and b >= a and num_b < 2) or (num_a == 2 and b > 0 and b >= c) or (num_c == 2 and b > 0 and b >= a):
                res += "b"
                b -= 1
                num_b += 1
                num_a = 0
                num_c = 0
            elif (c >= b and c >= a and num_c < 2) or (num_b == 2 and c > 0 and c >= a) or (num_a == 2 and c > 0 and c >= b):
                res += "c"
                c -= 1
                num_c += 1
                num_a = 0
                num_b = 0
        return res