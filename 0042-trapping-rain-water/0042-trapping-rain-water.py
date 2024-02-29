class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        cur = 0
        res = 0
        
        while cur < n:
            while stack and height[cur] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                dist = cur - stack[-1] - 1
                vol = dist * (min(height[stack[-1]], height[cur]) - height[top])
                res += vol
            
            stack.append(cur)
            cur += 1
        return res