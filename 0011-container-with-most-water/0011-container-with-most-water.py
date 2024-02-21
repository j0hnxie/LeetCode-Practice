class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        
        total = 0
        while l < r:
            total = max(total, ((r - l) * min(height[l], height[r])))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return total