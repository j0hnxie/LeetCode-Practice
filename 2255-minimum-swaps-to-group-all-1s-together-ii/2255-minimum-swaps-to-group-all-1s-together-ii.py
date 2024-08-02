class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        ones = []

        for num in nums:
            if num == 1:
                total += 1
            ones.append(total)
        
        if total == len(nums) or total == 0:
            return 0
        
        res = float('inf')
        for start in range(n):
            end = (start + total - 1) % (n)
            ones_num = 0
            if end < start:
                # print(start)
                # print(ones[-1] - ones[start])
                # print(ones[end] - ones[0])
                # print()
                ones_num = ones[-1] - ones[start] + nums[start] + ones[end] - ones[0] + nums[0]
            else:
                ones_num = ones[end] - ones[start] + nums[start]
            swaps = total - ones_num
            res = min(res, swaps)
        return res  

            