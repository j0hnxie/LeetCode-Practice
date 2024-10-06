class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        memo = [[0] * len2 for _ in range(len1)]

        memo[0][0] = 1 if text1[0] == text2[0] else 0

        for idx1 in range(1, len1):
            memo[idx1][0] = max(1 if text2[0] == text1[idx1] else 0, memo[idx1 - 1][0])
        
        for idx2 in range(1, len2):
            memo[0][idx2] = max(1 if text1[0] == text2[idx2] else 0, memo[0][idx2 - 1])

        for idx1 in range(1, len1):
            for idx2 in range(1, len2):
                if text1[idx1] == text2[idx2]:
                    memo[idx1][idx2] = max(memo[idx1][idx2], memo[idx1 - 1][idx2 - 1] + 1)
                else:
                    memo[idx1][idx2] = max(memo[idx1 - 1][idx2], memo[idx1][idx2 - 1])
        return memo[-1][-1]