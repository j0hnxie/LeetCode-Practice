class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        lMax = 0
        rMax = 0
        res = 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] > lMax:
                    lMax = height[l]
                else:
                    res += lMax - height[l]
                l += 1
            else:
                if height[r] > rMax:
                    rMax = height[r]
                else:
                    res += rMax - height[r]
                r -= 1
        return res