class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        n = min(n1, n2)

        res = ""
        cur = ""
        for sz in range(n):
            pre1, pre2 = str1[:sz + 1], str2[:sz + 1]
            if pre1 != pre2:
                # print("INEQUAL STRINGS")
                return res

            cur += str1[sz]

            if n1 % (sz + 1) != 0 or n2 % (sz + 1) != 0:
                continue

            n1_times, n2_times = n1 // (sz + 1), n2 // (sz + 1)

            if pre1 * n1_times != str1 or pre2 * n2_times != str2:
                continue
            else:
                res = cur
            

        return res