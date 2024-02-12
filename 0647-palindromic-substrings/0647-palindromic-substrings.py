class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = [[False for i in range(n)] for j in range(n)]
        count = 0
        
        for i in range(n):
            memo[i][i] = True
            count += 1
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                memo[i][i + 1] = True
                count += 1
        
        for i in range(3, n + 1):
            for j in range(n - i + 1):
                if s[j] == s[j + i - 1] and memo[j + 1][j + i - 2]:
                    memo[j][j + i - 1] = True
                    count += 1
                
        return count