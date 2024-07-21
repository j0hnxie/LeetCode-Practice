class Solution:
    def maxOperations(self, s: str) -> int:
        cur_cluster, res = 0, 0
        in_cluster = False
        for idx, char in enumerate(s):
            if char == "1":
                if not in_cluster:
                    res += cur_cluster
                cur_cluster += 1
                in_cluster = True
            else:
                in_cluster = False
        return res if s[-1] == "1" else res + cur_cluster