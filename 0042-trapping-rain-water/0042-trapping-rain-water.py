class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        l, r = 0, n - 1
        maxL, maxR = height[l], height[r]
        
        while l <= r:
            if height[l] < height[r]:
                res += max(min(maxL, maxR) - height[l], 0)
                l += 1
                maxL = max(maxL, height[l])
            else:
                res += max(min(maxL, maxR) - height[r], 0)
                r -= 1
                maxR = max(maxR, height[r])
        
        return res
                