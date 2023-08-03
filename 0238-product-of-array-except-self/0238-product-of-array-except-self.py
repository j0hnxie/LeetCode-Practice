class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(nums)
        pre = [0] * len(nums)
        pre[0] = nums[0]
        post = [0] * len(nums)
        post[-1] = nums[-1] 
        
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i]
            
        # print(pre)
        # print(post)
        
        for i in range(len(nums)):
            if i == 0:
                res[i] = post[i + 1]
            elif i == len(nums) - 1:
                res[i] = pre[i - 1]
            else:
                res[i] = pre[i - 1] * post[i + 1]
            
        return res
            
                