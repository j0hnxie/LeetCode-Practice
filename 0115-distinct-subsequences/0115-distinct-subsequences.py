class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        memo = [[0] * n for _ in range(m)]

        cur = 0
        for start_idx in range(n):
            if t[0] == s[start_idx]:
                cur += 1
            memo[0][start_idx] = cur

        for final_idx in range(1, m):
            for start_idx in range(1, n):
                memo[final_idx][start_idx] = memo[final_idx][start_idx - 1]
                if t[final_idx] == s[start_idx]:
                    memo[final_idx][start_idx] += memo[final_idx - 1][start_idx - 1]
        
        # print(memo)
        return memo[-1][-1]