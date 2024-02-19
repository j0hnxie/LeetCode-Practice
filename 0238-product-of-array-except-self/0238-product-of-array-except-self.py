class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        front = [0 for i in range(n)]
        product = 1
        
        for i in range(n):
            num = nums[i]
            product *= num
            front[i] = product
        
        back = [0 for i in range(n)]
        product = 1
        for i in range(n - 1, -1, -1):
            num = nums[i]
            product *= num
            back[i] = product
        
        output = [0 for i in range(n)]
        for i in range(n):
            left = front[i - 1] if i > 0 else 1
            right = back[i + 1] if i < n - 1 else 1
            output[i] = left * right
        return output
            