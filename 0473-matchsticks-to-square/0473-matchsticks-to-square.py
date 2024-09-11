class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        n = len(matchsticks)
        
        if total % 4:
            return False
        
        sz = total // 4

        memo = {}

        @cache
        def helper(one, two, three, four, idx):
            if idx == n:
                return one == two == three == four
            
            if one > sz or two > sz or three > sz or four > sz:
                return False
            
            stick = matchsticks[idx]

            if helper(one + stick, two, three, four, idx + 1):
                return True
            
            if helper(one, two + stick, three, four, idx + 1):
                return True

            if helper(one, two, three + stick, four, idx + 1):
                return True
            
            if helper(one, two, three, four + stick, idx + 1):
                return True

            return False

        matchsticks.sort(reverse=True)
        
        if matchsticks[-1] > sz:
            return False

        return helper(0, 0, 0, 0, 0)