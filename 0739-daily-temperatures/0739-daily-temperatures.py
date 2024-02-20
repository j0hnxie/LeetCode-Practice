class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0 for i in range(n)]
        
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            
            ans[i] = stack[-1][1] - i if len(stack) else 0
            
            stack.append((temperatures[i], i))
        
        return ans