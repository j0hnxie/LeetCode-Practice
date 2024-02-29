class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]
        
        for i in range(1, n):
            cur = height[i - 1]
            left[i] = max(cur, left[i - 1])
        
        for i in range(n - 2, -1, -1):
            cur = height[i + 1]
            right[i] = max(cur, right[i + 1])
        
        print(left)
        print(right)
        res = 0
        for i in range(n):
            res += max(0, min(left[i], right[i]) - height[i])
        
        return res