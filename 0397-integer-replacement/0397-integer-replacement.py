class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}
        
        def helper(x):
            if x == 1:
                return 0
            
            if x in memo:
                return memo[x]
            
            if x % 2 == 0:
                memo[x] = 1 + helper(x / 2)
            else:
                memo[x] = 1 + min(helper(x - 1), helper(x + 1))
            
            return memo[x]
        return helper(n)